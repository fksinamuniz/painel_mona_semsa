import re

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Pega trecho expandido do localStorage
for i, m in enumerate(re.finditer(r'localStorage', content)):
    idx = m.start()
    snippet = content[max(0,idx-600):idx+800]
    print(f"\n=== localStorage #{i+1} (pos {idx}) ===")
    print(snippet)
    print("---END---")
