# Day 2 AGENTS.md Lab Bundle

This is a self-contained training lab. It does not depend on the Day 1 repository.

## Contents

- `learner/starter/` is the clean learner project. It deliberately has no `AGENTS.md`.
- `learner/skill_and_mcp_lab.md` extends the exercise with Skills, plugins, MCP grounding, integration review, and safety checks.
- `learner/integration_task_template.md` is completed by the instructor for the cohort’s chosen SDK and safe local test setup.
- `instructor/integration_task_template.md` helps adapt the grounding comparison to an organization’s real SDK and component catalogue.
- `instructor/answer_key/AGENTS.md` is the instructor reference. Do not share this folder before learners draft their own instructions.
- `instructor/facilitation/` contains the answer observations and comparison worksheet.

## Recommended session use

1. learners should use `learner/starter/`.
2. Let learners inspect the project and record what Codex does with no project guidance.
3. Have them create a project-specific `AGENTS.md` with Codex `/init` or a prompt, then review and rewrite it.
4. Start a fresh Codex session in that directory so instruction discovery happens from the clean state.
5. Repeat the task in a clean copy with the same task prompt. Compare evidence rather than assuming the guided run will be better.
6. Introduce a task that conflicts with an AGENTS rule; observe, then run tests and inspect the diff.

