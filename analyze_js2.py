import re

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Procura por padrao de objetos com 'diretriz' ou 'acoes'
for term in ['diretriz', 'acoes', 'Diretriz', 'DIRETRIZ']:
    for m in re.finditer(re.escape(term), content, re.IGNORECASE):
        idx = m.start()
        snippet = content[max(0, idx-200):idx+400].replace('\n', ' ')
        print(f'--- "{term}" at {idx} ---')
        print(snippet)
        print()
