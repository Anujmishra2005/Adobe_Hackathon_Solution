import fitz  # PyMuPDF

class DocumentProcessor:
    def extract_sections(self, pdf_paths):
        sections = []
        for pdf_path in pdf_paths:
            doc = fitz.open(pdf_path)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                blocks = page.get_text("dict")['blocks']
                for b in blocks:
                    if 'lines' not in b:
                        continue
                    for line in b['lines']:
                        text = " ".join([span['text'] for span in line['spans']]).strip()
                        if len(text) > 10 and text.isprintable():
                            font_size = max(span['size'] for span in line['spans'])
                            sections.append({
                                "document": pdf_path.split("/")[-1],
                                "page": page_num,
                                "section_title": text,
                                "font_size": font_size,
                                "text_block": text
                            })
        return sections
