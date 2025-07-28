class SectionRanker:
    def __init__(self, metadata):
        self.persona = metadata["persona"].lower()
        self.job = metadata["job"].lower()

    def rank_sections(self, sections):
        for section in sections:
            score = 0
            text = section['section_title'].lower()
            if any(keyword in text for keyword in self.persona.split()):
                score += 5
            if any(keyword in text for keyword in self.job.split()):
                score += 10
            if "introduction" in text or "summary" in text:
                score += 3
            score += section['font_size'] / 10.0
            section['importance_rank'] = round(score, 2)
        sections = sorted(sections, key=lambda x: x['importance_rank'], reverse=True)
        return sections[:10]
