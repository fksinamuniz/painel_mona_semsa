import re

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Procura por localStorage ou IndexedDB ou fetch para entender onde os dados sao salvos
print("=== setDB implementacao ===")
for m in re.finditer(r'function setDB|setDB\s*=|const setDB|let setDB|var setDB', content):
    idx = m.start()
    print(content[max(0,idx-100):idx+500])
    print("---")

print("\n=== localStorage ===")
for m in re.finditer(r'localStorage', content):
    idx = m.start()
    print(content[max(0,idx-50):idx+200])
    print("---")

print("\n=== fetch\|api ===")
for m in re.finditer(r"fetch\(", content[:50000]):
    idx = m.start()
    print(content[max(0,idx-50):idx+200])
    print("---")
