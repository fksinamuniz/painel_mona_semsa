# -*- coding: utf-8 -*-
import sys, json, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

METAS_TS  = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\src\lib\metas.ts'
BUNDLE    = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\public\monitoramento\assets\index-xH-p0FqE.js'

with open(METAS_TS, encoding='utf-8') as f:
    ts_content = f.read()

match = re.search(r'export const METAS\s*=\s*(\[.*\])\s*;?\s*$', ts_content, re.DOTALL)
metas = json.loads(match.group(1))
print(f"Metas do metas.ts: {len(metas)}")

with open(BUNDLE, encoding='utf-8', errors='replace') as f:
    bundle = f.read()

# Buscar pela primeira meta no formato exato do bundle minificado
search_first = '{d:"1",num:"1.1.1"'
idx_first = bundle.find(search_first)
if idx_first < 0:
    # Tentar sem espacos
    search_first = 'd:"1",num:"1.1.1"'
    idx_first = bundle.find(search_first)

print(f"Posicao primeira meta: {idx_first}")
print(f"Contexto: {bundle[idx_first-10:idx_first+80]}")

# Andar para tras para pegar o [ de abertura do array
arr_open = bundle.rfind('[', 0, idx_first)
print(f"Abertura do array em: {arr_open}")
print(f"Contexto abertura: {bundle[arr_open-30:arr_open+30]}")

# Balancear colchetes para achar fechamento
depth = 0
arr_close = -1
for i in range(arr_open, len(bundle)):
    c = bundle[i]
    if c == '[':
        depth += 1
    elif c == ']':
        depth -= 1
        if depth == 0:
            arr_close = i
            break

orig_block = bundle[arr_open:arr_close+1]
count_check = orig_block.count('"num"')
print(f"Array encontrado: [{arr_open}:{arr_close}] ({arr_close - arr_open} chars)")
print(f"Ocorrencias de 'num' no bloco: {count_check}")
print(f"Primeiros 200 chars: {orig_block[:200]}")
print(f"Ultimos 100 chars: {orig_block[-100:]}")
