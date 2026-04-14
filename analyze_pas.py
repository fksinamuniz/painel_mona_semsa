import json

with open('pas_tables.json', encoding='utf-8') as f:
    data = json.load(f)

# Mostra todas tabelas com numero e header
print("=== TODAS AS TABELAS ===")
for t in data:
    h = t['dados'][0] if t['dados'] else []
    print(f"Tabela {t['tabela']} ({t['linhas']} linhas): {' | '.join(h)[:120]}")

print()
print("=== TABELAS 13 a 25 (busca por acoes/objetivos) ===")
for t in data[12:25]:
    print(f"\n--- Tabela {t['tabela']} ({t['linhas']} linhas) ---")
    for i, row in enumerate(t['dados'][:6]):
        print(f"  Linha {i+1}: {row}")
