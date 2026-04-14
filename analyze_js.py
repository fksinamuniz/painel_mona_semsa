import re

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Busca por strings que parecem ser chaves de metas
search_terms = ['objetivo', 'diretriz', 'acoes', 'indicador', 'acao', 'meta', 'Meta', 'acaoId', 'objetivoId']
for term in search_terms:
    indices = [m.start() for m in re.finditer(re.escape(term), content, re.IGNORECASE)]
    if indices:
        print(f'\n"{term}" encontrado {len(indices)} vezes. Primeiro contexto:')
        idx = indices[0]
        snippet = content[max(0, idx-80):idx+200].replace('\n', ' ')
        print(f'  ...{snippet}...')
