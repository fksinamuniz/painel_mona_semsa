import re

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Ver tudo em torno do localStorage
print("=== TODOS OS localStorage (contexto amplo) ===")
for i, m in enumerate(re.finditer(r'localStorage', content)):
    idx = m.start()
    snippet = content[max(0,idx-150):idx+400]
    print(f"\n--- Ocorrencia {i+1} (pos {idx}) ---")
    print(snippet)
