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

<div align="center">

### U-C4N

[![X](https://img.shields.io/badge/%F0%9D%95%8F-@UEdizaslan-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/UEdizaslan)

𝕏 [@UEdizaslan](https://x.com/UEdizaslan)

</div>
