import pdfplumber
import json

path = r"C:\Users\frank.muniz\Desktop\WebScraping\WebScrapingAntigravity\DOMI-PMS FINAL 2026 A 2029.pdf"

tables_data = []
try:
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables_data.extend(table)
    
    with open("extracted_tables.json", "w", encoding="utf-8") as f:
        json.dump(tables_data, f, ensure_ascii=False, indent=2)
except Exception as e:
    with open("extracted_tables.json", "w", encoding="utf-8") as f:
        json.dump({"error": str(e)}, f)
