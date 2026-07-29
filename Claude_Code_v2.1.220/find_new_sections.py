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

# Collect ALL offsets already covered by existing section files
covered_offsets = set()
for fname in os.listdir(outdir):
    if not fname.endswith('.txt') or fname.startswith('_') or fname == 'extract_sections.py':
        continue
    filepath = os.path.join(outdir, fname)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for line in content.split('\n'):
        if line.startswith('['):
            try:
                off = int(line[1:].split(']')[0])
                covered_offsets.add(off)
            except:
                pass

print(f'Already covered {len(covered_offsets)} string offsets')

# Find large strings (150+ chars) that look like prompt text, not JS code
prompt_like = []
for off, text in entries:
    if len(text) >= 150 and off not in covered_offsets:
        # Skip pure JS noise: lines starting with common JS patterns
        first_stripped = text[:50].strip()
        if re.match(r'^(const |let |var |function |class |return |if |for |while |switch |import |export |async |await |try |catch |throw |new |typeof |instanceof |this\.|require\(|module\.|process\.|console\.|JSON\.|Object\.|Array\.|String\.|Number\.|Date\.|Math\.|Promise\.|Error\b)', first_stripped):
            continue
        # Skip strings that are just punctuation/symbols
        if re.match(r'^[^a-zA-Z]{10,}', text[:30]):
            continue
        # Skip strings that are clearly error messages or internal node stuff
        if re.match(r'^(Error|Warning|SyntaxError|TypeError|ReferenceError|RangeError)', text):
            continue
        prompt_like.append((off, text))

print(f'\nFound {len(prompt_like)} potential new prompt strings not in existing sections')

# Sort and cluster them by proximity (cluster if within 500 bytes)
prompt_like.sort(key=lambda x: x[0])
clusters = []
current_cluster = []
for off, text in prompt_like:
    if not current_cluster:
        current_cluster = [(off, text)]
    elif off - current_cluster[-1][0] < 500:
        current_cluster.append((off, text))
    else:
        if len(current_cluster) >= 3 or sum(len(t) for _, t in current_cluster) > 500:
            clusters.append(current_cluster)
        current_cluster = [(off, text)]

if current_cluster and (len(current_cluster) >= 3 or sum(len(t) for _, t in current_cluster) > 500):
    clusters.append(current_cluster)

print(f'Found {len(clusters)} clusters of potential new sections')

# Check what's in the prev version to identify genuinely new content
prev_files = [f for f in os.listdir(prev_dir) if f.endswith('.txt') and not f.startswith('_')]
prev_first_lines = {}
for pf in prev_files:
    with open(os.path.join(prev_dir, pf), 'r', encoding='utf-8') as f:
        content = f.read(1000)
    lines = [l.strip() for l in content.split('\n') if l.strip() and len(l.strip()) > 30]
    if lines:
        prev_first_lines[pf] = lines[0][:80]

# For each cluster, show a preview
new_section_candidates = []
for i, cluster in enumerate(clusters):
    start_off = cluster[0][0]
    end_off = cluster[-1][0]
    total_chars = sum(len(t) for _, t in cluster)
    
    # Get concatenated text for analysis
    full_text = ' '.join([t for _, t in cluster])
    
    # Check if this is already captured by any existing section
    already_captured = False
    for _, text in entries:
        if off in covered_offsets:
            continue
        break
    
    # Check first meaningful sentence
    preview = full_text[:200]
    
    new_section_candidates.append((start_off, end_off, total_chars, preview, cluster))

# Sort by size (largest first)
new_section_candidates.sort(key=lambda x: -x[2])

print(f'\n=== TOP CANDIDATES FOR NEW SECTIONS ===')
for start_off, end_off, size, preview, cluster in new_section_candidates[:20]:
    print(f'\n--- Offset {start_off} (cluster size: {size} chars, {len(cluster)} strings) ---')
    print(f'Preview: {preview[:150]}')
    print()

# Also specifically look for common prompt pattern markers
print('\n=== SEARCHING FOR KNOWN PROMPT MARKERS ===')
markers = [
    'You are Claude Code',
    'You are an autonomous AI agent',
    'system_prompt',
    'systemPrompt',
    'SYSTEM_PROMPT',
    'identity_cli',
    'identity_sdk',
    'identity_agent',
    'You are a helpful assistant',
    'Claude agent, built on',
    'running within the Claude Agent SDK',
]

for marker in markers:
    for off, text in entries:
        if marker.lower() in text.lower() and off not in covered_offsets:
            print(f'  Found unclaimed marker "{marker}" at offset {off}: {text[:100]}')
            break

print('\nDone scanning!')
