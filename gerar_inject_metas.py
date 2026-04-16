# -*- coding: utf-8 -*-
"""
Le o metas.ts atualizado e gera um script JS para injetar
as 216 metas na chave pms26_html do localStorage do painel.
"""
import sys, json, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

METAS_TS = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\src\lib\metas.ts'
OUT_JS   = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\public\monitoramento\inject_metas.js'

# 1. Ler metas do metas.ts
with open(METAS_TS, encoding='utf-8') as f:
    ts_content = f.read()

match = re.search(r'export const METAS\s*=\s*(\[.*\])\s*;?\s*$', ts_content, re.DOTALL)
if not match:
    raise ValueError("Nao encontrou export const METAS")

metas = json.loads(match.group(1))
print(f"Metas lidas: {len(metas)}")

# 2. Ler o localStorage atual (pms26_html) se existir para preservar avaliações
# Como nao temos acesso direto ao localStorage aqui, vamos gerar estrutura completa
# preservando o schema que o painel espera.

# Schema esperado pelo painel: cada meta tem os campos do metas.ts
# mais possivelmente: status, avaliacoes_quad, etc.
# Vamos montar o payload completo

payload = {
    "metas": metas,
    "version": "2026-04-15",
    "total": len(metas)
}

payload_json = json.dumps(payload, ensure_ascii=False, separators=(',', ':'))

# 3. Gerar script JS que injeta os dados
js = f"""// Script de injecao das {len(metas)} metas do DOMI_PMS_2022-2029.xlsx
// Gerado automaticamente em 2026-04-15
(function() {{
  var data = {payload_json};
  
  // Tenta ler estrutura existente para preservar avaliacoes
  var existing = null;
  try {{
    var raw = localStorage.getItem('pms26_html');
    if (raw) existing = JSON.parse(raw);
  }} catch(e) {{}}

  if (existing && existing.metas) {{
    // Mapa de avaliacoes existentes por num
    var avalMap = {{}};
    existing.metas.forEach(function(m) {{
      if (m.status || m.avaliacoes || m.avaliacao_q1 || m.avaliacao_q2 || m.avaliacao_q3) {{
        avalMap[m.num] = m;
      }}
    }});
    
    // Mesclar: metas novas + preservar avaliacoes
    data.metas = data.metas.map(function(m) {{
      var old = avalMap[m.num];
      if (old) {{
        return Object.assign({{}}, m, {{
          status: old.status || m.status,
          avaliacoes: old.avaliacoes || m.avaliacoes,
          avaliacao_q1: old.avaliacao_q1,
          avaliacao_q2: old.avaliacao_q2,
          avaliacao_q3: old.avaliacao_q3,
          resultado_q1: old.resultado_q1,
          resultado_q2: old.resultado_q2,
          resultado_q3: old.resultado_q3,
          observacoes: old.observacoes
        }});
      }}
      return m;
    }});
  }}

  localStorage.setItem('pms26_html', JSON.stringify(data));
  console.log('[PMS] Injecao concluida: ' + data.metas.length + ' metas');
  alert('Metas atualizadas: ' + data.metas.length + ' metas carregadas. Recarregue a pagina.');
}})();
"""

with open(OUT_JS, 'w', encoding='utf-8') as f:
    f.write(js)

print(f"Script gerado: {OUT_JS}")
print("Abra o console do navegador no painel e cole o conteudo do arquivo inject_metas.js")
print("Ou acesse: http://10.132.208.238:8080/monitoramento/inject_metas.js")
