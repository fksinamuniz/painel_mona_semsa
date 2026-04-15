# -*- coding: utf-8 -*-
"""
Le o DOMI_PMS_2022-2029.xlsx e gera metas.ts atualizado.
Preserva o campo 'acoes' do metas.ts original.
"""
import sys, openpyxl, json, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

XLSX_PATH = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\DOMI_PMS_2022-2029.xlsx'
METAS_TS  = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\src\lib\metas.ts'

# ── 1. Ler o XLSX ──────────────────────────────────────────────────────────────
wb = openpyxl.load_workbook(XLSX_PATH)
ws = wb['METAS']

def fmt_value(v, unidade):
    """Formata valor de meta de acordo com a unidade declarada."""
    if v is None:
        return "0"
    if isinstance(v, str):
        return v.strip()

    u = str(unidade).lower() if unidade else ""
    is_pct_unit = "percentual" in u or "%" in u

    if isinstance(v, float):
        if is_pct_unit:
            # ex: 0.74 -> "74%", 0.1309 -> "13,09%"
            pct = round(v * 100, 2)
            if pct == int(pct):
                return f"{int(pct)}%"
            return f"{pct}%".replace('.', ',')
        else:
            # taxa, indice, numero absoluto - manter como numero
            if v == int(v):
                return str(int(v))
            return str(v).replace('.', ',')

    if isinstance(v, int):
        if is_pct_unit:
            return f"{v}%"
        return str(v)

    return str(v)

xlsx_rows = {}
for row in ws.iter_rows(min_row=6, values_only=True):
    num = row[0]
    if num is None:
        continue
    num = str(num).strip()
    if not re.match(r'^\d+\.\d+\.\d+', num):
        continue

    desc = str(row[1] or "").strip()
    ind  = str(row[2] or "").strip()
    un   = str(row[7] or "").strip()
    v26  = row[9]
    v27  = row[10]
    v28  = row[11]
    v29  = row[12]
    d    = num.split('.')[0]

    xlsx_rows[num] = {
        "d"    : d,
        "num"  : num,
        "desc" : desc,
        "ind"  : ind,
        "un"   : un,
        "m2026": fmt_value(v26, un),
        "m2027": fmt_value(v27, un),
        "m2028": fmt_value(v28, un),
        "m2029": fmt_value(v29, un),
    }

print(f"XLSX: {len(xlsx_rows)} metas lidas")

# ── 2. Ler acoes do metas.ts original ─────────────────────────────────────────
with open(METAS_TS, encoding='utf-8') as f:
    ts_content = f.read()

match = re.search(r'export const METAS\s*=\s*(\[.*\])\s*;?\s*$', ts_content, re.DOTALL)
if not match:
    raise ValueError("Nao encontrou export const METAS no metas.ts")

metas_original = json.loads(match.group(1))
acoes_map = {m['num']: m['acoes'] for m in metas_original if 'acoes' in m}
print(f"metas.ts: {len(metas_original)} metas | {len(acoes_map)} com acoes")

# ── 3. Mesclar ────────────────────────────────────────────────────────────────
updated   = []
alterados = 0
iguais    = 0
novos     = []

for num, x in sorted(xlsx_rows.items(), key=lambda k: [int(p) for p in k[0].split('.')]):
    entry = dict(x)
    if num in acoes_map:
        entry['acoes'] = acoes_map[num]

    orig = next((m for m in metas_original if m['num'] == num), None)
    if orig:
        mudou = any(orig.get(k) != x[k] for k in ['m2026','m2027','m2028','m2029','desc','ind'])
        if mudou:
            alterados += 1
            print(f"  ALT {num}: desc/metas atualizadas")
        else:
            iguais += 1
    else:
        novos.append(num)

    updated.append(entry)

# Manter entradas do metas.ts que nao estao no XLSX
for m in metas_original:
    if m['num'] not in xlsx_rows:
        updated.append(m)
        print(f"  MANTIDO (so no metas.ts): {m['num']}")

# ── 4. Gerar novo metas.ts ─────────────────────────────────────────────────────
lines = ["export const METAS = ["]
for i, entry in enumerate(updated):
    sep = "," if i < len(updated) - 1 else ""
    fields = list(entry.items())
    lines.append("  {")
    for fi, (k, v) in enumerate(fields):
        comma = "," if fi < len(fields) - 1 else ""
        if isinstance(v, list):
            items = json.dumps(v, ensure_ascii=False)
            lines.append(f'    "{k}": {items}{comma}')
        else:
            lines.append(f'    "{k}": {json.dumps(v, ensure_ascii=False)}{comma}')
    lines.append("  }" + sep)
lines.append("];")

new_content = "\n".join(lines) + "\n"

with open(METAS_TS, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\n[OK] metas.ts atualizado!")
print(f"   Total   : {len(updated)}")
print(f"   Iguais  : {iguais}")
print(f"   Alterados: {alterados}")
print(f"   Novos   : {len(novos)} -> {novos}")
