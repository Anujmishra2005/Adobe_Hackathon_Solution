# 📄 Solution_1a — Document Title and Heading Extraction

This repository contains the solution for **Challenge_1a** of the Adobe Hackathon, focusing on extracting structured information from PDF documents including the **title**, **outline/headings**, and **document language**.

---

## 🧠 Objective

To develop a Python-based system that:
- Automatically extracts the **main title** of the PDF document.
- Detects and classifies headings based on font size hierarchy (`H1`, `H2`, `H3`, etc.).
- Identifies the **language** of the document.
- Outputs a JSON file containing this structured information for each PDF.

---

## 🧩 Approach

### 🔍 Problem Understanding

The task required structured information extraction from unstructured PDF files, where headings and titles are not explicitly marked but are visually represented using font sizes and positioning.

### ⚙️ Solution Strategy

1. **Font Size-Based Hierarchy Detection**:
   - Font sizes are extracted across all pages.
   - The **largest repeated font** (excluding noisy tokens) is treated as the **title**.
   - Headings are classified into `H1`, `H2`, `H3`, etc., based on font size hierarchy.

2. **Text Block Grouping**:
   - Lines are grouped by coordinates and styling to detect clean and full heading lines.
   - Short, disjoint, or duplicate text fragments are filtered.

3. **Language Detection**:
   - Uses `langdetect` on sampled large text spans from the document.

4. **Noise Filtering**:
   - Skips text blocks with only symbols, whitespace, or less than 3 characters.
   - Deduplicates headings and avoids line-by-line fragments.

---

### 🧪 Benefits & Performance

| Metric            | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| ⏱️ **Speed**       | Fast parsing using PyMuPDF, low memory usage                                 |
| 🎯 **Accuracy**    | High precision in title and heading detection via font statistics            |
| 🔁 **Compatibility** | Works on most text-based PDFs; future support can be added for OCR input     |
| 🔌 **Extensibility** | JSON output makes it pluggable into other systems or indexing pipelines     |
| 💡 **Lightweight**  | No GPU, only CPU; lightweight dependencies                                  |

---

## 🗂️ Directory Structure

```
Adobe_Hackathon_Solution/
│
├── Challenge_1a/
│   └── sample_dataset/
│       └── pdfs/                # 📥 Input PDF files
│
├── Solution_1a/
│   ├── outputs_generated/       # 📤 Output JSON files
│   ├── process_pdfs.py          # 🚀 Main processing script
│   ├── requirements.txt         # 📦 Dependencies
│   └── README.md                # 📘 This file
```

---

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Solution_1a.git
cd Solution_1a
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
langdetect==1.0.9
```

---

## 🚀 How to Run

Ensure all input PDF files are placed in the following directory:

```
Challenge_1a/sample_dataset/pdfs/
```

Then execute the main script:

```bash
python process_pdfs.py
```

All outputs will be saved in:

```
Solution_1a/outputs_generated/
```

---

## 🧾 Output Format

Each output `.json` file will follow this structure:

```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Heading Text",
      "page": 0
    }
  ],
  "document_language": "en"
}
```

---

## ✅ Sample Output

```json
{
  "title": "Overview  Foundation Level Extensions",
  "outline": [
    {
      "level": "H1",
      "text": "Revision History",
      "page": 2
    },
    {
      "level": "H1",
      "text": "Table of Contents",
      "page": 3
    },
    {
      "level": "H2",
      "text": "2.1 Intended Audience",
      "page": 6
    }
  ],
  "document_language": "en"
}
```

---

## 🤝 Author

Developed by **Anuj Mishra** for the Adobe Hackathon 2025.

> 📬 Connect with me on [LinkedIn](https://www.linkedin.com/in/anujmishra05) or check out my [GitHub](https://github.com/Anujmishra2005)

---
