---
name: programmer-requirement
description: Analyze a legacy desktop business application and plan small, reliable code changes across its UI, business logic, and database dependencies. Use for maintenance or feature requests in such applications; require explicit approval before editing code.

---

# Programmer Requirement

1. Inspect the relevant application files and documentation. Trace the requested behavior from UI events and screens through business rules to database queries, tables, or stored procedures. Distinguish observed dependencies from assumptions.
2. State the current behavior, requested behavior, affected components, and any missing requirements. Identify security risks (such as input handling, authorization, and sensitive data exposure) and compatibility risks (such as supported runtime, existing interfaces, and database schema). Report only risks supported by the inspected code or task context.
3. Propose the smallest practical change. Describe short, single-purpose functions with clear inputs, outputs, and error handling, plus focused checks for the affected behavior. Do not claim a function works until it has been verified.
4. Before editing any application code, tests, configuration, or database scripts, show the specific files and proposed changes and ask the user for explicit approval. Skill invocation or a general request to implement is not approval for this step. If approval is withheld, stop before code edits and provide the analysis and plan.
5. After approval, make only the approved changes. Run the project's existing verification commands when available, inspect the diff, and report results and remaining risks. If no verification command is documented, say so rather than inventing one.
