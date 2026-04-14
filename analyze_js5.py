import re

with open(r'public/monitoramento/assets/index-xH-p0FqE.js', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Ver a estrutura geral do bundle - procura por arrays de metas definidas
# Pega o trecho do DIRETRIZ para entender a estrutura de dados
idx = content.upper().find('DIRETRIZ')
print(f"=== TRECHO DIRETRIZ (pos={idx}) ===")
print(content[max(0,idx-1000):idx+3000])
