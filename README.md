# 📘 Adobe India Hackathon 2025 — Connecting the Dots

Welcome to our submission for the **Adobe India Hackathon 2025** under the theme:

> **"Rethink Reading. Rediscover Knowledge."**

---

## 🧩 Challenge Overview

In the **Connecting the Dots** challenge, we were tasked with transforming static PDF documents into intelligent, context-aware companions. The goal is to **extract, understand, and present document knowledge** in ways that align with human understanding and specific user goals.

We submitted solutions for:

- ✅ **Challenge 1a**: Title & Heading Extraction
- ✅ **Challenge 1b**: Persona-Aware Section Relevance and Subsection Extraction

---

## 📂 Solutions Overview

### 🔹 [Solution 1a – Title & Heading Extraction](./Solution_1a/README.md)

📄 Extracts key structural metadata from raw PDFs:

- Detects the **main title** using font size hierarchy.
- Classifies headings into `H1`, `H2`, `H3`, etc.
- Detects **document language**.
- Outputs structured JSON for indexing or semantic parsing.

✅ Optimized for:
- Fast parsing using PyMuPDF
- Lightweight CPU execution
- Clean hierarchical output for outlines

🔗 [View Full README →](./Solution_1a/README.md)

---

### 🔹 [Solution 1b – Persona-Aware Section Extractor](./Solution_1b/README.md)

🧠 Intelligent system to recommend the most relevant sections from multiple PDFs:

- Extracts meaningful paragraphs from each page.
- Ranks based on **persona** and **job-to-be-done** using semantic + keyword scoring.
- Generates **subsection summaries** using heuristics.
- Removes noisy formatting like paths and Unicode artifacts.
- Outputs fully clean, structured JSON.

✅ Highlights:
- Modular (supports any persona or task)
- Runs in under 1 min per document collection
- Fully configurable & extendable
- No model dependencies — 100% rule-based and deterministic

🔗 [View Full README →](./Solution_1b/README.md)

---

## 📁 Directory Structure

```
Adobe_Hackathon_Solution/
├── Challenge_1a/                  # 📥 Input PDFs & structure for Task 1a
├── Challenge_1b/                  # 📥 Input collections for Task 1b
│
├── Solution_1a/                   # 🧠 Output & logic for Task 1a
│   ├── process_pdfs.py
│   ├── outputs_generated/
│   ├── README.md
│
├── Solution_1b/                   # 🧠 Output & logic for Task 1b
│   ├── main.py
│   ├── processor.py
│   ├── extractor.py
│   ├── ranker.py
│   ├── outputs_generated/
│   ├── approach_explanation.md
│   └── README.md
```

---

## 🚀 Speed, Accuracy, Extensibility

| Feature                | Challenge 1a                           | Challenge 1b                             |
|------------------------|----------------------------------------|------------------------------------------|
| 🧠 Approach            | Font statistics & language detection   | Heuristic + Semantic Ranking             |
| 🕒 Execution Time      | < 10s per PDF                          | ~60s per collection                      |
| 📦 Model Dependencies | None                                   | None                                     |
| ⚡ Accuracy            | High for font-based PDFs               | High for persona-task alignment          |
| 🔧 Hardware           | CPU-only                               | CPU-only                                 |
| 🧹 Clean Output        | Yes (JSON structured)                  | Yes (JSON with ranking and summaries)    |
| 🔌 Extensible Design   | Yes                                    | Yes (pluggable scoring logic)            |

---

## 👨‍💻 Developed By

**Anuj Mishra** — Adobe Hackathon 2025

- 🔗 [LinkedIn](https://www.linkedin.com/in/anujmishra05)
- 💻 [GitHub](https://github.com/Anujmishra2005)

---

## 💡 Final Thoughts

This submission reimagines PDFs as not just static files, but **interactive, intelligent documents** that adapt to the user's context.

Let’s not just read documents. Let’s **understand** them.

---
