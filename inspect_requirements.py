from pathlib import Path
p = Path('requirements.txt')
text = p.read_text(encoding='utf-16')
print(text)
print('--- lines ---')
for i, line in enumerate(text.splitlines(), 1):
    print(i, repr(line))
