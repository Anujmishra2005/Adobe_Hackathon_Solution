import json
import os
from sklearn.metrics import precision_score, recall_score

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_headings(json_data):
    return set((h["page"], h["text"].strip().lower()) for h in json_data.get("outline", []))

def evaluate(pred_dir, truth_dir):
    files = [f for f in os.listdir(pred_dir) if f.endswith(".json")]
    all_preds, all_truths = [], []

    for fname in files:
        pred_path = os.path.join(pred_dir, fname)
        truth_path = os.path.join(truth_dir, fname)

        if not os.path.exists(truth_path):
            print(f"⚠️ Skipping {fname}: No ground truth available.")
            continue

        pred_data = load_json(pred_path)
        truth_data = load_json(truth_path)

        pred_headings = extract_headings(pred_data)
        truth_headings = extract_headings(truth_data)

        # Evaluate matches
        for h in truth_headings:
            all_truths.append(1)
            all_preds.append(1 if h in pred_headings else 0)

        for h in pred_headings:
            if h not in truth_headings:
                all_truths.append(0)
                all_preds.append(1)

    if not all_preds:
        print("⚠️ No matching files to evaluate.")
        return

    precision = precision_score(all_truths, all_preds)
    recall = recall_score(all_truths, all_preds)

    print(f"\n📊 Evaluation Report")
    print(f"Precision: {precision:.2f}")
    print(f"Recall:    {recall:.2f}")

if __name__ == "__main__":
    PRED_DIR = "../Challenge_1a/sample_dataset/outputs"
    TRUTH_DIR = "../Challenge_1a/sample_dataset/ground_truth"
    evaluate(PRED_DIR, TRUTH_DIR)
