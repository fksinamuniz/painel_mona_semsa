(function() {
    const actionsData = ACTION_DATA_HERE;
    const STORAGE_KEY = 'pms26_html';
    
    let rawData = localStorage.getItem(STORAGE_KEY);
    if (!rawData) {
        console.error("Não foi possível encontrar a chave 'pms26_html' no localStorage. Verifique se você está na página correta do painel.");
        return;
    }

    let data = JSON.parse(rawData);
    
    // Supondo que a estrutura do 'data' tenha uma propriedade 'metas' que é uma lista de objetos
    // Se for apenas uma lista diretamente:
    let metas = Array.isArray(data) ? data : (data.metas || []);
    
    if (metas.length === 0) {
        console.error("Nenhuma meta encontrada no objeto recuperado do localStorage.");
        return;
    }

    let updatedCount = 0;
    metas.forEach(meta => {
        if (meta.num && actionsData[meta.num]) {
            meta.acoes = actionsData[meta.num];
            updatedCount++;
        }
    });

    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    console.log(`Sucesso! ${updatedCount} metas foram atualizadas com as ações de 2026.`);
    console.log("Recarregue a página (F5) para ver as mudanças.");
})();
