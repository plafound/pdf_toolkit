import os
import pikepdf

BASE = "workspace/rotate"
INPUT_DIR = os.path.join(BASE, "input")
OUTPUT_DIR = os.path.join(BASE, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_rotate():
    print("=== ROTATE PDF ===")
    deg = int(input("Derajat rotasi (90/180/270): ") or "90")
    for f in os.listdir(INPUT_DIR):
        if not f.endswith(".pdf"): continue
        inp, outp = os.path.join(INPUT_DIR, f), os.path.join(OUTPUT_DIR, f)
        with pikepdf.open(inp) as pdf:
            for p in pdf.pages:
                p.Rotate = (p.obj.get("/Rotate") or 0 + deg) % 360
            pdf.save(outp)
        print("✅", f)