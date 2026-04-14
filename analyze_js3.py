import re, json

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Ver trecho maior em torno de DIRETRIZ
idx = content.upper().find('DIRETRIZ')
if idx != -1:
    snippet = content[max(0, idx-500):idx+2000]
    print("=== Trecho em torno de DIRETRIZ ===")
    print(snippet[:3000])

# Tambem buscar estrutura de acoes
print("\n\n=== Busca por 'acoes:' ou 'acoes=[' ===")
for m in re.finditer(r'acoes', content[:800000]):
    idx2 = m.start()
    snippet2 = content[max(0, idx2-50):idx2+300]
    if '{' in snippet2 or '[' in snippet2:
        print(f"Pos {idx2}: {snippet2[:300]}")
        print("---")
