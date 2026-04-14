import re

with open('inject_pms_actions.js', 'rb') as f:
    content = f.read().decode('utf-16le')

# Find strings that look like labels or titles
strings = re.findall(r'["\']([^"\']{5,})["\']', content)
for s in strings:
    if any(keyword in s for keyword in ['Justificativa', 'Observaç', 'Salvar', 'Quadrimestre']):
        print(s)
