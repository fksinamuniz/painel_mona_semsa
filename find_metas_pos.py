# -*- coding: utf-8 -*-
"""
Encontra e exibe o contexto exato do array de metas no bundle.
"""
import sys, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BUNDLE = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\public\monitoramento\assets\index-xH-p0FqE.js'

with open(BUNDLE, encoding='utf-8', errors='replace') as f:
    bundle = f.read()

print(f"Bundle: {len(bundle)} chars")

# Procurar todas ocorrencias de "1.1.1" para encontrar o array real
import re as re2
for m in re2.finditer(r'1\.1\.1', bundle):
    pos = m.start()
    ctx = bundle[max(0, pos-100):pos+100]
    print(f"\nPos {pos}: {repr(ctx)}")
