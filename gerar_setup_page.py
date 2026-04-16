import sys, json, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

METAS_TS = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\src\lib\metas.ts'
OUT_HTML  = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\public\monitoramento\setup.html'

with open(METAS_TS, encoding='utf-8') as f:
    ts_content = f.read()

match = re.search(r'export const METAS\s*=\s*(\[.*\])\s*;?\s*$', ts_content, re.DOTALL)
metas = json.loads(match.group(1))
print(f"Metas: {len(metas)}")

payload_json = json.dumps({"metas": metas, "version": "2026-04-15", "total": len(metas)}, ensure_ascii=False, separators=(',', ':'))

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Atualizar Metas — PMS 2026-2029</title>
  <style>
    body {{ font-family: system-ui, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; background: #f0f4f8; color: #1e293b; }}
    .card {{ background: white; border-radius: 16px; padding: 40px 48px; box-shadow: 0 4px 24px rgba(0,0,0,.1); max-width: 480px; width: 90%; text-align: center; }}
    h1 {{ font-size: 1.4rem; margin-bottom: 8px; }}
    p {{ color: #64748b; font-size: .95rem; margin-bottom: 24px; }}
    .badge {{ display: inline-block; background: #dbeafe; color: #1d4ed8; font-weight: 700; font-size: 2.5rem; border-radius: 12px; padding: 12px 28px; margin-bottom: 24px; }}
    .status {{ padding: 14px; border-radius: 10px; font-weight: 600; margin-top: 20px; font-size: .95rem; display: none; }}
    .ok {{ background: #dcfce7; color: #166534; display: block; }}
    .err {{ background: #fee2e2; color: #991b1b; display: block; }}
    button {{ background: #2563eb; color: white; border: none; border-radius: 10px; padding: 14px 32px; font-size: 1rem; font-weight: 700; cursor: pointer; transition: background .2s; }}
    button:hover {{ background: #1d4ed8; }}
    button:disabled {{ background: #94a3b8; cursor: default; }}
    a {{ display: inline-block; margin-top: 16px; color: #2563eb; font-weight: 600; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge" id="count">{len(metas)}</div>
    <h1>Atualizar Metas do Painel PMS</h1>
    <p>Clique no botão abaixo para carregar as <strong>{len(metas)} metas</strong> do DOMI PMS 2026–2029 no painel de monitoramento.</p>
    <button id="btn" onclick="injetar()">&#9654; Atualizar Agora</button>
    <div class="status ok" id="ok">✅ {len(metas)} metas atualizadas com sucesso!</div>
    <div class="status err" id="err">❌ Erro ao salvar. Verifique o console.</div>
    <br>
    <a href="/monitoramento/index.html">&#8592; Ir para o Painel</a>
  </div>
  <script>
    var DATA = {payload_json};

    function injetar() {{
      try {{
        var btn = document.getElementById('btn');
        btn.disabled = true;
        btn.textContent = 'Atualizando...';

        // Preservar avaliacoes existentes
        var existing = null;
        try {{
          var raw = localStorage.getItem('pms26_html');
          if (raw) existing = JSON.parse(raw);
        }} catch(e) {{}}

        if (existing && existing.metas) {{
          var avalMap = {{}};
          existing.metas.forEach(function(m) {{
            avalMap[m.num] = m;
          }});
          DATA.metas = DATA.metas.map(function(m) {{
            var old = avalMap[m.num];
            if (!old) return m;
            var merged = Object.assign({{}}, m);
            ['status','avaliacoes','avaliacao_q1','avaliacao_q2','avaliacao_q3',
             'resultado_q1','resultado_q2','resultado_q3','observacoes'].forEach(function(k) {{
              if (old[k] !== undefined) merged[k] = old[k];
            }});
            return merged;
          }});
        }}

        localStorage.setItem('pms26_html', JSON.stringify(DATA));
        document.getElementById('ok').style.display = 'block';
        btn.textContent = '✓ Concluído';
        setTimeout(function() {{
          window.location.href = '/monitoramento/index.html';
        }}, 1800);
      }} catch(e) {{
        document.getElementById('err').textContent = '❌ Erro: ' + e.message;
        document.getElementById('err').style.display = 'block';
        document.getElementById('btn').disabled = false;
        document.getElementById('btn').textContent = 'Tentar Novamente';
      }}
    }}
  </script>
</body>
</html>"""

with open(OUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print("Setup page criada:", OUT_HTML)
print("Acesse: http://10.132.208.238:8080/monitoramento/setup.html")
