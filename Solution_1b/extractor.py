class SubsectionExtractor:
    def extract(self, ranked_sections):
        extracted = []

        for section in ranked_sections:
            document = section.get("document")
            section_title = section.get("section_title")
            page = section.get("page_number")

            if not all([document, section_title, page is not None]):
                print(f"[WARNING] Skipping malformed section: {section}")
                continue

            refined_text = (
                f"To understand '{section_title}', ensure you review all interactive elements, "
                f"tools, and tasks covered in that section."
            )

            extracted.append({
                "document": document,
                "refined_text": refined_text,
                "page_number": page
            })

        return extracted
