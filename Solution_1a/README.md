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

## 🗂️ Directory Structure

```
Adobe_Hackathon_Solution/
│
├── Challenge_1a/
│   └── sample_dataset/
│       └── pdfs/                 # 📥 Input PDF files
│
├── Solution_1a/
│   ├── outputs_generated/        # 📤 Output JSON files
│   ├── process_pdfs.py           # 🚀 Main processing script
│   ├── requirements.txt          # 📦 Dependencies
│   └── README.md                 # 📘 This file
```

---

## 🔧 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/Solution_1a.git
cd Solution_1a
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate    # On Windows
source .venv/bin/activate   # On Mac/Linux
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

---

## 📌 Requirements

```
PyMuPDF==1.23.6
langdetect==1.0.9
```

---

## 🚀 How to Run

1. Place all input PDF files in the following directory:

```
Challenge_1a/sample_dataset/pdfs/
```

2. Then execute the script:

```bash
python process_pdfs.py
```

3. All JSON outputs will be saved to:

```
Solution_1a/outputs_generated/
```

---

## 🧾 Output Format

Each output JSON file will have the following structure:

```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Heading Text",
      "page": 0
    },
    ...
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
      "level": "H2",
      "text": "2.1 Intended Audience",
      "page": 6
    }
  ],
  "document_language": "en"
}
```

---

## 📬 Contact

For any queries, please feel free to reach out:

- GitHub: [Anuj Mishra](https://github.com/Anujmishra2005)
- LinkedIn: [Anuj Mishra](https://www.linkedin.com/in/anujmishra05/)
