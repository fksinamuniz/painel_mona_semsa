import json
import re
import math

with open("extracted_tables.json", "r", encoding="utf-8") as f:
    data = json.load(f)

metas = []
num_pattern = re.compile(r'^(\d+)\.\d+\.\d+$')

for row in data:
    if not isinstance(row, list) or len(row) < 13:
        continue
    
    num = str(row[0]).strip()
    match = num_pattern.match(num)
    if not match:
        continue
        
    d = match.group(1)
    desc = str(row[1]).replace("\n", " ").replace("  ", " ").strip() if row[1] else ""
    ind = str(row[2]).replace("\n", " ").replace("  ", " ").strip() if row[2] else ""
    
    # fix squished words with a simple heuristic if needed, but usually it's fine
    
    un = str(row[7]).replace("\n", " ").strip() if row[7] else str(row[5]).replace("\n", " ").strip()
    if un == "None": un = ""
    
    def clean_val(v):
        if not v or v == "None": return "0"
        v = str(v).upper().replace("\n", "").strip()
        if "S/I" in v or "SI" in v or v == "-": return "0"
        return v
        
    m2026 = clean_val(row[9])
    m2027 = clean_val(row[10])
    m2028 = clean_val(row[11])
    m2029 = clean_val(row[12])
    
    metas.append({
        "d": d,
        "num": num,
        "desc": desc,
        "ind": ind,
        "un": un,
        "m2026": m2026,
        "m2027": m2027,
        "m2028": m2028,
        "m2029": m2029
    })

# Remove duplicates if any (due to page breaks duplicating headers sometimes)
unique_metas = {m["num"]: m for m in metas}.values()

ts_content = "export const METAS = [\n"
for m in unique_metas:
    ts_content += f"  {json.dumps(m, ensure_ascii=False)},\n"
ts_content += "];\n"

# Update Vite project
with open(r"C:\Users\frank.muniz\Downloads\monitoramento\src\data\metas.ts", "w", encoding="utf-8") as f:
    f.write(ts_content)

# Also update Next.js copy just in case we need it locally
with open(r"C:\Users\frank.muniz\Desktop\WebScraping\WebScrapingAntigravity\src\lib\metas.ts", "w", encoding="utf-8") as f:
    f.write(ts_content)

print(f"Extracted {len(unique_metas)} unique metas and updated both metas.ts files.")
