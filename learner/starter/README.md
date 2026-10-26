# Tiny Shop Checkout

Welcome to a small Python checkout project. It calculates a cart total from a list of items. The project is intentionally simple so you can focus on how Codex learns project-specific working agreements.

## Project map

- `src/checkout.py` contains the public function `calculate_total(items)`.
- `tests/test_checkout.py` contains visible tests.
- `sample_orders.json` contains synthetic order data for inspection.

There is intentionally no `AGENTS.md` in this starter.

## Run the checks

From this directory:

```sh
python3 -m unittest discover -s tests -v
```

No package installation is required.

## Lab mission

You will work with Codex twice on the same task: once in this starter with no project instructions, and once in a clean copy after you write and review `AGENTS.md`.

1. Inspect this project without editing it. Write down its public contract and verification command.
2. In a terminal from the folder containing `starter/`, make a guided copy:

   ```sh
   cp -R starter guided-run
   ```
3. In the original copy, send the baseline task prompt from `task_card.md`. Before accepting edits, record assumptions, files changed, tests run, and anything you need to review.
4. In `guided-run`, create an `AGENTS.md`. You may start with `/init` in the Codex CLI or ask Codex to draft the file. Review every line; scaffold output is not automatically correct.
5. Start a fresh Codex session in `guided-run`. Ask Codex to summarize the project instructions and identify the active file.
6. Send the exact same task prompt in both copies. Compare the output, tests, changed files, and review effort.
7. Complete the second task in `task_card.md` to test whether your instructions generalize to a different request.

## Working in Codex CLI

Open a terminal in this starter folder and start Codex there:

```sh
codex
```

Run `/init` only in the guided copy. It generates a starting `AGENTS.md`; then inspect and edit it. Use `/status` to confirm the project folder if needed.

## Working in VS Code

Open this folder as the workspace. Open `src/checkout.py` and `tests/test_checkout.py`. Ask Codex to inspect the project first. In a second copy, create and review `AGENTS.md`, then start a fresh Codex session there before the repeat run. An open tab is useful context, but Codex's project instructions are discovered from the project path, so confirm the workspace root is the folder containing `AGENTS.md`.

## Submission

Submit your final `AGENTS.md`, the comparison worksheet, and a short note:

- What did your file help Codex remember?
- What did it fail to guarantee?
- Which rule would you turn into a test or CI check?
