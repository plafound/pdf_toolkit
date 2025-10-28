import os
import pikepdf

BASE = "workspace/split"
INPUT_DIR = os.path.join(BASE, "input")
OUTPUT_DIR = os.path.join(BASE, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_split():
    print("=== SPLIT PDF ===")
    for f in os.listdir(INPUT_DIR):
        if not f.endswith(".pdf"): continue
        src = os.path.join(INPUT_DIR, f)
        with pikepdf.open(src) as pdf:
            for i, p in enumerate(pdf.pages, 1):
                out = os.path.join(OUTPUT_DIR, f"{f[:-4]}_page{i}.pdf")
                new = pikepdf.Pdf.new(); new.pages.append(p)
                new.save(out)
        print("✅", f)
