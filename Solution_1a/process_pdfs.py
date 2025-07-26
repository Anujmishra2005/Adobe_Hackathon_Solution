# ---------------------------- IMPORTS ----------------------------
import os
import json
import difflib
from langdetect import detect
import fitz  # PyMuPDF

# ---------------------------- CONFIG ----------------------------
PDF_DIR = "../Challenge_1a/sample_dataset/pdfs"
OUT_DIR = "../Challenge_1a/sample_dataset/outputs"
SCHEMA_PATH = "../Challenge_1a/sample_dataset/schema/output_schema.json"

# ---------------------------- LANGUAGE DETECTION (BONUS) ----------------------------
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# ---------------------------- SIMILARITY MATCHING ----------------------------
def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

# ---------------------------- TOC MATCHING ----------------------------
def match_toc(doc, headings):
    try:
        toc = doc.get_toc()
        matched = []
        for level, title, page in toc:
            for heading in headings:
                if similar(title.lower(), heading["text"].lower()) > 0.6:
                    matched.append({
                        "title": heading["text"],
                        "page": heading["page"]
                    })
        return matched
    except Exception:
        return []

# ---------------------------- TITLE DETECTION ----------------------------
def detect_headings(doc):
    headings = []
    for i in range(len(doc)):
        blocks = doc[i].get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        if s["size"] > 12:  # Assume headings use larger font
                            headings.append({
                                "text": s["text"].strip(),
                                "page": i
                            })
    return headings

# ---------------------------- CONTENT EXTRACTION ----------------------------
def extract_content(doc, page_num):
    return doc[page_num].get_text()

# ---------------------------- JSON STRUCTURING ----------------------------
def build_output_json(headings, doc):
    output = {
        "language": "",
        "sections": []
    }

    language = detect_language(doc[0].get_text())
    output["language"] = language

    for h in headings:
        section = {
            "title": h["text"],
            "page": h["page"],
            "content": extract_content(doc, h["page"])
        }
        output["sections"].append(section)

    return output

# ---------------------------- MAIN PROCESSING ----------------------------
def process_pdf(file_path):
    file_name = os.path.basename(file_path)
    print(f"Processing: {file_name}")
    doc = fitz.open(file_path)

    headings = detect_headings(doc)
    toc_matched = match_toc(doc, headings)
    output_data = build_output_json(toc_matched or headings, doc)

    output_file = os.path.join(OUT_DIR, file_name.replace(".pdf", ".json"))
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

# ---------------------------- ENTRY POINT ----------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for fname in os.listdir(PDF_DIR):
        if fname.endswith(".pdf"):
            process_pdf(os.path.join(PDF_DIR, fname))

if __name__ == "__main__":
    main()