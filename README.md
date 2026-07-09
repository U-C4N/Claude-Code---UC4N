# Claude Code - UC4N

> Extracted system-prompt fragments from every version of Claude Code — archived version by version, with the new changes written up as news.

Each version lives in its own folder (`Claude_Code_vX.Y.ZZZ/`). The numbered `.md` files inside represent separate sections of the prompt (identity strings, agent prompts, tool descriptions, output styles, etc.).

> **Methodology note:** Fragments are extracted from the `claude.exe` binary. Numeric prefixes can be re-numbered between versions, so the same number does **not** mean the same section — match sections by title/content. Also, extraction can sometimes leak binary string-table garbage into files (MIME lists, HTML-entity tables, symbol names), so a larger file size doesn't always mean more real content.

---

## Versions

| Version | Folder | Sections |
|---|---|---|
| v2.1.187 | `Claude_Code_v2.1.187/` | 33 |
| v2.1.195 | `Claude_Code_v2.1.195/` | 26 |
| v2.1.199 | `Claude_Code_v2.1.199/` | 27 |
| v2.1.201 | `Claude_Code_v2.1.201/` | 26 |
| v2.1.205 | `Claude_Code_v2.1.205/` | 54 |

---

## Changelog: v2.1.201 → v2.1.205

> 4-version jump. **28 new sections** extracted. Major expansion in autonomous mode, new tool categories (MCP, skills, hooks, cron, web fetch), new agent identities (Agent SDK), and new guidance sections (plan vs memory, sandbox failures, commit/PR workflow, scratchpad directory).

### 🆕 Added (28 new sections)

- **Agent identity expansion: `agents_sdk`, `default_agent_prompt`, `capability_statement`, `interactive_agent_intro`** — Identity now split into four variants: CLI identity, Agent SDK identity, subagent default prompt, and interactive-mode intro. "You are highly capable" capability statement added as standalone section.
- **`autonomous_loop_tick`** — New **dynamic pacing** section for autonomous loop. Separate from main autonomous_loop content.
- **Auto-mode trifecta: `auto_mode_classifier`, `auto_mode_classifier_intro`, `auto_mode_process`** — Classifier now has its own standalone prompt, an intro/denial explanation, AND a classification review process section.
- **Git/GitHub workflow: `commit_messages_pr`, `creating_pull_requests`, `git_workflow`** — Commit message format, PR creation guidelines, and general git workflow extracted as separate sections.
- **Plan mode expansion: `plan_agent_specialist`, `plan_artifact_tool`, `plan_mode_instructions`, `plan_rejected_detail`, `plan_tool`, `plan_vs_memory`, `todo_list_usage`, `custom_workflow_body`** — Plan mode now has specialist agent prompts, artifact publishing, memory vs plan guidance, todo-list usage rules, and custom workflow body override.
- **Hook system: `hooks`, `hook_condition`, `stop_condition`** — Full hook event table (PostToolUse, etc.), condition evaluation prompt, and stop-condition verification prompt.
- **MCP & Skills: `mcp`, `skills`, `knowledge_mcp_search`** — MCP resource listing, skills delegation prompt, and MCP search strategy guidance.
- **Web fetch: `web_fetch`, `web_fetch_tool`** — Web fetch tool description + IMPORTANT usage notes (HTTPS upgrade, redirect handling).
- **Chrome integration: `chrome_browser_important`, `claude_in_chrome`** — Chrome browser IMPORTANT usage note + Claude in Chrome extension integration.
- **Sandbox: `sandbox_failure`** — Sandbox failure detection and recovery guidance.
- **Context & memory: `injected_context_notice`, `memory_selection`, `scratchpad_directory`, `todo_reminder`** — Context injection notice, memory selection prompt, scratchpad directory convention, and todo reminder (returned from v2.1.199).
- **Tools: `advisor_tool`, `send_message_tool`, `statusline_agent`, `tool_denial_user`** — Advisor tool description, SendMessage tool, statusline agent, and user-refusal handling.
- **`team_communication`** — Agent teammate communication section (extracted from `team_comm`).

### ✳️ Expanded / matured

- **`cyber_risk`** — Now includes Fable 5 / Mythos 5 identity paragraph and model tier description with link to anthropic.com/news.
- **`autonomous_loop`** — Clean extraction with full autonomous stewardship, PR maintenance, repeated invocation, and "spirit of the task" guidance.
- **`blast_radius`** — Full reversibility policy with destructive/hard-to-reverse/shared-state action examples.
- **`git_operations`** — Full git workflow with commit steps, parallel tool calls, and PR workflow.

### 🔧 Renamed / restructured

- `identity_cli` + `identity_sdk` + `identity_agent` → `agents_sdk` + `default_agent_prompt` + `interactive_agent_intro`
- `simple_mode_intro` → `interactive_agent_intro` (merged with system_harness)
- `team_comm` → `team_communication`
- `plan_mode_guard` → `plan_rejected`
- `chrome_browser` → `chrome_browser_important`
- `coordinator`, `explore_agent`, `session_title`, `fable_unavailable`, `output_style_proactive`, `compact_service`, `context_management`, `exit_plan_mode`, `policy_spec`, `claude_md_override` — content matches v2.1.201, extraction format differences only.

### ➖ Changed / merged

- `system_harness` — merged into `interactive_agent_intro`
- `fable5_description` — merged into `cyber_risk` (same binary chunk)
- `tool_denial_guidance` — split into `tool_denial_guidance` + `tool_denial_user`
- `todo_reminder` — **returned** (was dropped in v2.1.201, confirmed real in v2.1.205)
- `plan_agent` — **returned** (was dropped after v2.1.187)
- `memory_selection` — **returned** (was dropped after v2.1.187)
- `statusline_agent` — **returned** (was dropped after v2.1.195)
- `auto_mode_classifier_intro` — **returned** (was not extracted since v2.1.195)

---

## Changelog: v2.1.187 → v2.1.195

> Only **verified / meaningful** prompt changes are listed below. Most of the large byte increases in the v2.1.195 extraction (verification_agent 30 KB, auto_mode_classifier 28 KB, identity/fable 15 KB, todo_reminder, statusline) are extraction noise, not real prompt text, and have been filtered out.

### 🆕 Added

- **`34_autonomous_loop` — Autonomous / timer-invoked triggering.** New fragment: *"You're being invoked on a timer while…"* Claude Code can now **invoke itself on a timer, without user interaction**. Lines up with scheduled cloud agents / routines and continuous agent-loop behavior.
- **`35_agent_sdk_identity` — Claude Agent SDK identity.** New identity fragment: *"running within the Claude Agent SDK."* Signals an official SDK-embedded variant of Claude Code.
- **New identity strings** (inside `identity_strings`): in addition to the single line,
  - *"You are Claude Code, Anthropic's official CLI for Claude, **running within the Claude Agent SDK**."*
  - *"You are a **Claude agent, built on Anthropic's Claude Agent SDK**."*
- **`04_doing_tasks_section` — "Reversibility & blast radius" safety policy.** This section was **empty** in the previous version; now it's populated: for actions that are hard to reverse or affect shared systems (git push, deleting branches, sending messages), **ask the user first by default**; a one-time approval doesn't count as standing approval.
- **New model strings** (inside `claude_fable_unavailable`): real model labels are now visible — *"Fable 5, Opus 4.7+"*, *"Fable 5, Opus 4.6+, Sonnet 4.6"* — plus a *"Use sparingly for the hardest tasks"* (excessive tokens / overthinking) warning.

### ✳️ Expanded / matured

- **`14_auto_mode_critique`** — grew from a single sentence into a **4-point structured rubric**: **Clarity**, **Completeness**, **Conflicts**, **Actionability**. Reviews user-written allow/deny rules far more systematically.

### ➖ Not present in this extraction

> The entire v2.1.195 folder was searched for the distinctive sentences of these sections; none had moved to another file. Whether this is an extraction-scope difference or a genuine removal can't be confirmed from this data alone.

- `17_output_style_learning` (Learning output style)
- `26_plan_agent` (read-only planning specialist prompt)
- `31_memory_selection` (memory selector prompt)
- `32_github_issue_title` (GitHub issue title generator)
- `33_team_coordination` (team/teammate prompt)
- `09_agent_env_notes`, `30_builtin_agents` — no longer separate files (chrome content lives on in `21_chrome_browser_automation`)
- `06_tone_conciseness`, `25_js_prompt_assemblies` — were already empty/placeholders; not a real loss

### 🔧 Minor / formatting

- `01_cyber_risk`, `03_system_harness`, `05_executing_actions`, `07_git_operations`, `10_explore_agent`, `19_session_title`, `21_chrome_browser_automation`, `24_tool_prompts`, `28_context_management`: only a few dozen bytes of difference — no meaningful content change.
- `08_default_agent_prompt`, `12_coordinator_system_prompt` (§2), `02_simple_mode_intro`: the v2.1.195 extraction is cut off mid-sentence; read this as an **extraction truncation**, not a content removal.

---

## ⭐ Highlights

1. **Claude Agent SDK identity arrived** — Claude Code now also positions itself as "running within the Agent SDK" / "a Claude agent built on the Agent SDK."
2. **Autonomous / timer-invoked loop** (`34_autonomous_loop`) — periodic self-invocation without a user.
3. **New "reversibility & blast radius" policy** — ask before destructive actions by default.
4. **New model tier: Fable 5** (Opus 4.7+ / Opus 4.6+ + Sonnet 4.6), with an excessive-token warning.
5. **Auto-mode rule critique matured** — into a 4-dimension evaluation rubric.

---

## Changelog: v2.1.195 → v2.1.199

> Extraction format changed from numbered `.md` to descriptive `.txt` filenames. Section count increased to 27 (new sections extracted, some merged).

### 🆕 Added / newly extracted

- **`auto_critique`** — Auto-mode rule critique logic extracted as standalone section
- **`blast_radius`** — "Reversibility & blast radius" safety policy (was `04_doing_tasks_section` in v2.1.195, now independent)
- **`claude_md_override`** — CLAUDE.md / project instructions override mechanism
- **`exit_plan_mode`** — Plan mode exit tool description
- **`policy_spec`** — `<policy_spec>` Bash command prefix detection rules
- **`tool_denial_guidance`** — Tool denial recovery guidance

### ✳️ Expanded

- **`coordinator`** — Now includes full §2 tools, §3 workers, §4 workflow, §5 concurrency, §6 verification sections
- **`autonomous_loop`** — Fuller extraction with timer invocation and repeated invocation sections
- **`explore_agent`** — Longer extraction with tool descriptions

### 🔧 Renamed / restructured

- `01_cyber_risk_instruction` → `cyber_risk`
- `02_simple_mode_intro` → `simple_mode_intro`
- `03_system_harness_section` → `system_harness`
- `07_git_operations` → `git_operations`
- `10_explore_agent` → `explore_agent`
- `12_coordinator_system_prompt` → `coordinator`
- `14_auto_mode_critique` → `auto_critique`
- `19_session_title` → `session_title`
- `20_todo_reminder` → `todo_reminder`
- `21_chrome_browser_automation` → `chrome_browser`
- `22_identity_strings` → split into `identity_cli`, `identity_sdk`, `identity_agent`
- `23_claude_fable_unavailable` → `fable_unavailable` + `fable5_description`
- `24_tool_prompts` → absorbed into individual agent files
- `28_context_management` → `context_management`
- `29_plan_mode_guard` → `plan_mode_guard`
- `34_autonomous_loop` → `autonomous_loop`
- `35_agent_sdk_identity` → absorbed into `identity_sdk`

### ➖ Not present

- `06_tone_conciseness`, `09_agent_env_notes`, `11_verification_agent`, `13_auto_mode_classifier_intro`, `15_output_style_proactive`, `16_output_style_explanatory`, `17_output_style_learning`, `18_compact_service`, `25_js_prompt_assemblies`, `26_plan_agent`, `27_statusline_agent`, `30_builtin_agents`, `31_memory_selection`, `32_github_issue_title`, `33_team_coordination` — extraction scope differences or content merges

---

## Changelog: v2.1.199 → v2.1.201

> Patch-level bump (2 versions). Most sections are identical or near-identical. Key meaningful changes below.

### 🆕 Added

- **`autonomous_loop` — Major expansion.** Now includes new guidance on broader scope: *"following through on the spirit of the task they gave you, not just its literal scope"*, persistence (*"Only stop if the original task is provably complete or the user said to stop"*), and browser notification rules (*"Keep the message under 200 characters, one line, no markdown. Lead with what they'd act on"*). The "Repeated invocations" section was rewritten to bias toward broader scope exploration before quitting.

### ✳️ Expanded / matured

- **`simple_mode_intro`** — Rewritten intro text; now starts with *"You work alongside the user on software engineering tasks"* instead of the previous identity-first format
- **`plan_mode_guard`** — Wording changed around what tools are allowed in plan mode; exception clause expanded

### 🔧 Minor / formatting

- **`blast_radius`**, **`cyber_risk`**, **`fable5_description`** — Extraction format differences, core content unchanged
- Remaining sections show byte-level differences consistent with extraction noise rather than content changes

### ➖ Dropped

- **`todo_reminder`** — Not found in v2.1.201 extraction (was HTML entity false-positive in v2.1.199)

---

<div align="center">

### U-C4N

[![X](https://img.shields.io/badge/%F0%9D%95%8F-@UEdizaslan-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/UEdizaslan)

</div>
