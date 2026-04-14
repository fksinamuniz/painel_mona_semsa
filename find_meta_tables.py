import json, re
try:
    with open('pas_tables.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Total tables: {len(data)}")
    pattern = re.compile(r'^\d+\.\d+\.\d+$')
    
    for t in data:
        header = t['dados'][0] if t['dados'] else []
        content_sample = " ".join(str(x) for x in t['dados'][:5])
        
        # Check if table contains meta codes like 1.1.1
        has_meta_code = any(pattern.match(str(cell).strip()) for row in t['dados'] for cell in row)
        
        if has_meta_code:
            print(f"Tab {t['tabela']} ({len(t['dados'])} rows) contains META CODES.")
            print(f"  Header: {' | '.join(str(x) for x in header)[:200]}")
            for row in t['dados'][:5]:
                print(f"    {row}")
            print("-" * 50)
            
except Exception as e:
    print(f"Error: {e}")
