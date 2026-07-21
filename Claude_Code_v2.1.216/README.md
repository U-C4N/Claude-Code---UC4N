# Claude Code v2.1.216 — System Prompt Extraction

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
                                                                      
                ██╗   ██╗██████╗  █████╗ ███╗   ██╗                   
                ██║   ██║╚════██╗██╔══██╗████╗  ██║                   
                ██║   ██║ █████╔╝╚██████║██╔██╗ ██║                   
                ██║   ██║ ╚═══██╗██╔══██║██║╚██╗██║                   
                ╚██████╔╝██████╔╝██║  ██║██║ ╚████║                   
                 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝                   
```

---

**Extraction Date:** 2026-07-21  
**Binary:** `claude.exe` v2.1.216 — **258,288,288 bytes** (246 MB)  
**Source:** `%APPDATA%\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe`  
**Previous Extraction:** v2.1.205  

---

## 📊 Quick Stats

| Metric | v2.1.205 | v2.1.216 | Δ |
|---|---|---|---|
| Binary size | 247 MB | 258 MB | +11 MB (+4.5%) |
| Sections | 54 | 53 | -1 |
| Total strings extracted | — | 217,961 | — |
| Raw strings dump | — | 40.1 MB | — |

---

## 🔥 What's New / Changed

### Model Identity
```
Fable 5, Opus 4.6+, Sonnet 4.6+
```
Updated from v2.1.205's model references. Fable 5 is the new Mythos-class tier.

### 🚀 Autonomous Loop (`autonomous_loop.txt`) — **+57.7%**
> 4,946 → 7,801 chars

New escalation rule: **3 consecutive "nothing to do" → scale back to quick CI check, stop narrating.** More explicit reversibility guidance: reversible actions (edits, tests) = go ahead; irreversible (push, delete, send) = wait for user.

Detailed PR maintenance workflow added: check CI → diagnose flaky vs real failures → resolve review threads via GraphQL → rebase before pushing.

### 🛡️ Blast Radius (`blast_radius.txt`) — **+266%**
> 4,405 → 16,133 chars

Massive expansion. Now bundles the full system harness including:
- `# System` — context management, tool execution, prompt injection flags
- `# Language` — multilingual output with diacritical correctness requirements
- `# Output Style` — configurable output modes
- `# Using your tools` — parallel tool call optimization, subagent guidance
- `# Tone and style` — no emojis, short responses, file:line references
- `# Executing actions with care` — concrete risky action examples:
  - Destructive: `rm -rf`, dropping tables, killing processes
  - Hard-to-reverse: force-push, `git reset --hard`, CI/CD changes
  - Visible to others: pushing, PRs, Slack, email
  - Git safety: `git status` before destructive commands, stash untracked work

### 🔄 Context Management (`context_management.txt`) — **-58.6%**
> 24,201 → 10,026 chars

Restructured. Now references background job sessions. Compact/pre-compact flow reorganized.

### 🗑️ Removed
- **`creating_pull_requests.txt`** — Pull request creation instructions removed (likely merged into other sections)

### 📝 Minor Updates
| File | Change |
|---|---|
| `statusline_agent.txt` | +286% — expanded agent status formatting |
| `default_agent_prompt.txt` | +219% — tool-specific descriptions added |
| `agents_sdk.txt` | +201% — SDK agent identity expanded |
| `explore_agent.txt` | +153% — exploration guidelines refined |
| `todo_list_usage.txt` | +111% — task tracking rules expanded |
| `sandbox_failure.txt` | +26% — sandbox error handling updated |
| `cyber_risk.txt` | +5% — model refs updated, minor wording |

---

## 📁 Complete File Index (53 sections)

### 🔑 Identity & Core (82-84 MB cluster)
| File | Size | Description |
|---|---|---|
| `agents_sdk.txt` | 4.6 KB | "You are a Claude agent, built on Anthropic's Claude Agent SDK" |
| `default_agent_prompt.txt` | 4.7 KB | Default agent identity + tool descriptions |
| `interactive_agent_intro.txt` | 5.8 KB | "You work alongside the user..." |
| `capability_statement.txt` | 4.5 KB | Software engineering task framing |
| `claude_md_override.txt` | 4.1 KB | CLAUDE.md rule override behavior |
| `session_title.txt` | 2.3 KB | Session title + git branch name generator |
| `injected_context_notice.txt` | 0.3 KB | Context injection notice text |

### 🛡️ Safety & Policy (82-84 MB cluster)
| File | Size | Description |
|---|---|---|
| `cyber_risk.txt` | 1.8 KB | Authorized security testing policy |
| `policy_spec.txt` | 4.0 KB | Bash command prefix detection |
| `tool_denial_guidance.txt` | 2.7 KB | Tool denial response guidance |
| `tool_denial_user.txt` | 1.9 KB | User-facing tool denial messages |
| `sandbox_failure.txt` | 3.2 KB | Sandbox error/warning templates |
| `memory_selection.txt` | 1.3 KB | Memory selection rules |

### 🤖 Agent System (82-130 MB)
| File | Size | Description |
|---|---|---|
| `autonomous_loop.txt` | 7.8 KB | Timer-invoked autonomous operation |
| `autonomous_loop_tick.txt` | 0.7 KB | Single autonomous tick prompt |
| `blast_radius.txt` | 16.1 KB | Full system harness: System + Language + Output + Tools + Tone + Care |
| `context_management.txt` | 10.0 KB | Auto-compact and context limit handling |
| `compact_service.txt` | 3.8 KB | Compact/reactive-compact service prompt |
| `exit_plan_mode.txt` | 1.0 KB | Exit plan mode instructions |

### 🎯 Plan Mode (82-131 MB)
| File | Size | Description |
|---|---|---|
| `plan_mode_instructions.txt` | 3.7 KB | "Plan mode is active. You MUST NOT make edits..." |
| `plan_rejected.txt` | 3.1 KB | Plan rejected response |
| `plan_rejected_detail.txt` | 2.7 KB | Detailed plan rejection |
| `plan_agent.txt` | 3.5 KB | Plan mode agent behavior |
| `plan_agent_specialist.txt` | 2.5 KB | Plan specialist subagent |
| `plan_tool.txt` | 3.6 KB | Plan tool usage guide |
| `plan_artifact_tool.txt` | 0.5 KB | Plan artifact tool |
| `plan_vs_memory.txt` | 3.2 KB | Plan vs memory distinction |

### 🔧 Tools & MCP (82-103 MB)
| File | Size | Description |
|---|---|---|
| `mcp.txt` | 4.1 KB | MCP server instructions |
| `knowledge_mcp_search.txt` | 1.5 KB | Knowledge MCP search tool |
| `web_fetch.txt` | 4.1 KB | Web fetch tool + content processing |
| `web_fetch_tool.txt` | 1.4 KB | Web fetch tool behavior |
| `chrome_browser_important.txt` | 3.5 KB | Chrome browser automation |
| `claude_in_chrome.txt` | 0.7 KB | Claude-in-Chrome specific |
| `skills.txt` | 0.9 KB | Skills tool usage |
| `hooks.txt` | 3.0 KB | Hook system integration |
| `hook_condition.txt` | 0.4 KB | Hook condition guard |
| `advisor_tool.txt` | 3.6 KB | Advisor tool specification |
| `scratchpad_directory.txt` | 24.2 KB | Scratchpad directory management |
| `custom_workflow_body.txt` | 6.0 KB | Custom workflow body prompt |

### 🔀 Git & PR (109-122 MB)
| File | Size | Description |
|---|---|---|
| `git_operations.txt` | 2.2 KB | Git command rules and restrictions |
| `git_workflow.txt` | 1.4 KB | Git workflow patterns |
| `commit_messages_pr.txt` | 0.7 KB | Commit message + PR conventions |
| `sandbox_failure.txt` | 3.2 KB | (also in safety) |

### 🤝 Communication & Output (83-215 MB)
| File | Size | Description |
|---|---|---|
| `team_communication.txt` | 2.7 KB | SendMessage / team communication |
| `send_message_tool.txt` | 0.2 KB | SendMessage tool brief |
| `output_style_proactive.txt` | 1.6 KB | Proactive output style |
| `statusline_agent.txt` | 7.2 KB | Agent status line format |
| `stop_condition.txt` | 1.1 KB | Stop condition rules |

### 📋 Task Management (83-120 MB)
| File | Size | Description |
|---|---|---|
| `todo_list_usage.txt` | 4.2 KB | Todo list usage rules |
| `todo_reminder.txt` | 3.1 KB | Todo reminder triggers |
| `auto_mode_classifier.txt` | 2.2 KB | Auto mode classifier rules |
| `auto_mode_classifier_intro.txt` | 2.9 KB | Classifier intro prompt |
| `auto_mode_process.txt` | 1.6 KB | Auto mode process flow |
| `explore_agent.txt` | 2.5 KB | Explore agent definition |

---

## 🗺️ Binary Offset Map

```
 58 MB  ██ claude_md_override
        |
 82 MB  ████████████████████████████████████████████████████████
        █ IDENTITY CLUSTER (82-84 MB)                           █
        █ agents_sdk, default_agent, interactive_agent_intro,   █
        █ cyber_risk, policy_spec, plan_mode_*, team_comm,      █
        █ chrome_browser, memory, tool_denial, web_fetch,       █
        █ mcp, hooks, session_title, claude_md_override,        █
        █ advisor_tool, exit_plan_mode, plan_rejected, todo_*   █
 84 MB  ████████████████████████████████████████████████████████
        |
 85 MB  ██ auto_mode_classifier
 90 MB  ██ statusline_agent
 94 MB  ██ plan_vs_memory
 97 MB  ██ web_fetch_tool
 99 MB  ██ autonomous_loop_tick
100 MB  ██ skills
103 MB  ██ explore_agent
108 MB  ██ plan_agent_specialist
109 MB  ██ commit_messages_pr, git_workflow, sandbox_failure
110 MB  ██ plan_tool
114 MB  ██ send_message_tool, todo_list_usage
118 MB  ██ git_operations
121 MB  ██ capability_statement, injected_context_notice
122 MB  ██ hook_condition, stop_condition
124 MB  ██ plan_agent, plan_mode_instructions
131 MB  ██ plan_agent (tail)
134 MB  ██ claude_in_chrome
154 MB  ██ custom_workflow_body
186 MB  ██ compact_service
205 MB  ██ output_style_proactive
        |
225 MB  ████████████████████████████████████████████████████████
        █ LARGE PROMPT CLUSTER (225-242 MB)                     █
        █ autonomous_loop, blast_radius, context_management     █
242 MB  ████████████████████████████████████████████████████████
227 MB  ██ scratchpad_directory
```

---

## 🔬 Extraction Method

1. **String dump** — Python chunked reader extracts 217,961 ASCII/UTF-8 sequences (≥30 chars) from 258 MB binary → `_all_strings.txt` (40.1 MB)
2. **Marker matching** — Each v2.1.205 section's first meaningful line searched against the string dump to locate offset
3. **Radius extraction** — ±5-8 KB around each marker extracted to individual `.txt` files
4. **Quality** — Files contain **raw strings**; prompt text is embedded within minified JS/config fragments. Large standalone sections (autonomous_loop, blast_radius) are near-clean. Dense cluster sections (82-84 MB) contain JS noise proportional to cluster density.

---

## 📦 Raw Artifacts

| File | Size | Description |
|---|---|---|
| `_all_strings.txt` | 40.1 MB | Full string extraction (217,961 entries with offsets) |
| `*.txt` (53 files) | ~220 KB | Individual prompt sections |

---

*U-C4N Extraction — 2026-07-21*
