import re
import json

def parse_actions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    actions_data = {}
    current_meta = None
    
    # Regex for Meta: e.g., 1.1.1 or 2.1.10
    meta_regex = re.compile(r'^(\d+\.\d+(\.\d+)+)')
    # Regex for Action: e.g., Ação Nº 1, Ação N.º 1, Ação N° 1
    # Using re.search or refining match to handle tabs/spaces better
    action_regex = re.compile(r'^Ação\s+N[.°º]*\s*[\w\.]+\t*(.*)', re.IGNORECASE)

    for line_idx, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        meta_match = meta_regex.search(line)
        if meta_match and line.startswith(meta_match.group(1)):
            current_meta = meta_match.group(1)
            if current_meta not in actions_data:
                actions_data[current_meta] = []
            continue
            
        action_match = action_regex.match(line)
        if action_match and current_meta:
            action_text = action_match.group(1).strip()
            if action_text:
                actions_data[current_meta].append(action_text)
            continue
            
    return actions_data

if __name__ == "__main__":
    path = r'c:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\PAS 2026 _Ações.txt'
    data = parse_actions(path)
    
    output_path = r'c:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\actions_extracted_full.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Extracted {len(data)} metas with actions.")
