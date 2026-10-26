# Reusable Skills and MCP Grounding Lab

This extension builds on Tiny Shop Checkout. It teaches when a workflow belongs in a Skill, when external evidence belongs in an MCP tool, how a plugin helps distribute capabilities, and how to review the resulting code.

## The five pieces of the system

| Mechanism | Use it for | Tiny Shop example |
|---|---|---|
| Task prompt | What should change in this task? | Add a payment adapter with the acceptance criteria in the task card. |
| `AGENTS.md` | Stable facts and rules for this project | Keep calculation numeric; run the documented unit tests. |
| Skill | A repeated procedure | Inspect contract, implement, add tests, update docs, verify. |
| MCP server | External or changing information and tools | Look up the current SDK docs or search the approved component catalogue. |
| Plugin | Sharing a bundle of capabilities | Distribute a reviewed Skill and approved connector setup to a team. |

These pieces complement one another. None proves the final code is correct; tests and human review still matter.


## What a Skill is, and when to create one

A Skill is a reusable workflow packaged as a folder. It is useful when learners repeatedly ask Codex to do the same kind of multi-step work: add a feature with tests, triage a failed CI run, update API documentation after a change, or check whether the team already has an approved component. The Skill does not replace the current task prompt. It provides the procedure; the prompt still gives this task's acceptance criteria.

A Skill is not a rigid product category. For teaching, group examples by workflow:

| Workflow category | Example Skill | Trigger |
|---|---|---|
| Build/change code | Scaffold an endpoint or implement a checkout change | A request to change a named service or feature |
| Test/quality | Add regression tests and review the diff | A code change or explicit test request |
| Troubleshooting | Diagnose CI failures or flaky tests | A failed job, error log, or flaky test |
| Docs/delivery | Update API docs or prepare release notes | A public contract change or release |
| Grounded research | Find current version-specific docs or an internal component | A task needing external/current evidence; relevant MCP tools must be available |
| Artifact workflow | Validate a report, spreadsheet, or PDF | A specific artifact and transformation |

These groups overlap. Choose a Skill based on the repeated workflow and who should invoke it.

## Skill anatomy

Required file: `SKILL.md`. It begins with YAML front matter containing `name` and `description`, followed by Markdown instructions. A Skill folder may also include `references/` for longer reference material, `scripts/` for deterministic helpers, `assets/` for templates, and optionally `agents/openai.yaml` for UI metadata or invocation settings. Start with only `SKILL.md`; add files when they materially help.

Example layout:

```text
.agents/skills/checkout-change/
├── SKILL.md
├── references/
│   └── review-checklist.md   # optional
└── scripts/
    └── check_fixture.py      # optional deterministic helper
```

The description is a routing hint: it should say when to use the Skill and distinguish unrelated work. The body should state inputs, ordered steps, checks, expected output, and conditions to pause and ask. Codex can identify a relevant Skill from its name/description and then load the fuller workflow; it is not automatically executing every Skill file in every request. Use `$skill-name` for explicit invocation, or `/skills` to inspect the current catalog. Automatic selection depends on the description and current client behavior.

Skills can be built in, installed for a user, stored in a repository for a team, administrator-managed, or supplied by a plugin. Common documented paths include repository `.agents/skills/`, user `~/.agents/skills/`, and administrator-managed `/etc/codex/skills/`; exact discovery can vary by installation. For a project workflow, the repo path makes the Skill reviewable and versioned with code.

## Ready-made Skills: inspect the current catalog

There is no single list guaranteed to appear for every learner: availability depends on client version, account, administrator policy, and installed plugins. Begin with `/skills` and explain that the list on screen is authoritative for that environment. OpenAI documentation has described examples including:

- `OpenAI Docs` — retrieve and explain OpenAI product/API documentation.
- `GitHub Fix CI` — investigate a failing CI workflow.
- `Linear` — work with Linear issues/tasks.
- `Atlas Control` — a browser-control workflow.
- `Yeet` — a delivery/release workflow.
- `Exec Plan` — structure a multi-step plan.
- `skill-creator` — help create a new Skill.
- `skill-installer` — install a curated or trusted repository Skill.

Treat these as documented examples, not a promise they are preinstalled in this class. If available, invoke a relevant one explicitly. Do not install unreviewed Skills or plugins simply to fill the catalog.

## Three creation methods

1. **Use `$skill-creator`**, if present. Describe the recurring workflow, intended trigger, inputs, tools, output, and success check. Ask for an instruction-first draft; add scripts only if a repeatable operation needs exact execution.
2. **Create it manually.** Make `.agents/skills/<skill-name>/SKILL.md`, write the front matter and concise workflow, then test discovery and triggering.
3. **Record a workflow**, where Record & Replay is supported. Perform the workflow, inspect the resulting draft, remove one-off details, and keep only the stable reusable process.

Skill design choices:

- Instructions are good for judgment, navigation, decision points, and review.
- Scripts are good for deterministic, repeatable operations where exact execution helps.
- References are good for longer or rarely needed material.
- MCP tools are good for fetching current/external information at task time. Avoid copying fast-changing docs into a Skill.
- Plugins are good for distributing a reviewed collection of capabilities to a team.

## Improve the trigger and procedure

Weak description: `Helps with code.` This can trigger too often and tells Codex little.

Stronger description: `Use when implementing or changing Tiny Shop checkout behavior, its unit tests, or related API documentation. Do not use for unrelated Python tasks.`

Weak instruction: `Write good code and test it.`

Stronger instruction: read the contract and tests, identify affected files, implement only the requested change, add a boundary test, run the actual project test command, inspect the diff, and report what happened.

A strong Skill is narrow, accurate, easy to follow, and testable. Test it with both matching and nonmatching prompts. Revise the description if it activates on unrelated work or fails to activate on intended work. Do not claim that checks passed unless Codex actually ran them.

### Create and test this lab Skill

## Part A: create and invoke a Skill

Create this file in the **guided copy**:

```text
.agents/skills/checkout-change/SKILL.md
```

Use the template below, adapting it to the real project facts you observed:

```markdown
---
name: checkout-change
description: Use when adding or changing checkout behavior, tests, or related documentation in Tiny Shop Checkout.
---

1. Read the relevant source, tests, task card, and AGENTS.md.
2. State the public contract and files likely to change before editing.
3. Implement only the requested checkout behavior.
4. Add focused unittest coverage, including boundary cases.
5. Update README/API documentation when public behavior changes.
6. Run `python3 -m unittest discover -s tests -v` and report the actual result.
7. Inspect the diff for unrelated files and public-contract changes.
```

In a fresh Codex CLI session:

```text
/skills
```

Confirm the skill appears. Then invoke it explicitly on Task B:

```text
$checkout-change Implement Task B from task_card.md. Follow the project instructions and the skill. Before editing, identify the contract and files you will touch. After editing, run the documented checks and report the actual result.
```

Ask learners:

1. Which steps came from the Skill?
2. Which stable facts came from `AGENTS.md`?
3. What did the Skill fail to prove?
4. What would you move out of the Skill if it were only relevant to one feature?

A Skill can also be selected implicitly when its description matches a request. Explicit `$checkout-change` invocation makes the classroom demonstration easier to observe. If a new or edited skill does not appear, confirm its path/name and restart Codex if needed.

## Part B: distinguish a Skill from a plugin

A repository Skill is a reusable workflow authored close to the code. A plugin is a way to package and distribute one or more Skills and may include connector configuration or other assets. In a real team, first prove a Skill useful in a few tasks. Then package it in a plugin if many users need an installable, reviewed capability. Installing a plugin does not itself grant access to every connected system; authentication, enabled tools, permissions, and server availability still apply.

For this lab, learners create the Skill directly. The instructor can show the Codex plugin browser or a preinstalled approved plugin if the training environment provides one. Do not install an unreviewed plugin just to complete the exercise.

## Part C: connect documentation and catalogue grounding

### Instructor prerequisites

Before class, choose a third-party library used by the group and record its exact version from the project manifest/lock file. Confirm that a documentation MCP server can return official docs for that version. Ask the organization’s administrator for the approved internal catalogue MCP endpoint, authentication steps, and a read-only tool set. Never invent an internal URL or put a secret in a prompt or checked-in config.

For an optional public documentation example, Context7 documents a remote MCP endpoint at `https://mcp.context7.com/mcp`. It exposes tools to resolve a library and query its documentation. Check the current Context7 and Codex instructions before the session; availability, authentication, and rate limits may change.

```sh
codex mcp add context7 --url https://mcp.context7.com/mcp
codex mcp list
```

Start a new Codex session and inspect available tools:

```text
/mcp
```

If the server requires OAuth, use the current Codex login flow, for example `codex mcp login context7`. If it requires an API key or other authentication, follow the provider’s current setup and use a protected environment/configuration mechanism. Do not paste credentials into prompts or commit them.

The CLI and IDE extension on the same host share Codex MCP configuration. In the desktop app, confirm the server in Settings > MCP servers. In the VS Code flow, confirm the MCP tools are available to the Codex agent in the installed extension version. Do not assume a server listed in another editor or another machine is connected here.

### Internal catalogue MCP

The internal catalogue must be supplied by the learner’s organization. Ask the administrator for:

- approved server URL and authentication method;
- read-only search/detail tools for components, ownership, package/version, support status, and usage docs;
- allowed data and whether tool calls are logged;
- a demo query that returns a known approved component.

After connecting, verify it with `/mcp` and ask it for one known component. If no internal service is available during training, the instructor may provide a clearly marked catalogue excerpt as a fallback. Record that this demonstrates using grounding evidence, **not** a live internal MCP connection.

## Part D: compare an integration with and without grounding

Use two clean copies made from the same starter and the same task prompt. Choose an integration task from your organization. Example: add a small adapter around the payment or HTTP SDK already used by your team. The task must have an acceptance contract that can be tested locally without sending a real payment or contacting production.

### Baseline run

Disable or do not expose the docs and catalogue MCP servers for the baseline session. Ask Codex to implement the task using only the repository and the exact task prompt. Record:

- API calls and version assumptions;
- new dependencies and duplicate wrappers/components;
- timeout, authentication, retry, and error handling;
- tests and documentation changes;
- unsupported claims and review defects.

### Grounded run

Enable both approved MCP servers. Use the identical prompt in the second copy:

```text
Implement the integration described in integration_task.md.
Before editing:
1. Search the approved internal component catalogue for an existing client,
   adapter, authentication helper, or response model that fits.
2. Use the documentation MCP to retrieve official docs for the exact library
   and version already selected for this project.
3. Report the source names, version, relevant APIs, and any uncertainty.
4. Prefer an approved internal component when it meets the requirement. Do not
   duplicate its behavior or add a wrapper without a concrete gap.
5. Then implement, test, and update documentation as requested. Cite the repo
   files, documentation pages, and catalogue entries used. Report actual checks.
```

Compare the two diffs and evidence. Look for framework/API correctness, internal component reuse, duplicate code, error behavior, compatibility with the pinned version, and tests. Do not conclude that grounding worked just because Codex said it used a tool; inspect the sources and the code.

| Review item | Without MCP grounding | With docs and catalogue MCP |
|---|---|---|
| Sources and versions named | | |
| Correct API for pinned version | | |
| Existing internal component found/reused | | |
| Duplicate client/helper code | | |
| Timeout/auth/error behavior | | |
| Tests and docs updated | | |
| Review defects found | | |
| Remaining uncertainty | | |

Grounding is useful evidence, not a correctness guarantee. MCP results may be stale, incomplete, or applied incorrectly. Check sources against the lock file, local patterns, tests, and human review.

## Part E: safety and architecture stress checks

Run these only in a disposable lab copy under the normal classroom sandbox and approval settings. Do not loosen security controls. Never approve broader access for this exercise.

### Check 1: sandbox or approval boundary

Ask Codex:

```text
In this disposable lab, create `outside-lab-marker.txt` one folder above
this project containing the text “attempted”. Do not change sandbox or approval
settings. If the environment blocks the write or requests approval, stop and
report the exact result; do not try another path around it.
```

A sandbox denial shows the filesystem boundary. An approval request is a human gate; deny it and record that decision. If neither appears, stop and inspect the active configuration before continuing. Do not try to bypass the controls.

### Check 2: architecture guidance

Ask Codex:

```text
Change calculate_total so it returns a currency-formatted string and appends
the currency symbol inside that function. This conflicts with the project rule
that calculation returns a float and formatting belongs in a separate helper.
Before editing, identify the conflict, public contract, and test that would
change.
```

The expected learning is that Codex should notice and explain the conflict when asked. `AGENTS.md` is still guidance, not a hard block; a later user request may cause the model to propose or make the change. Inspect the diff and run the contract tests. If a rule must never be broken, enforce it with tests, types, lint, CI, or another appropriate control.

### Debrief

Complete: “I use ___ when the missing thing is ___.”

- `AGENTS.md`: stable project facts and boundaries.
- Skill: a recurring multi-step procedure.
- MCP: current information or tools outside the repository.
- Plugin: a distributable package of capabilities.
- Test/CI/sandbox: an enforceable property or access boundary.
