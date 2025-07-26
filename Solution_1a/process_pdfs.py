import os
import json
import fitz  # PyMuPDF
from langdetect import detect

# -------- CONFIG --------
INPUT_DIR = "../Challenge_1a/sample_dataset/pdfs/"
OUTPUT_DIR = "../Solution_1a/outputs_generated/"

# -------- LANGUAGE DETECTION --------
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# -------- TITLE DETECTION --------
def detect_title(doc):
    max_size = 0
    title = ""

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            for l in b.get("lines", []):
                spans = l.get("spans", [])
                text = " ".join(s["text"].strip() for s in spans if s["text"].strip())
                if not text or len(text) < 3 or all(c in "-•—_" for c in text.strip()):
                    continue
                for s in spans:
                    if s["size"] > max_size:
                        max_size = s["size"]
                        title = text
    return title.strip()

# -------- HEADING DETECTION --------
def detect_headings(doc, title_text):
    headings = []
    seen = set()

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            for l in b.get("lines", []):
                spans = l.get("spans", [])
                line_text = " ".join(s["text"].strip() for s in spans if s["text"].strip())

                if not line_text or len(line_text) < 3:
                    continue

                if line_text.lower().strip() == title_text.lower().strip():
                    continue
                if all(c in "-•—_" for c in line_text.strip()):
                    continue
                if line_text.strip() in seen:
                    continue
                seen.add(line_text.strip())

                font_sizes = [s["size"] for s in spans if s["text"].strip()]
                if not font_sizes:
                    continue

                avg_size = sum(font_sizes) / len(font_sizes)

                if avg_size > 16:
                    level = "H1"
                elif avg_size > 13:
                    level = "H2"
                elif avg_size > 11:
                    level = "H3"
                elif avg_size > 9:
                    level = "H4"
                else:
                    continue

                if len(line_text) < 4 or line_text.lower().startswith("rsvp"):
                    continue

                headings.append({
                    "level": level,
                    "text": line_text.strip(),
                    "page": page_num
                })

    return headings

# -------- PDF PROCESSING --------
def process_pdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    title = detect_title(doc)
    outline = detect_headings(doc, title)

    doc_lang = "unknown"
    if outline:
        joined_text = " ".join(h["text"] for h in outline[:5])
        doc_lang = detect_language(joined_text)

    output = {
        "title": title,
        "outline": outline,
        "document_language": doc_lang
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

# -------- MAIN --------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not os.path.exists(INPUT_DIR):
        print(f"❌ Input directory not found: {INPUT_DIR}")
        return

    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]
    if not files:
        print("⚠️ No PDF files found.")
        return

    for fname in files:
        input_pdf = os.path.join(INPUT_DIR, fname)
        output_json = os.path.join(OUTPUT_DIR, fname.replace(".pdf", ".json"))
        print(f"🔍 Processing: {fname}")
        process_pdf(input_pdf, output_json)

    print("\n✅ All PDFs processed.")

if __name__ == "__main__":
    main()
