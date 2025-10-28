import os
import pikepdf

BASE = "workspace/merge"
INPUT_DIR = os.path.join(BASE, "input")
OUTPUT_DIR = os.path.join(BASE, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_merge():
    print("=== MERGE PDF ===")
    files = sorted(f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf"))
    out = os.path.join(OUTPUT_DIR, "merged.pdf")
    pdf = pikepdf.Pdf.new()
    for f in files:
        src = pikepdf.open(os.path.join(INPUT_DIR, f))
        pdf.pages.extend(src.pages)
        src.close()
    pdf.save(out)
    print("✅ File digabung:", out)
