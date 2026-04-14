import re

def check_metas():
    with open('src/lib/metas.ts', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex for getting each meta object
    metas_raw = re.findall(r'\{[^{}]+\}', content)
    total_metas = len(metas_raw)
    metas_with_actions = 0
    
    for meta in metas_raw:
        if '"acoes":' in meta:
            metas_with_actions += 1
            
    print(f"Total Metas: {total_metas}")
    print(f"Metas with actions: {metas_with_actions}")

if __name__ == "__main__":
    check_metas()
