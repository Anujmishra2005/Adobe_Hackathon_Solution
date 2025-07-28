import fitz  # PyMuPDF
import os

class DocumentProcessor:
    def extract_sections(self, documents):
        results = []
        for doc_path in documents:
            doc = fitz.open(doc_path)
            for page_number in range(len(doc)):
                page = doc[page_number]
                blocks = page.get_text("dict")["blocks"]
                for block in blocks:
                    if "lines" in block:
                        text = " ".join([span["text"] for line in block["lines"] for span in line["spans"]])
                        if len(text.strip()) >= 50:
                            results.append({
                                "document": os.path.basename(doc_path),
                                "section_title": text.strip(),
                                "page_number": page_number
                            })
        return results
