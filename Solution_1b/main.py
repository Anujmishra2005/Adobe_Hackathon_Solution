import os
import json
import datetime
from processor import DocumentProcessor
from ranker import SectionRanker
from extractor import SubsectionExtractor


def process_collection(collection_path, output_path):
    input_json = os.path.join(collection_path, "challenge1b_input.json")
    with open(input_json, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    pdf_dir = os.path.join(collection_path, "PDFs")
    documents = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

    print("[INFO] Processing PDFs in:", pdf_dir)

    processor = DocumentProcessor()
    doc_sections = processor.extract_sections(documents)

    ranker = SectionRanker(metadata)
    ranked_sections = ranker.rank_sections(doc_sections)

    extractor = SubsectionExtractor()
    subsections = extractor.extract(ranked_sections)

    output_json = {
        "metadata": {
            "input_documents": [os.path.basename(doc) for doc in documents],
            "persona": metadata.get("persona", ""),
            "job": metadata.get("job", ""),
            "processing_timestamp": datetime.datetime.now().isoformat()
        },
        "extracted_sections": ranked_sections,
        "subsection_analysis": subsections
    }

    output_dir = os.path.join(output_path, os.path.basename(collection_path))
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, "challenge1b_output.json")
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(output_json, f, indent=2)
    print("[SUCCESS] Output written to:", output_file_path)


def main():
    base_input = "../Challenge_1b"
    base_output = "outputs_generated"
    os.makedirs(base_output, exist_ok=True)

    for collection in os.listdir(base_input):
        collection_path = os.path.join(base_input, collection)
        if os.path.isdir(collection_path):
            print(f"\n[COLLECTION] {collection}")
            process_collection(collection_path, base_output)


if __name__ == '__main__':
    main()
