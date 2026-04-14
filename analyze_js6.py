import re

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Procura estruturas de dados de metas - arrays de objetos
# O painel de monitoramento provavelmente tem objetos tipo {id, num, diretriz, objetivo, meta, indicador, acoes:[]}
patterns = [
    r'\{num:\d+',
    r'\{id:\d+',
    r'diretriz:"[^"]{10,}',
    r'objetivo:"[^"]{10,}',
]
for pat in patterns:
    matches = list(re.finditer(pat, content))
    if matches:
        m = matches[0]
        idx = m.start()
        print(f"Pattern '{pat}' encontrado {len(matches)} vezes. Primeiro:")
        print(content[idx:idx+600])
        print("---")
