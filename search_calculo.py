import pdfplumber
import os

pdf_file = 'DOMI-PMS FINAL 2026 A 2029.pdf'
if not os.path.exists(pdf_file):
    print(f"File {pdf_file} not found.")
    exit(1)

with pdfplumber.open(pdf_file) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text() or ''
        # Search for calculation-related terms
        terms = ['Cálculo', 'calculo', 'Fórmula', 'fórmula', 'Metodologia', 'metodologia']
        for term in terms:
            if term in text:
                print(f"FOUND '{term}' on page {i+1}")
                # Print a bit more context
                idx = text.find(term)
                print(f"Context: {text[max(0, idx-100):idx+500]}")
                print("-" * 50)
                # Don't break, keep looking for other terms or other occurrences on the same page
