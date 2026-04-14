import pdfplumber
import json
import re

path = r'C:\Users\frank.muniz\Desktop\Painel PMS Mona\PMS Mona\PAS 2026 _Ações.pdf'

def get_clean_text(cells):
    if not cells: return ""
    return " ".join([str(c).strip() for c in cells if c and str(c).strip()]).strip()

def extract_actions():
    metas_actions = {}
    current_meta = None
    last_action_index = -1
    
    meta_pattern = re.compile(r'^\d+\.\d+\.\d+$')
    action_pattern = re.compile(r'Ação\s*N[°º]\s*(\d+)', re.IGNORECASE)

    with pdfplumber.open(path) as pdf:
        for page_idx, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    row_text = [str(c).strip() if c else "" for c in row]
                    
                    # Check if this row defines a new meta
                    found_meta = None
                    for cell in row_text:
                        if meta_pattern.match(cell):
                            found_meta = cell
                            break
                    
                    if found_meta:
                        current_meta = found_meta
                        if current_meta not in metas_actions:
                            metas_actions[current_meta] = []
                        last_action_index = -1
                        continue

                    if not current_meta:
                        continue

                    # Check if this row defines a new action
                    found_action_match = None
                    action_cell_idx = -1
                    for idx, cell in enumerate(row_text):
                        match = action_pattern.search(cell)
                        if match:
                            found_action_match = match
                            action_cell_idx = idx
                            break
                    
                    if found_action_match:
                        # Extract description from the rest of the row
                        desc_parts = []
                        for idx, cell in enumerate(row_text):
                            if idx != action_cell_idx and cell:
                                desc_parts.append(cell)
                        
                        desc = " ".join(desc_parts).strip()
                        if desc:
                            metas_actions[current_meta].append(desc)
                            last_action_index = len(metas_actions[current_meta]) - 1
                    else:
                        # Possibly a continuation of the previous action description
                        # Only if it's not a header or another meta
                        clean_row = get_clean_text(row_text)
                        if last_action_index != -1 and clean_row and not any(kw in clean_row.lower() for kw in ["diretriz", "objetivo", "meta", "indicador"]):
                            # Append to last action
                            metas_actions[current_meta][last_action_index] += " " + clean_row

    # Clean up whitespace and duplicates
    discard_phrases = [
        "número absoluto", "percentual", "taxa", "razão", "sim/não", "dias", "minutos",
        "Meta do PMS", "2026 a 2029", "Linha de Base", "Indicador de Meta", "Unidade de medida",
        "Valor da linha de base", "Ano 2024", "Ano 2025", "Janeiro", "Fevereiro", "Março"
    ]
    
    final_metas = {}
    for meta, actions in metas_actions.items():
        unique_actions = []
        for a in actions:
            clean_a = a
            for phr in discard_phrases:
                # Remove phrase if it appears at the end or surrounded by noise
                clean_a = re.sub(re.escape(phr), "", clean_a, flags=re.IGNORECASE)
            
            clean_a = re.sub(r'\s+', ' ', clean_a).strip()
            # Remove trailing dots if they were part of a label
            clean_a = clean_a.rstrip('.')
            
            if len(clean_a) > 10 and clean_a not in unique_actions:
                unique_actions.append(clean_a)
        if unique_actions:
            final_metas[meta] = unique_actions

    return final_metas

if __name__ == "__main__":
    print("Starting extraction...")
    results = extract_actions()
    with open("actions_extracted.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Extraction complete. Found actions for {len(results)} metas.")
    print("Saved to actions_extracted.json")
