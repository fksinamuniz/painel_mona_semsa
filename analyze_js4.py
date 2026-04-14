import re

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Busca contexto de acoes + setDB
print("=== setDB + acoes ===")
for m in re.finditer(r'setDB', content):
    idx = m.start()
    snippet = content[max(0, idx-100):idx+400]
    if 'acoes' in snippet or 'acao' in snippet.lower():
        print(f"Pos {idx}:")
        print(snippet[:500])
        print("---")

# Busca estrutura de metas - pode ter um array de objetos com id, titulo, acoes
print("\n=== Busca por estrutura {id:, titulo: ===")
for m in re.finditer(r'\{id:"[^"]+",titulo:"[^"]*"', content):
    idx = m.start()
    snippet = content[idx:idx+500]
    print(f"Pos {idx}: {snippet[:400]}")
    print("---")
