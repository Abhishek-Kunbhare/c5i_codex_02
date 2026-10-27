# Repository Guidelines

## Purpose and Scope

This repository is a self-contained Codex training lab. The runnable Tiny Shop Checkout project is in `learner/starter/`; the starter intentionally has no `AGENTS.md` for the unguided exercise.

## Public Contract and Contact

`learner/starter/src/checkout.py` exposes `calculate_total(items)`. Its documented items have `name`, `price`, and `quantity`; the function returns a float. Neither repository README lists a maintainer or public contact.

## Working Rules

Read `learner/starter/task_card.md` and the relevant source and tests before changing checkout behavior. Preserve the existing `calculate_total(items)` call and float return type for Task A. Keep Task B's `format_total(total)` separate from calculation. Do not add dependencies or change the item schema for Task A.

## Verification

From `learner/starter/`, run the documented command: `python3 -m unittest discover -s tests -v`. Report the command and actual result.

## Ambiguity Handling

Check the starter README and task card when the requested behavior or exercise copy is unclear. Ask the requester if those files do not resolve the decision.
