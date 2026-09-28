"""Tasks' tests: the real record store and gate, and quill.py, on this machine.

`cm quill test` runs them; `cm quill test --sandbox` runs quill.py in the
sandbox, as a server does.
"""

import pytest

from cloudmorrow.quill.testing import Harness


@pytest.fixture()
def q():
    with Harness(".", circles={"Readers": {"*": "read"}}) as harness:
        yield harness


@pytest.fixture()
def board(q):
    return q.seed("board", title="House")


def test_everybody_gets_a_board_the_first_time(q):
    assert [b["title"] for b in q.list("board")] == ["alice's tasks"]


def test_a_task_moves_through_the_lanes_and_knows_when_it_was_done(q, board):
    task = q.seed("task", board=board.id, title="Repot the fig")
    assert task["lane"] == "todo"
    done = q.change("task", task.id, lane="done")
    assert done["done_at"]


def test_duplicating_a_task_puts_a_copy_in_to_do(q, board):
    task = q.seed("task", board=board.id, title="Repot the fig", body="- [ ] soil", lane="doing")
    result = q.act("duplicate", task)
    assert result.ok and result.toast == "Duplicated Repot the fig"
    (model, copy_id), = result.opened
    copy = q.get(model, copy_id)
    assert (copy["title"], copy["body"], copy["lane"]) == ("Repot the fig", "- [ ] soil", "todo")


def test_clearing_done_takes_only_this_boards_finished_tasks(q, board):
    other = q.seed("board", title="Garden")
    q.seed("task", board=board.id, title="Done here", lane="done")
    q.seed("task", board=board.id, title="Still to do")
    q.seed("task", board=other.id, title="Done elsewhere", lane="done")
    assert q.act("clear-done", board).toast == "Cleared 1 finished task"
    left = sorted(t["title"] for t in q.list("task"))
    assert left == ["Done elsewhere", "Still to do"]
    assert q.act("clear-done", board).toast == "Nothing is done on this board yet"


def test_somebody_who_may_only_read_cannot_clear_or_duplicate(q, board):
    task = q.seed("task", board=board.id, title="Mine", lane="done")
    reader = q.as_user("sam", circles=["Readers"])
    # Personal: sam cannot even see alice's board.
    assert reader.act("clear-done", board).refused
    assert reader.act("duplicate", task).refused
