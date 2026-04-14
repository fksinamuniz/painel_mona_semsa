import json
try:
    with open('pas_tables.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Total tables: {len(data)}")
    for t in data:
        header = t['dados'][0] if t['dados'] else []
        header_str = " | ".join(str(x) for x in header)
        if any(kw in header_str.lower() for kw in ['ação', 'acao', 'meta', 'objetivo']):
            print(f"Tab {t['tabela']} ({len(t['dados'])} rows): {header_str[:150]}")
except Exception as e:
    print(f"Error: {e}")
