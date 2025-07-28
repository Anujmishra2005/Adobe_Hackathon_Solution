# ranker.py

import re

class SectionRanker:
    def __init__(self, metadata):
        persona_info = metadata.get("persona", {})
        job_info = metadata.get("job", "")

        self.persona_role = persona_info.get("role", "").lower()
        self.persona_focus = persona_info.get("focus", "").lower()
        self.job_to_be_done = job_info.lower()

    def _score_text(self, text):
        score = 0
        text_lower = text.lower()

        if self.persona_role:
            score += text_lower.count(self.persona_role)
        if self.persona_focus:
            score += text_lower.count(self.persona_focus)
        if self.job_to_be_done:
            score += text_lower.count(self.job_to_be_done)

        return score

    def rank_sections(self, extracted_sections):
        scored = []
        for section in extracted_sections:
            text = section.get("text")
            if not text:
                continue  # Skip malformed sections

            score = self._score_text(text)
            section["score"] = score
            scored.append(section)

        # Sort sections based on score (higher is more relevant)
        ranked_sections = sorted(scored, key=lambda x: x["score"], reverse=True)

        # Assign importance rank based on order
        for i, section in enumerate(ranked_sections):
            section["importance_rank"] = i + 1
            section.pop("score", None)

        return ranked_sections

    def rank_subsections(self, section_texts):
        refined = []
        for section in section_texts:
            text = section.get("text")
            if not text:
                continue

            sentences = re.split(r'(?<=[.?!])\s+', text)
            for sentence in sentences:
                score = self._score_text(sentence)
                if score > 0:
                    refined.append({
                        "document": section.get("document", ""),
                        "text": sentence.strip(),
                        "page_number": section.get("page", 0),
                        "score": score
                    })

        # Sort refined text by relevance
        refined_sorted = sorted(refined, key=lambda x: x["score"], reverse=True)
        for item in refined_sorted:
            item.pop("score", None)

        return refined_sorted
