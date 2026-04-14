import pdfplumber
import json
import re

path = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\PAS 2026 _Ações.pdf'

def extract_all_tables():
    all_data = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for j, table in enumerate(tables):
                all_data.append({
                    "page": i + 1,
                    "table_index": j,
                    "rows": table
                })
    
    with open("debug_all_tables.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(all_data)} tables to debug_all_tables.json")

if __name__ == "__main__":
    extract_all_tables()
