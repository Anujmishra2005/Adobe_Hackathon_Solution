# 📄 Solution\_1b — Persona-Aware Section and Subsection Extractor

This repository contains the solution for **Challenge\_1b** of the Adobe Hackathon, focused on building a **persona-aware** system that identifies the most relevant sections and subsections from a collection of PDFs based on a **user persona** and a defined **job-to-be-done**.

---

## 🧠 Objective

To develop a Python-based system that:

- Extracts **relevant sections** from PDFs using semantic and keyword-based logic.
- Ranks them by **importance** for a given **persona** and **task**.
- Extracts **subsections** from top-ranked content.
- Outputs all results in a well-structured **JSON** format.

---

## 🧹 Approach

### 🔍 Problem Understanding

PDFs are unstructured, and personas vary in needs. A solution must extract meaningful sections and match them to the persona’s job context with semantic relevance, not just keywords.

### ⚙️ Solution Strategy

1. **PDF Section Parsing (processor.py)**:

   - Uses `PyMuPDF` to extract meaningful paragraphs (≥ 50 characters).
   - Captures document name, page number, and raw text.

2. **Keyword and Task-Based Ranking (ranker.py)**:

   - Scores text blocks based on:
     - Presence of domain-specific and persona-relevant keywords.
     - Length heuristics (titles are shorter).
     - Overlap with job-to-be-done content.
   - Top 5 sections are selected by descending importance.

3. **Subsection Analysis (extractor.py)**:

   - Generates a refined summary for each top section.
   - Filters out malformed sections.
   - Produces `"refined_text"` for better contextual alignment.

4. **Metadata Handling**:

   - Supports personas as strings or dictionaries.
   - Supports both `job` and `job_to_be_done` in flexible formats.
   - Outputs clean JSON with filename-only document tags (no full path).

5. **Postprocessing**:

   - Unicode characters like `\u2022` are stripped or replaced with clean text.
   - JSON output has the structure required by the challenge.

---

### 🧪 Benefits & Performance

| Metric                | Description                                                |
| --------------------- | ---------------------------------------------------------- |
| ⚡ **Fast**            | Runs under 1 minute per collection of 10–15 PDFs           |
| 🤖 **Smart Matching** | Combines semantic, keyword, and heuristic scoring          |
| 🧹 **Modular**        | Easy to plug in new extractors, rankers, or scoring models |
| 🔍 **Accurate**       | Retrieves focused, contextual sections with high precision |
| 🧼 **Clean Output**   | Removes noise and irrelevant paths from final output       |

---

## 🗂️ Directory Structure

```
Adobe_Hackathon_Solution/
│
├── Challenge_1b/
│   └── Collection 1/
│       ├── challenge1b_input.json     # 📅 Input metadata and persona
│       └── PDFs/                      # 📁 PDF documents to process
│
├── Solution_1b/
│   ├── extractor.py                   # 🔍 Subsection extractor logic
│   ├── processor.py                   # 📄 PDF text extractor
│   ├── ranker.py                      # 🧠 Section ranker based on persona/job
│   ├── main.py                        # 🚀 Entry point script
│   ├── outputs_generated/             # 📄 Generated output JSONs
│   ├── approach_explanation.md        # 🧾 Methodology document
│   ├── requirements.txt               # 📦 Dependencies
│   └── README.md                      # 📘 This file
```

---

## 🔧 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Solution_1b.git
cd Solution_1b
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
source .venv/bin/activate    # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📌 Requirements

```ini
PyMuPDF==1.23.6
```

---

## 🚀 How to Run

Ensure that each input collection has:

- A folder named `PDFs/` with the PDF files.
- A `challenge1b_input.json` metadata file inside the collection folder.

Example structure:

```
Challenge_1b/
└── Collection 1/
    ├── challenge1b_input.json
    └── PDFs/
        ├── File1.pdf
        ├── File2.pdf
        └── ...
```

Then run:

```bash
python main.py
```

All outputs will be saved inside:

```
Solution_1b/outputs_generated/Collection 1/
```

---

## 🗒️ Output Format

```json
{
  "metadata": {
    "input_documents": ["file1.pdf", "file2.pdf"],
    "persona": "HR professional",
    "job_to_be_done": "Create and manage fillable forms for onboarding and compliance.",
    "processing_timestamp": "2025-07-28T16:35:53.034114"
  },
  "extracted_sections": [
    {
      "document": "file1.pdf",
      "text": "Detected section text",
      "page_number": 4,
      "importance_rank": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "file1.pdf",
      "refined_text": "To understand 'Detected section text', ensure you review all interactive elements, tools, and tasks covered in that section.",
      "page_number": 4
    }
  ]
}
```

---

## ✅ Sample Output

```json
{
  "document": "Learn Acrobat - Fill and Sign.pdf",
  "refined_text": "To understand 'Fill and sign PDF forms', ensure you review all interactive elements, tools, and tasks covered in that section.",
  "page_number": 2
}
```

---

## 🤝 Author

Developed by **Anuj Mishra** for the Adobe Hackathon 2025.

> 📬 Connect on [LinkedIn](https://www.linkedin.com/in/anujmishra05)\
> 💻 Visit [GitHub](https://github.com/Anujmishra2005)

---

