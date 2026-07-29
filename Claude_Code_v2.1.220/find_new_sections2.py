import os, re

entries_file = r'C:\Users\ACER\Documents\GitHub\Claude Code - UC4N\Claude_Code_v2.1.220\_all_strings.txt'
outdir = r'C:\Users\ACER\Documents\GitHub\Claude Code - UC4N\Claude_Code_v2.1.220'
prev_dir = r'C:\Users\ACER\Documents\GitHub\Claude Code - UC4N\Claude_Code_v2.1.216'

# Load entries
entries = []
with open(entries_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('['):
            parts = line.split('] ', 1)
            if len(parts) == 2:
                off = int(parts[0][1:])
                text = parts[1]
                entries.append((off, text))

print(f'Loaded {len(entries)} entries')

# Known section offsets from extraction (offset +-15000 radius)
section_radius = 15000
section_offsets = {
    'advisor_tool': 87078164,
    'agents_sdk': 87030333,
    'auto_mode_classifier': 90985868,
    'auto_mode_classifier_intro': 88115116,
    'auto_mode_process': 87153020,
    'autonomous_loop': 242700762,
    'autonomous_loop_tick': 105766876,
    'blast_radius': 249517891,
    'capability_statement': 130504324,
    'chrome_browser_important': 88098418,
    'claude_in_chrome': 108001724,
    'claude_md_override': 87074132,
    'commit_messages_pr': 125840396,
    'compact_service': 206425236,
    'context_management': 249543940,
    'custom_workflow_body': 165803268,
    'cyber_risk': 88084516,
    'default_agent_prompt': 87030333,
    'exit_plan_mode': 88049172,
    'explore_agent': 108685852,
    'git_operations': 125040724,
    'git_workflow': 125040724,
    'hook_condition': 131977364,
    'hooks': 89022204,
    'injected_context_notice': 130647916,
    'interactive_agent_intro': 130499852,
    'knowledge_mcp_search': 88381188,
    'mcp': 87033244,
    'memory_selection': 88112172,
    'output_style_proactive': 110232828,
    'plan_agent': 134052172,
    'plan_agent_specialist': 108698348,
    'plan_artifact_tool': 88832356,
    'plan_mode_instructions': 134054045,
    'plan_rejected': 88112633,
    'plan_rejected_detail': 88115116,
    'plan_tool': 115691504,
    'plan_vs_memory': 100389452,
    'policy_spec': 88087036,
    'sandbox_failure': 125861972,
    'scratchpad_directory': 245308769,
    'send_message_tool': 123397932,
    'session_title': 87090924,
    'skills': 105890004,
    'statusline_agent': 96005188,
    'stop_condition': 131995236,
    'team_communication': 88002684,
    'todo_list_usage': 122690516,
    'todo_reminder': 88005236,
    'tool_denial_guidance': 88115116,
    'tool_denial_user': 87009732,
    'web_fetch': 87025672,
    'web_fetch_tool': 103142500,
}

def is_covered(offset):
    """Check if offset falls within any known section's radius"""
    for name, sec_off in section_offsets.items():
        if abs(offset - sec_off) <= section_radius:
            return name
    return None

# Find ALL medium-to-large strings (200+ chars) that look like prompt text
# and are NOT covered by existing sections
uncovered_prompts = []

for off, text in entries:
    if len(text) < 200:
        continue
    if is_covered(off):
        continue
    
    # Skip JS noise
    first50 = text[:50].strip()
    if re.match(r'^(const |let |var |function |class |return |if |for |while |switch |import |export |async |await |try |catch |throw |new |typeof |instanceof |this\.|require\(|module\.|process\.|console\.|JSON\.|Object\.|Array\.|String\.|)', first50):
        continue
    if re.match(r'^[^a-zA-Z]{20,}', first50):
        continue
    if text.startswith('`') and '{' not in text[:100]:
        continue
    
    # Count how much of this looks like natural language
    alpha_ratio = sum(1 for c in text[:200] if c.isalpha()) / max(len(text[:200]), 1)
    if alpha_ratio < 0.4:
        continue
    
    # Check for prompt-like patterns
    prompt_indicators = ['You are', 'you are', 'your task', 'you should', 'you must', 
                         'you can', 'do not', 'never', 'always', 'when the user',
                         'Claude', 'system', 'instructions', 'guidelines',
                         'tool', 'function', 'environment', 'answer']
    has_indicator = any(ind in text.lower() for ind in prompt_indicators)
    
    if not has_indicator and len(text) < 500:
        continue
    
    uncovered_prompts.append((off, text[:200], len(text)))

# Sort by size desc
uncovered_prompts.sort(key=lambda x: -x[2])

print(f'\n=== UNCOVERED PROMPT-LIKE STRINGS (potential new sections) ===')
print(f'Found {len(uncovered_prompts)} candidates\n')

for i, (off, preview, size) in enumerate(uncovered_prompts[:30]):
    print(f'--- Candidate #{i+1} | Offset: {off} | Size: {size} chars ---')
    print(f'  {preview}')
    print()

# Also specifically search for prompt patterns known from Claude code
print('\n=== SPECIFIC PROMPT PATTERN SEARCH ===')
important_markers = [
    'You are Claude',
    'You are an AI',
    'You are a helpful',
    'You are an expert',
    'You are an autonomous',
    'tool_use',
    'tool result',
    'system prompt',
    'Here is the',
    'Your task is',
    'You have access',
    'Function calling',
    'Available tools',
    'To use this tool',
    'When you need',
    'CRITICAL:',
    'IMPORTANT:',
    'WARNING:',
    'REMEMBER:',
    'NEVER:',
    'rules for',
    'guidelines for',
    '## ',
]

for marker in important_markers:
    for off, text in entries:
        if marker in text and len(text) > 100 and not is_covered(off):
            covered_by = is_covered(off)
            # Check if it's actually part of a nearby section
            nearby_section = None
            for name, sec_off in section_offsets.items():
                if abs(off - sec_off) <= section_radius + 5000:
                    nearby_section = name
                    break
            
            if not nearby_section:
                print(f'  NEW: "{marker}" at {off} ({len(text)} chars): {text[:120]}')
            break  # just first match per marker

print('\n=== DONE ===')
