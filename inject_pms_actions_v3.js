(async function() {
    const STORAGE_KEY = 'pms26_html';
    const DATA_URL = '/actions_extracted_full.json';

    console.log("Iniciando a injeção de ações do PAS 2026...");

    try {
        // 1. Buscar os dados das ações
        const response = await fetch(DATA_URL);
        if (!response.ok) {
            throw new Error(`Erro ao carregar o arquivo JSON: ${response.statusText}`);
        }
        const actionsData = await response.json();
        const metaCount = Object.keys(actionsData).length;
        console.log(`Dados carregados: ${metaCount} metas encontradas no JSON.`);

        // 2. Recuperar dados do localStorage
        let rawData = localStorage.getItem(STORAGE_KEY);
        if (!rawData) {
            console.error(`Não foi possível encontrar a chave '${STORAGE_KEY}' no localStorage.`);
            console.log("DICA: Verifique se você está na página correta do painel e se os dados já foram carregados pelo sistema.");
            return;
        }

        let data = JSON.parse(rawData);
        let metas = Array.isArray(data) ? data : (data.metas || []);

        if (metas.length === 0) {
            console.error("Nenhuma meta encontrada no objeto recuperado do localStorage.");
            return;
        }

        // 3. Atualizar as metas com as ações correspondentes
        let updatedCount = 0;
        metas.forEach(meta => {
            // As chaves no JSON são strings como "1.1.1", "2.1.7", etc.
            if (meta.num && actionsData[meta.num]) {
                meta.acoes = actionsData[meta.num];
                updatedCount++;
            }
        });

        // 4. Salvar de volta no localStorage
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));

        console.log(`%cSucesso! ${updatedCount} metas foram atualizadas com as ações de 2026.`, "color: green; font-weight: bold;");
        console.log("Recarregue a página (F5) para aplicar as mudanças visuais.");

    } catch (error) {
        console.error("Erro durante a injeção:", error);
    }
})();
