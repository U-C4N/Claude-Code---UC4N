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

# Section offsets from previous search
sections = {
    'advisor_tool': 87078164,
    'agents_sdk': 87030333,
    'auto_mode_classifier': 90985868,
    'auto_mode_classifier_intro': 88115116,
    'auto_mode_process': 87153020,
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
    'send_message_tool': 123397932,
    'session_title': 87090924,
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

# Try to find missing sections from prev version content
for fname in ['autonomous_loop.txt', 'git_workflow.txt', 'hook_condition.txt', 'scratchpad_directory.txt', 'skills.txt']:
    filepath = os.path.join(prev_dir, fname)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    found = False
    for line in lines:
        line = line.strip()
        if len(line) > 40 and not line.startswith('{') and not line.startswith('`') and not line.startswith('function') and not re.match(r'^[a-zA-Z_]\w*\s*[:=]', line):
            # Use first 60 chars of this meaningful line
            key = line[:60]
            for off, text in entries:
                if key.lower() in text.lower():
                    name = fname.replace('.txt', '')
                    sections[name] = off
                    print(f'Found {name} at offset {off}')
                    found = True
                    break
            if found:
                break
    
    if not found:
        print(f'Could not find {fname}')

# Also search specific known phrases for missing ones
extra_searches = {
    'autonomous_loop': ['Claude is running in autonomous mode', 'autonomous mode', 'This is a Claude Code'],
    'git_workflow': ['Never run destructive commands', 'commit workflow'],
    'skills': ['configured MCP servers', 'available skills'],
}

for name, keys in extra_searches.items():
    if name in sections:
        continue
    for key in keys:
        for off, text in entries:
            if key.lower() in text.lower():
                sections[name] = off
                print(f'Found {name} at offset {off} with: {key}')
                break
        if name in sections:
            break

print(f'\nTotal sections to extract: {len(sections)}')

# Extract each section
for name, offset in sorted(sections.items()):
    radius = 15000
    nearby_texts = []
    for off, text in entries:
        if offset - radius <= off <= offset + radius:
            nearby_texts.append((off, text))
    
    result = '\n'.join([t for _, t in nearby_texts])
    
    filepath = os.path.join(outdir, f'{name}.txt')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)
    
    size_kb = len(result) / 1024
    print(f'{name}.txt: {len(nearby_texts)} strings, {size_kb:.1f}KB')

print('\nDone extracting all sections!')
