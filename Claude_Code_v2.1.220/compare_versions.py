import os

prev_dir = r'C:\Users\ACER\Documents\GitHub\Claude Code - UC4N\Claude_Code_v2.1.216'
new_dir = r'C:\Users\ACER\Documents\GitHub\Claude Code - UC4N\Claude_Code_v2.1.220'

# Get all section files (exclude _all_strings.txt, extract_sections.py etc)
def get_section_files(dirpath):
    files = {}
    for fname in os.listdir(dirpath):
        fpath = os.path.join(dirpath, fname)
        if os.path.isfile(fpath) and fname.endswith('.txt') and not fname.startswith('_') and fname != 'extract_sections.py' and fname != 'find_new_sections.py' and fname != 'find_new_sections2.py' and fname != 'extract_new_sections.py':
            size = os.path.getsize(fpath)
            # Count meaningful chars (approx)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(200000)
            files[fname] = size
    return files

prev_files = get_section_files(prev_dir)
new_files = get_section_files(new_dir)

print("=== NEW FILES (not in v2.1.216) ===")
new_only = set(new_files.keys()) - set(prev_files.keys())
for f in sorted(new_only):
    print(f'  {f}: {new_files[f]/1024:.1f}KB')

print("\n=== REMOVED FILES (in v2.1.216 but not v2.1.220) ===")
removed = set(prev_files.keys()) - set(new_files.keys())
for f in sorted(removed):
    print(f'  {f}: was {prev_files[f]/1024:.1f}KB')

print("\n=== CHANGED FILES ===")
common = set(prev_files.keys()) & set(new_files.keys())
changes = []
for f in sorted(common):
    old_s = prev_files[f]
    new_s = new_files[f]
    diff = new_s - old_s
    pct = (diff / old_s * 100) if old_s > 0 else 0
    if abs(pct) > 3:  # only significant changes
        direction = '+' if diff > 0 else '-'
        changes.append((abs(pct), f, old_s, new_s, diff, pct))

changes.sort(key=lambda x: -x[0])
for pct_score, f, old_s, new_s, diff, pct in changes:
    print(f'  {f}: {old_s/1024:.1f}KB -> {new_s/1024:.1f}KB ({diff/1024:+.1f}KB, {pct:+.1f}%)')

print("\n=== BINARY INFO ===")
import os
binary = r'C:\Users\ACER\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe'
old_binary = None
# Check if old binary exists somewhere
print(f'New binary size: {os.path.getsize(binary)} bytes ({os.path.getsize(binary)/1024/1024:.0f} MB)')

# Total string count
entries_file = os.path.join(new_dir, '_all_strings.txt')
if os.path.exists(entries_file):
    with open(entries_file, 'r', encoding='utf-8') as f:
        line_count = sum(1 for _ in f)
    print(f'Total strings extracted: {line_count}')
