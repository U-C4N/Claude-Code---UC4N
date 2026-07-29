import os

entries_file = r'C:\Users\ACER\Documents\GitHub\Claude Code - UC4N\Claude_Code_v2.1.220\_all_strings.txt'
outdir = r'C:\Users\ACER\Documents\GitHub\Claude Code - UC4N\Claude_Code_v2.1.220'

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

# New section candidates to extract
new_candidates = [
    ('advisor_tool_prompt', 244472169),
    ('continue_session_prompt', 244921943),
    ('plan_mode_reminder', 243531032),
    ('available_tools_guidance', 245032246),
    ('mcp_tab_group_tool', 174548060),
    ('screenshot_tool_prompt', 111404324),
    ('browser_guidelines', 249702594),
    ('claude_md_structure', 220352088),
]

for name, offset in new_candidates:
    radius = 5000
    nearby = []
    for off, text in entries:
        if abs(off - offset) <= radius:
            nearby.append((off, text))
    
    result = '\n'.join([t for _, t in nearby])
    
    filepath = os.path.join(outdir, f'{name}.txt')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f'{name}.txt: {len(nearby)} strings, {len(result)/1024:.1f}KB at offset {offset}')

# Also extract the larger doc files (Managed Agents etc)
# These are huge markdown files embedded in the binary
doc_candidates = [
    ('managed_agents_ruby', 256766963, 30000),
    ('managed_agents_events', 256998608, 30000),
    ('typescript_api_guide', 257381841, 20000),
]

for name, offset, radius in doc_candidates:
    nearby = []
    for off, text in entries:
        if abs(off - offset) <= radius:
            nearby.append((off, text))
    
    # Try to find natural language content, filter JS noise
    clean_parts = []
    for off, text in nearby:
        alpha = sum(1 for c in text[:100] if c.isalpha()) / max(len(text[:100]), 1)
        if alpha > 0.3 and len(text) > 50:
            clean_parts.append(text)
    
    result = '\n'.join(clean_parts)
    filepath = os.path.join(outdir, f'{name}.txt')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f'{name}.txt: {len(nearby)} raw strings, {len(result)/1024:.1f}KB clean content at offset {offset}')

print('\nDone!')
