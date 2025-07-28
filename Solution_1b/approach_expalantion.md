# Approach Explanation — Challenge 1B

## Overview

In this challenge, we aim to create a **persona-aware document summarizer**. Given a collection of PDFs, a persona definition, and a job-to-be-done, the system extracts relevant sections and sub-sections based on semantic relevance. The solution is built to handle diverse document domains, personas, and tasks.

---

## 🔍 Step-by-Step Methodology

### 1. PDF Parsing
We use `PyMuPDF` to extract:
- **Text** content
- **Headings** (based on font size and positioning)
- **Page number** and **title** metadata

### 2. Embedding-Based Relevance Scoring
We use `sentence-transformers` to convert:
- Job descriptions
- Section headings
- Paragraphs

...into semantic vectors and calculate similarity using cosine similarity. This allows for **context-aware matching**, rather than keyword matching.

### 3. Section & Sub-Section Ranking
- We score each section against the persona’s task vector.
- Top sections are assigned a `importance_rank` based on score.
- Within top sections, we extract sub-sections using sliding window summaries.

---

## ⚙️ Compatibility and Optimization

- ✅ Runs on **CPU** only (no GPU needed)
- ✅ Model size well within **1GB** (`MiniLM`)
- ✅ Processes **3–5 documents under 60 seconds**
- ✅ Output stored in structured JSON format

---

## 📈 Benefits

| Feature        | Benefit                                        |
|----------------|------------------------------------------------|
| Semantic Embeddings | High contextual accuracy across domains |
| Fast Inference | Fast processing using compact MiniLM model     |
| Generic Design | Adapts to any persona-task-document combo      |
| Lightweight    | Works on low-spec CPU machines                 |

---

## 🧪 Test Cases Verified

- Academic Research (Graph Neural Networks)
- Business Analysis (Annual Tech Reports)
- Educational Content (Organic Chemistry)

This modular, language-model-driven pipeline balances **speed**, **accuracy**, and **flexibility**.
