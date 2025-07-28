class SectionRanker:
    def __init__(self, persona, job):
        self.persona = persona.lower()
        self.job = job.lower()

    def _score_text(self, text):
        score = 0
        text_lower = text.lower()

        keywords = [
            "form", "fillable", "fill and sign", "onboarding", "compliance", "prepare form",
            "interactive", "signature", "e-signature", "create pdf", "convert", "send document",
            "cities", "things to do", "restaurants", "culture", "travel", "trip", "plan", "guide"
        ]
        for kw in keywords:
            if kw in text_lower:
                score += 3

        if any(word in text_lower for word in self.job.split()):
            score += 1.5

        if len(text.split()) <= 15:
            score += 1

        return score

    def rank_sections(self, doc_sections):
        scored = []
        for section in doc_sections:
            score = self._score_text(section.get("section_title", ""))
            section["score"] = score
            scored.append(section)

        ranked = sorted(scored, key=lambda x: x["score"], reverse=True)

        for i, section in enumerate(ranked):
            section["importance_rank"] = i + 1
            section.pop("score", None)

        return ranked[:5]
