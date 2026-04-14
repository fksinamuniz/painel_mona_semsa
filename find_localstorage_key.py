import re, json

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Encontrar a chave do localStorage
print("=== LOCALSTORAGE: getItem / setItem ===")
for m in re.finditer(r'localStorage\.(getItem|setItem)\s*\(["\']([^"\']+)["\']', content):
    print(f"  {m.group(0)}")

# 2. Buscar pelo nome da chave que armazena os dados do PMS
print("\n=== getItem calls ===")
for m in re.finditer(r'localStorage\.getItem\(([^)]+)\)', content):
    idx = m.start()
    print(f"  pos {idx}: {content[idx:idx+200]}")
    print()

# 3. Buscar por "pms" ou "monitoramento" como possivel chave
print("\n=== Strings 'pms', 'monit' ===")
for term in ['pms', 'monit', 'dados', 'estado', 'state', 'store']:
    for m in re.finditer(f'["\\\']({term}[^"\\\']*)["\\\']', content, re.IGNORECASE):
        idx = m.start()
        snippet = content[max(0, idx-30):idx+100]
        if 'localStorage' in content[max(0,idx-200):idx+200]:
            print(f"  '{term}' -> chave: {m.group(1)} (com localStorage próximo)")
