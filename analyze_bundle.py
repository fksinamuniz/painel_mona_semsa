import re

path = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\public\monitoramento\assets\index-xH-p0FqE.js'
content = open(path, encoding='utf-8', errors='replace').read()

get_keys = re.findall(r'getItem\(["\']([^"\']+)["\']', content)
set_keys = re.findall(r'setItem\(["\']([^"\']+)["\']', content)
num_count = content.count('"num"')

print("getItem keys:", set(get_keys))
print("setItem keys:", set(set_keys))
print("Ocorrencias de num:", num_count)
print("Tamanho JS:", len(content), "chars")
