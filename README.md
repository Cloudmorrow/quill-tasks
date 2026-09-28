# Tasks

A Quill for [Cloudmorrow](https://github.com/Cloudmorrow/cloudmorrow): boards,
and three lanes on each — **To Do**, **Doing**, **Done** — because that is
what a board is for.

- A task is a title and a Markdown body, which is where its detail and its
  subtasks (`- [ ]` lines) live.
- Done empties itself: a week after a task is finished, it goes.
- Everyone starts with a board named after them.

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
