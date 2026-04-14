import zipfile, json
from xml.etree import ElementTree as ET

path = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\PAS 2026 PRELIMINAR.docx'
ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def get_text(el):
    return ''.join(t.text or '' for t in el.iter(ns+'t'))

with zipfile.ZipFile(path, 'r') as z:
    with z.open('word/document.xml') as f:
        tree = ET.parse(f)

root = tree.getroot()
body = root.find('.//' + ns + 'body')
tables = body.findall('.//' + ns + 'tbl')

result = []
for i, tbl in enumerate(tables, start=1):
    rows = tbl.findall('.//' + ns + 'tr')
    table_data = []
    for row in rows:
        cells = row.findall('.//' + ns + 'tc')
        row_data = [get_text(c).strip() for c in cells]
        table_data.append(row_data)
    result.append({'tabela': i, 'linhas': len(rows), 'dados': table_data})

with open(r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\pas_tables.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('Salvo em pas_tables.json. Tabelas relevantes:')
keywords = ['acao', 'ação', 'objetivo', 'meta', 'indicador', 'responsavel', 'diretriz', 'programacao', 'programação']
for t in result:
    h = t['dados'][0] if t['dados'] else []
    header_str = ' | '.join(h)
    if any(kw in header_str.lower() for kw in keywords):
        print(f"  Tabela {t['tabela']} ({t['linhas']} linhas): {header_str[:120]}")
