# -*- coding: utf-8 -*-
"""
Patch correto: substitui o array 'kr' (metas hardcoded) no bundle JS.
O array comeca em: kr = [\n    {\n      d: "1",\n      num: "1.1.1",...
"""
import sys, json, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

METAS_TS = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\src\lib\metas.ts'
BUNDLE   = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\public\monitoramento\assets\index-xH-p0FqE.js'

# 1. Ler metas
with open(METAS_TS, encoding='utf-8') as f:
    ts_content = f.read()
match = re.search(r'export const METAS\s*=\s*(\[.*\])\s*;?\s*$', ts_content, re.DOTALL)
metas = json.loads(match.group(1))
print(f"Metas novas: {len(metas)}")

# 2. Ler bundle original
with open(BUNDLE, encoding='utf-8', errors='replace') as f:
    bundle = f.read()
print(f"Bundle: {len(bundle)} chars")

# 3. Encontrar 'kr = [' que precede a primeira meta
# Posicao conhecida: ~355600
# Buscar o padrao exato
pat = re.search(r'\bkr\s*=\s*\[', bundle)
if not pat:
    print("ERRO: 'kr = [' nao encontrado no bundle!")
    sys.exit(1)

arr_open = pat.end() - 1  # posicao do '['
print(f"'kr = [' encontrado em: {pat.start()}, '[' em: {arr_open}")
print(f"Contexto: {bundle[arr_open:arr_open+100]}")

# 4. Balancear colchetes para achar fechamento
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
print(f"Array kr: [{arr_open}:{arr_close}] ({arr_close - arr_open + 1} chars)")
print(f"Primeiros 200: {orig_block[:200]}")

# Contar metas no bloco original
orig_count = orig_block.count('"num":') + orig_block.count('num:"') + orig_block.count("num: \"")
print(f"Metas no bloco original: ~{orig_count}")

# 5. Gerar novo array no mesmo formato
def fmt_meta(m):
    lines = [
        '    {',
        f'      d: {json.dumps(m["d"], ensure_ascii=False)},',
        f'      num: {json.dumps(m["num"], ensure_ascii=False)},',
        f'      desc: {json.dumps(m["desc"], ensure_ascii=False)},',
        f'      ind: {json.dumps(m["ind"], ensure_ascii=False)},',
        f'      un: {json.dumps(m["un"], ensure_ascii=False)},',
        f'      m2026: {json.dumps(m["m2026"], ensure_ascii=False)},',
        f'      m2027: {json.dumps(m["m2027"], ensure_ascii=False)},',
        f'      m2028: {json.dumps(m["m2028"], ensure_ascii=False)},',
        f'      m2029: {json.dumps(m["m2029"], ensure_ascii=False)},',
    ]
    if m.get('acoes'):
        acoes_js = '[\n' + ',\n'.join(f'        {json.dumps(a, ensure_ascii=False)}' for a in m['acoes']) + '\n      ]'
        lines.append(f'      acoes: {acoes_js},')
    lines.append('    }')
    return '\n'.join(lines)

new_array = '[\n' + ',\n'.join(fmt_meta(m) for m in metas) + '\n  ]'
print(f"Novo array: {len(new_array)} chars, {len(metas)} metas")

# 6. Substituir e salvar
new_bundle = bundle[:arr_open] + new_array + bundle[arr_close+1:]
print(f"Bundle novo: {len(new_bundle)} chars")

# Verificar
check = new_bundle.count('num: "1.1.1"')
print(f"Verificacao 'num: 1.1.1': {check} ocorrencias (esperado 1)")

with open(BUNDLE, 'w', encoding='utf-8', errors='replace') as f:
    f.write(new_bundle)

print(f"\n[OK] Bundle atualizado! {len(metas)} metas no array 'kr'.")
print("Pressione Ctrl+F5 no painel para recarregar.")
