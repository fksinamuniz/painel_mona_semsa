const fs = require('fs');

const oldContent = fs.readFileSync('./src/lib/metas.ts', 'utf8');
let evalString = oldContent.replace(/export const METAS =/g, 'var METAS =');
// A quick eval context
// To safely get METAS:
const script = `
  ${evalString}
  function getMetas() { return METAS; }
  getMetas();
`;
const legacyMetas = eval(script);

const legacyDict = {};
legacyMetas.forEach(m => { legacyDict[m.num] = m; });

const pdfData = JSON.parse(fs.readFileSync('extracted_tables.json', 'utf8'));
const newMetas = [];
const numPattern = /^(\d+)\.\d+\.\d+$/;

for (const row of pdfData) {
  if (!Array.isArray(row) || row.length < 13) continue;
  const num = String(row[0] || '').trim();
  const match = num.match(numPattern);
  if (!match) continue;

  const d = match[1];
  let desc = String(row[1] || '').replace(/\n/g, ' ').replace(/\s+/g, ' ').trim();
  let ind = String(row[2] || '').replace(/\n/g, ' ').replace(/\s+/g, ' ').trim();
  let un = String(row[7] || '').replace(/\n/g, ' ').trim();
  if(!un || un === 'None') un = String(row[5] || '').replace(/\n/g, ' ').trim();

  if (legacyDict[num]) {
      if (desc.length > 0) desc = legacyDict[num].desc;
      if (ind.length > 0) ind = legacyDict[num].ind;
      if (un.length > 0 && un !== "None") un = legacyDict[num].un;
  }

  const cleanVal = (v) => {
    if (!v || v === 'None' || v === 'null') return '0';
    let strV = String(v).toUpperCase().replace(/\n/g, '').trim();
    if (strV.includes('S/I') || strV.includes('SI') || strV === '-') return '0';
    return strV;
  };

  newMetas.push({
    d, num,
    desc, ind, un,
    m2026: cleanVal(row[9]),
    m2027: cleanVal(row[10]),
    m2028: cleanVal(row[11]),
    m2029: cleanVal(row[12])
  });
}

const uniqueDict = {};
newMetas.forEach(m => { uniqueDict[m.num] = m; });
const result = Object.values(uniqueDict);

const tsContent = `export const METAS = ${JSON.stringify(result, null, 2)};\n`;

fs.writeFileSync('C:/Users/frank.muniz/Downloads/monitoramento/src/data/metas.ts', tsContent, 'utf8');
fs.writeFileSync('C:/Users/frank.muniz/Desktop/WebScraping/WebScrapingAntigravity/src/lib/metas.ts', tsContent, 'utf8');

console.log(`Extracted ${result.length} metas and gracefully merged with legacy DOMI descriptions!`);
