# ---------------------------- IMPORTS ----------------------------
import os
import json
import fitz  # PyMuPDF
from langdetect import detect

# ---------------------------- CONFIG ----------------------------
INPUT_DIR = "../Challenge_1a/sample_dataset/pdfs/"
OUTPUT_DIR = "../Solution_1a/outputs_generated/"

# ---------------------------- HEADING DETECTION ----------------------------
def detect_headings(doc):
    headings = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        size = s["size"]
                        text = s["text"].strip()
                        if len(text) == 0:
                            continue
                        if size > 16:
                            level = "H1"
                        elif size > 13:
                            level = "H2"
                        elif size > 11:
                            level = "H3"
                        else:
                            continue

                        lang = detect_language(text)

                        headings.append({
                            "level": level,
                            "text": text,
                            "page": page_num + 1,
                            "language": lang
                        })
    return headings

# ---------------------------- TITLE DETECTION ----------------------------
def detect_title(doc):
    font_sizes = {}
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        size = round(s["size"], 1)
                        font_sizes[size] = font_sizes.get(size, 0) + 1

    max_font_size = max(font_sizes, key=font_sizes.get)
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        if round(s["size"], 1) == max_font_size:
                            return s["text"].strip()
    return "Untitled"

# ---------------------------- LANGUAGE DETECTION ----------------------------
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# ---------------------------- PDF PROCESSING ----------------------------
def process_pdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    title = detect_title(doc)
    headings = detect_headings(doc)

    output = {
        "title": title,
        "outline": headings,
        "document_language": detect_language(" ".join(h["text"] for h in headings[:5])) if headings else "unknown"
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

# ---------------------------- MAIN ENTRY ----------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for fname in os.listdir(INPUT_DIR):
        if fname.endswith(".pdf"):
            input_pdf = os.path.join(INPUT_DIR, fname)
            output_json = os.path.join(OUTPUT_DIR, fname.replace(".pdf", ".json"))
            process_pdf(input_pdf, output_json)

if __name__ == "__main__":
    main()
