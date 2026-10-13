# Tasks

A Quill for [Cloudmorrow](https://github.com/Cloudmorrow/cloudmorrow): boards,
and three lanes on each — **To Do**, **Doing**, **Done** — because that is
what a board is for.

- A task is a title and a Markdown body, which is where its detail and its
  subtasks (`- [ ]` lines) live.
- Done empties itself: a week after a task is finished, it goes.
- Everyone starts with a board named after them.

## Using it

A board is picked from a dropdown that is also where you make one, and has
three lanes: To Do, Doing, Done. A task's detail and its `- [ ]` subtasks
are its Markdown body, the same thing the editor already knows how to
write and tick. Done empties itself — a task is deleted a week after it got
there, and every card says how long it has left — so the lane stays what
you finished recently rather than everything you ever finished.

**Working a board:**

#### In the web app

The **Tasks** tab: the board from the dropdown, its three lanes, and the
plus beside the title for a new task. Drag a card between lanes with the
mouse, or with a finger; tap one for its sheet, where **Duplicate** puts a
copy in To Do. **Clear Done now** is on the board's sheet.

#### In the terminal app

The **Tasks** card (`f2`): `ctrl+n` makes a task in To Do, `[` and `]`
move the one under the cursor between lanes, `enter` opens its sheet,
`ctrl+b` makes a board, and the toolbar renames or deletes the one shown.

#### On the command line

```
cm tasks list                              # the board, lane by lane
cm tasks add "Repot the fig" due=2026-10-01
cm tasks done fig                          # by the start of its id, or its title
cm tasks move 8f2c doing
cm tasks groups                            # the boards
cm tasks list -g Garden                    # another board
cm tasks duplicate 8f2c
cm tasks clear-done
```

---

## What it adds to your Cloudmorrow

| | |
| --- | --- |
| Datamodels | uses the foundational `board` and `task` (domain *Tasks*) |
| Screens | one board, on the phone, the web app, the terminal, `cm tasks`, and to your assistant |
| Jobs | `sweep_done`: deletes tasks that have been done for seven days |
| Datasets | `first_board`: one board for each person, the first time they open Tasks |
| Actions | **Duplicate** a task into To Do; **Clear Done now** on a board — on its sheet, `cm tasks duplicate`, `cm tasks clear-done`, and to your assistant |
| Services, webhooks, APIs | none |

Its code is [`quill.py`](quill.py): the two actions, run in the sandbox as whoever presses them. Everything else is declared in [`quill.toml`](quill.toml).

## Working on it

See [CLAUDE.md](CLAUDE.md) and the skills in `.claude/skills/`. In short:

```
uv sync                  # .venv with Cloudmorrow and pytest
cm quill check           # the manifest, as a server would install it
cm quill test            # tests/, against the real record store and gate
cm quill test --sandbox  # the same, with the code in the sandbox
cm quill dev --local     # a throwaway server here, reinstalled as you save
```

## Licence

AGPL-3.0-or-later.
