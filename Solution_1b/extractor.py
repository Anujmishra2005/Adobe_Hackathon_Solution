class SubsectionExtractor:
    def extract(self, ranked_sections):
        refined = []
        for sec in ranked_sections:
            refined.append({
                "document": sec["document"],
                "refined_text": sec["text_block"][:300] + "..." if len(sec["text_block"]) > 300 else sec["text_block"],
                "page": sec["page"]
            })
        return refined
