import pdfplumber
import json

path = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\PAS 2026 _Ações.pdf'

def debug_pdf():
    with pdfplumber.open(path) as pdf:
        print(f"Total pages: {len(pdf.pages)}")
        # Inspect more pages
        for i in range(5, 15):
            page = pdf.pages[i]
            table = page.extract_table()
            if table:
                print(f"\n--- Page {i+1} Table ---")
                for row in table[:10]: # Print first 10 rows
                    print(row)
            else:
                text = page.extract_text()
                print(f"\n--- Page {i+1} Text (No table found) ---")
                print(text[:500] if text else "Empty page")

if __name__ == "__main__":
    debug_pdf()
