import json
import re

# Load extracted actions
with open('actions_extracted.json', 'r', encoding='utf-8') as f:
    actions_map = json.load(f)

# Path to metas.ts
metas_path = 'src/lib/metas.ts'

with open(metas_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find each object in METAS array
# We look for objects like { "d": "1", "num": "1.1.1", ... }
def update_meta(match):
    obj_str = match.group(0)
    # Extract num
    num_match = re.search(r'"num":\s*"([^"]+)"', obj_str)
    if num_match:
        num = num_match.group(1)
        if num in actions_map:
            # Check if acoes already exists
            if '"acoes":' in obj_str:
                # Replace existing acoes
                new_acoes = json.dumps(actions_map[num], ensure_ascii=False)
                obj_str = re.sub(r'"acoes":\s*\[[^\]]*\]', f'"acoes": {new_acoes}', obj_str)
            else:
                # Insert acoes before the closing brace
                new_acoes = json.dumps(actions_map[num], ensure_ascii=False, indent=4)
                # Cleanup indent for the last brace
                new_acoes = new_acoes.replace('\n', '\n    ')
                obj_str = obj_str.rstrip().rstrip('}').rstrip() + f',\n    "acoes": {new_acoes}\n  }}'
    return obj_str

# Match each object { ... } in the array
# We'll use a regex that matches from { to the next } while balancing if possible, 
# but since these are simple flat objects in metas.ts, it's easier.
new_content = re.sub(r'\{[^{}]+\}', update_meta, content)

with open(metas_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {metas_path} with extracted actions.")
