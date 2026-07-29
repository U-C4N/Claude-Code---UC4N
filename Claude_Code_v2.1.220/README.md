# Claude Code v2.1.220 — System Prompt Extraction

```
     ▄████████  ▄████████    ▄█    █▄       ▄████████    ▄█    █▄    
    ███    ███ ███    ███   ███    ███     ███    ███   ███    ███   
    ███    █▀  ███    ███   ███    ███     ███    ███   ███    ███   
    ███        ███    ███  ▄███▄▄▄▄███▄▄  ▄███▄▄▄▄██▀  ▄███▄▄▄▄███▄▄ 
    ███      ▀███████████ ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀▀▀   ▀▀███▀▀▀▀███▀ 
    ███    █▄  ███    ███   ███    ███     ███    ███   ███    ███   
    ███    ███ ███    ███   ███    ███     ███    ███   ███    ███   
    ████████▀  ███    █▀    ███    █▀      ██████████   ███    █▀    
                                                                     
      ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗                
     ██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝                
     ██║     ██║     ███████║██║   ██║██║  ██║█████╗                  
     ██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝                  
     ╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗                
      ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝                
                                                                      
           ██████╗ ██████╗ ██████╗ ███████╗                           
          ██╔════╝██╔═══██╗██╔══██╗██╔════╝                           
          ██║     ██║   ██║██║  ██║█████╗                             
          ██║     ██║   ██║██║  ██║██╔══╝                             
          ╚██████╗╚██████╔╝██████╔╝███████╗                           
           ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝                           
                                                                      
                ██╗   ██╗██████╗  █████╗ ██╗   ██╗                   
                ██║   ██║╚════██╗██╔══██╗████╗  ██║                   
                ██║   ██║ █████╔╝╚██████║██╔██╗ ██║                   
                ██║   ██║ ╚═══██╗██╔══██║██║╚██╗██║                   
                ╚██████╔╝██████╔╝██║  ██║██║ ╚████║                   
                 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝                   
```

---

**Extraction Date:** 2026-07-27  
**Binary:** `claude.exe` v2.1.220 — **265,720,480 bytes** (253 MB)  
**Source:** `%APPDATA%\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe`  
**Previous Extraction:** v2.1.216  

---

## 📊 Quick Stats

| Metric | v2.1.216 | v2.1.220 | Δ |
|---|---|---|---|
| Binary size | 258 MB | 253 MB | -5 MB (-1.9%) |
| Sections | 53 | 64 | +11 |
| Total strings extracted | 217,961 | 224,458 | +6,497 |
| Raw strings dump | 40.1 MB | — | — |

---

## 🔥 What's New / Changed

### 🆕 New Sections (11 added)

| File | Size | Description |
|---|---|---|
| `managed_agents_ruby.txt` | 102.0 KB | Managed Agents Ruby SDK — event/repl bindings documentation |
| `managed_agents_events.txt` | 80.5 KB | Managed Agents Events & Steering — event system documentation |
| `typescript_api_guide.txt` | 32.4 KB | Claude API TypeScript guide — full SDK reference embedded |
| `available_tools_guidance.txt` | 13.3 KB | "Check this list before writing" — tool selection guidance |
| `advisor_tool_prompt.txt` | 9.8 KB | Advisor tool (stronger reviewer model) full prompt |
| `plan_mode_reminder.txt` | 7.9 KB | "REMEMBER: You can ONLY explore and plan" — stricter plan mode enforcement |
| `browser_guidelines.txt` | 7.4 KB | Browser automation tool usage guidelines |
| `mcp_tab_group_tool.txt` | 7.3 KB | MCP tab group management tool description |
| `continue_session_prompt.txt` | 6.3 KB | Session continuation prompt — restricts tool usage during resume |
| `claude_md_structure.txt` | 4.9 KB | CLAUDE.md structure definition for custom workflows |
| `screenshot_tool_prompt.txt` | 4.1 KB | Screenshot tool (claude-in-chrome) description |

### 🚀 Major Rewrites

**`context_management.txt` — +277.4%**
> 9.8 KB → 37.0 KB

Massive expansion. Now includes full background job session management, multi-session context windowing, and detailed compact/pre-compact orchestration flow. Refactored around "compact service" architecture.

**`web_fetch.txt` — +246.8%**
> 4.0 KB → 13.8 KB

Extended web fetch tool documentation with content extraction pipeline, readability processing, and URL resolution rules.

**`agents_sdk.txt` — +207.1%**
> 4.5 KB → 13.7 KB

SDK agent identity expanded with detailed capability descriptions and sub-agent coordination.

**`default_agent_prompt.txt` — +201.6%**
> 4.5 KB → 13.7 KB

Default agent prompt restructured with richer tool-specific descriptions and behavioral rules.

**`autonomous_loop.txt` — +125.8%**
> 7.6 KB → 17.2 KB

Extended autonomous loop with:
- Revised escalation logic: 3 consecutive "nothing to do" → scale back
- Enhanced PR maintenance workflow (check CI → diagnose flaky vs real failures → resolve threads via GraphQL → rebase before push)
- Detailed reversibility framework with explicit examples

**`blast_radius.txt` — +38.5%**
> 15.8 KB → 21.8 KB

System harness reorganized with new sections on execution context awareness and expanded tone/style rules.

### 🗑️ Removed
None — all 53 sections from v2.1.216 carried forward.

### ➕ Significant Growth

| File | v2.1.216 | v2.1.220 | Δ |
|---|---|---|---|
| `memory_selection.txt` | 1.3 KB | 8.0 KB | +512.8% |
| `tool_denial_user.txt` | 1.9 KB | 8.3 KB | +343.4% |
| `exit_plan_mode.txt` | 1.0 KB | 4.1 KB | +329.7% |
| `hook_condition.txt` | 0.4 KB | 1.5 KB | +281.0% |
| `injected_context_notice.txt` | 0.3 KB | 1.2 KB | +267.4% |
| `commit_messages_pr.txt` | 0.7 KB | 2.2 KB | +205.1% |
| `send_message_tool.txt` | 0.2 KB | 0.6 KB | +198.2% |
| `mcp.txt` | 4.0 KB | 11.4 KB | +183.6% |
| `compact_service.txt` | 3.7 KB | 10.1 KB | +170.9% |
| `plan_rejected_detail.txt` | 2.6 KB | 7.0 KB | +167.1% |
| `plan_rejected.txt` | 3.0 KB | 8.0 KB | +166.1% |
| `sandbox_failure.txt` | 3.1 KB | 8.0 KB | +157.7% |
| `session_title.txt` | 2.2 KB | 5.6 KB | +154.4% |
| `auto_mode_classifier_intro.txt` | 2.8 KB | 7.0 KB | +152.6% |
| `statusline_agent.txt` | 7.1 KB | 15.9 KB | +124.7% |
| `explore_agent.txt` | 2.4 KB | 5.2 KB | +118.8% |
| `plan_agent_specialist.txt` | 2.4 KB | 5.1 KB | +109.3% |

### ➖ Shrinkage

| File | v2.1.216 | v2.1.220 | Δ |
|---|---|---|---|
| `git_operations.txt` | 2.1 KB | 0.3 KB | -84.5% |
| `git_workflow.txt` | 1.3 KB | 0.3 KB | -75.5% |
| `auto_mode_process.txt` | 1.5 KB | 0.7 KB | -55.8% |
| `claude_md_override.txt` | 4.0 KB | 2.5 KB | -35.9% |
| `claude_in_chrome.txt` | 0.6 KB | 0.4 KB | -32.2% |
| `output_style_proactive.txt` | 1.6 KB | 1.3 KB | -14.8% |

Git sections trimmed significantly — likely consolidated into other prompt areas.

---

## 📁 Complete File Index (64 sections)

### 🔑 Identity & Core (82-84 MB cluster)
| File | Size | Description |
|---|---|---|
| `agents_sdk.txt` | 13.7 KB | "You are a Claude agent, built on Anthropic's Claude Agent SDK" |
| `default_agent_prompt.txt` | 13.7 KB | Default agent identity + tool descriptions |
| `interactive_agent_intro.txt` | 6.9 KB | "You work alongside the user..." |
| `capability_statement.txt` | 6.6 KB | Software engineering task framing |
| `claude_md_override.txt` | 2.5 KB | CLAUDE.md rule override behavior |
| `session_title.txt` | 5.6 KB | Session title + git branch name generator |
| `injected_context_notice.txt` | 1.2 KB | Context injection notice text |
| `claude_md_structure.txt` | 4.9 KB | CLAUDE.md structure definition (NEW) |
| `continue_session_prompt.txt` | 6.3 KB | Session continuation tool restriction (NEW) |

### 🛡️ Safety & Policy (82-84 MB cluster)
| File | Size | Description |
|---|---|---|
| `cyber_risk.txt` | 2.7 KB | Authorized security testing policy |
| `policy_spec.txt` | 4.9 KB | Bash command prefix detection |
| `tool_denial_guidance.txt` | 7.0 KB | Tool denial response guidance |
| `tool_denial_user.txt` | 8.3 KB | User-facing tool denial messages |
| `sandbox_failure.txt` | 8.0 KB | Sandbox error/warning templates |
| `memory_selection.txt` | 8.0 KB | Memory selection rules |
| `hook_condition.txt` | 1.5 KB | Hook condition guard |

### 🤖 Agent System (82-242 MB)
| File | Size | Description |
|---|---|---|
| `autonomous_loop.txt` | 17.2 KB | Timer-invoked autonomous operation |
| `autonomous_loop_tick.txt` | 1.0 KB | Single autonomous tick prompt |
| `blast_radius.txt` | 21.8 KB | Full system harness: System + Language + Output + Tools + Tone + Care |
| `context_management.txt` | 37.0 KB | Auto-compact and context limit handling |
| `compact_service.txt` | 10.1 KB | Compact/reactive-compact service prompt |
| `exit_plan_mode.txt` | 4.1 KB | Exit plan mode instructions |
| `plan_mode_reminder.txt` | 7.9 KB | "REMEMBER: You can ONLY explore and plan" (NEW) |
| `advisor_tool_prompt.txt` | 9.8 KB | Advisor tool (stronger model) prompt (NEW) |

### 🎯 Plan Mode (82-131 MB)
| File | Size | Description |
|---|---|---|
| `plan_mode_instructions.txt` | 5.4 KB | "Plan mode is active. You MUST NOT make edits..." |
| `plan_rejected.txt` | 8.0 KB | Plan rejected response |
| `plan_rejected_detail.txt` | 7.0 KB | Detailed plan rejection |
| `plan_agent.txt` | 5.3 KB | Plan mode agent behavior |
| `plan_agent_specialist.txt` | 5.1 KB | Plan specialist subagent |
| `plan_tool.txt` | 3.7 KB | Plan tool usage guide |
| `plan_artifact_tool.txt` | 0.6 KB | Plan artifact tool |
| `plan_vs_memory.txt` | 5.5 KB | Plan vs memory distinction |

### 🔧 Tools & MCP (82-174 MB)
| File | Size | Description |
|---|---|---|
| `mcp.txt` | 11.4 KB | MCP server instructions |
| `knowledge_mcp_search.txt` | 1.4 KB | Knowledge MCP search tool |
| `web_fetch.txt` | 13.8 KB | Web fetch tool + content processing |
| `web_fetch_tool.txt` | 1.6 KB | Web fetch tool behavior |
| `chrome_browser_important.txt` | 6.4 KB | Chrome browser automation |
| `claude_in_chrome.txt` | 0.4 KB | Claude-in-Chrome specific |
| `screenshot_tool_prompt.txt` | 4.1 KB | Screenshot tool description (NEW) |
| `browser_guidelines.txt` | 7.4 KB | Browser tool usage guidelines (NEW) |
| `skills.txt` | 1.3 KB | Skills tool usage |
| `hooks.txt` | 2.9 KB | Hook system integration |
| `advisor_tool.txt` | 4.4 KB | Advisor tool specification |
| `scratchpad_directory.txt` | 27.7 KB | Scratchpad directory management |
| `custom_workflow_body.txt` | 9.9 KB | Custom workflow body prompt |
| `available_tools_guidance.txt` | 13.3 KB | "Check this list before writing" (NEW) |
| `mcp_tab_group_tool.txt` | 7.3 KB | MCP tab group tool (NEW) |

### 🔀 Git & PR (109-125 MB)
| File | Size | Description |
|---|---|---|
| `git_operations.txt` | 0.3 KB | Git command rules and restrictions |
| `git_workflow.txt` | 0.3 KB | Git workflow patterns |
| `commit_messages_pr.txt` | 2.2 KB | Commit message + PR conventions |

### 🤝 Communication & Output (83-215 MB)
| File | Size | Description |
|---|---|---|
| `team_communication.txt` | 3.8 KB | SendMessage / team communication |
| `send_message_tool.txt` | 0.6 KB | SendMessage tool brief |
| `output_style_proactive.txt` | 1.3 KB | Proactive output style |
| `statusline_agent.txt` | 15.9 KB | Agent status line format |
| `stop_condition.txt` | 1.4 KB | Stop condition rules |

### 📋 Task Management (83-122 MB)
| File | Size | Description |
|---|---|---|
| `todo_list_usage.txt` | 4.5 KB | Todo list usage rules |
| `todo_reminder.txt` | 3.8 KB | Todo reminder triggers |
| `auto_mode_classifier.txt` | 2.7 KB | Auto mode classifier rules |
| `auto_mode_classifier_intro.txt` | 7.0 KB | Classifier intro prompt |
| `auto_mode_process.txt` | 0.7 KB | Auto mode process flow |
| `explore_agent.txt` | 5.2 KB | Explore agent definition |

### 📚 Embedded Documentation (NEW — 245-257 MB)
| File | Size | Description |
|---|---|---|
| `managed_agents_ruby.txt` | 102.0 KB | Managed Agents Ruby SDK full README |
| `managed_agents_events.txt` | 80.5 KB | Managed Agents Events & Steering docs |
| `typescript_api_guide.txt` | 32.4 KB | Claude API TypeScript SDK guide |

---

## 🗺️ Binary Offset Map

```
 58 MB  ██ claude_md_override
        |
 82 MB  ████████████████████████████████████████████████████████
        █ IDENTITY + SAFETY CLUSTER (82-84 MB)                  █
        █ agents_sdk, default_agent, interative_intro,          █
        █ cyber_risk, policy_spec, plan_mode_*, team_comm,      █
        █ chrome_browser, memory, tool_denial, web_fetch,       █
        █ mcp, hooks, session_title, claude_md_override,        █
        █ advisor_tool, exit_plan_mode, plan_rejected, todo_*,  █
        █ continue_session, claude_md_structure                  █
 84 MB  ████████████████████████████████████████████████████████
        |
 85 MB  ██ auto_mode_classifier
 90 MB  ██ statusline_agent
 94 MB  ██ plan_vs_memory
 97 MB  ██ web_fetch_tool
 99 MB  ██ autonomous_loop_tick
100 MB  ██ skills
103 MB  ██ explore_agent
105 MB  ██ plan_agent_specialist
108 MB  ██ screenshot_tool_prompt
109 MB  ██ commit_messages_pr, git_workflow, sandbox_failure
110 MB  ██ plan_tool
111 MB  ██ output_scroll
114 MB  ██ send_message_tool, todo_list_usage
118 MB  ██ git_operations
121 MB  ██ capability_statement, injected_context_notice, stop_condition
124 MB  ██ plan_agent, plan_mode_instructions
131 MB  ██ hook_condition
134 MB  ██ claude_in_chrome
154 MB  ██ custom_workflow_body
174 MB  ██ mcp_tab_group_tool
186 MB  ██ compact_service
205 MB  ██ output_style_proactive
        |
225 MB  ████████████████████████████████████████████████████████
        █ LARGE PROMPT CLUSTER (225-249 MB)                     █
        █ autonomous_loop, blast_radius, context_management,    █
        █ plan_mode_reminder, advisor_tool_prompt,              █
        █ available_tools_guidance, browser_guidelines          █
249 MB  ████████████████████████████████████████████████████████
        |
245 MB  ██ scratchpad_directory, continue_session_prompt
        |
256 MB  ████████████████████████████████████████████████████████
        █ EMBEDDED DOCS (256-257 MB)                            █
        █ managed_agents_ruby, managed_agents_events,           █
        █ typescript_api_guide                                  █
257 MB  ████████████████████████████████████████████████████████
```

---

## 🔬 Extraction Method

1. **String dump** — Python chunked reader extracts 224,458 ASCII/UTF-8 sequences (≥30 chars) from 265 MB binary → `_all_strings.txt`
2. **Marker matching** — Each v2.1.216 section's first meaningful line searched against the string dump to locate offset
3. **Radius extraction** — ±5-15 KB around each marker extracted to individual `.txt` files
4. **Novelty scan** — Uncovered prompt-like strings ≥150 chars scanned for new sections not present in v2.1.216, using prompt markers, alpha ratio filtering, and JS noise rejection
5. **Quality** — Files contain **raw strings**; prompt text is embedded within minified JS/config fragments. Large standalone sections (blast_radius, context_management, autonomous_loop) are near-clean. Dense cluster sections (82-84 MB, 256-257 MB docs) contain JS noise proportional to cluster density.

---

## 📦 Raw Artifacts

| File | Size | Description |
|---|---|---|
| `_all_strings.txt` | ~44 MB | Full string extraction (224,458 entries with offsets) |
| `*.txt` (64 files) | ~600 KB | Individual prompt sections |

---

*U-C4N Extraction — 2026-07-27*
