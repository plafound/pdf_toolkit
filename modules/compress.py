import os
from pathlib import Path
from pikepdf import Pdf
from PIL import Image
import fitz  # PyMuPDF
import tempfile

def compress_images_in_pdf(input_path, output_path, level=5):
    """
    level 1 = kualitas tinggi (kompres sedikit)
    level 9 = kualitas rendah (kompres maksimal)
    """

    # Faktor kualitas
    quality = max(10, 100 - (level * 10))  # misal level 5 → kualitas 50%

    # Buka PDF sebagai gambar per halaman
    doc = fitz.open(input_path)
    temp_pdf = fitz.open()

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        pix = page.get_pixmap(dpi=150)  # render halaman ke gambar

        # Simpan ke gambar sementara
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_img:
            img_path = tmp_img.name
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(img_path, quality=quality, optimize=True)

        # Tambahkan ke PDF baru
        img_doc = fitz.open(img_path)
        rect = img_doc[0].rect
        pdfbytes = img_doc.convert_to_pdf()
        img_pdf = fitz.open("pdf", pdfbytes)
        page = temp_pdf.new_page(width=rect.width, height=rect.height)
        page.show_pdf_page(rect, img_pdf, 0)
        img_doc.close()
        os.remove(img_path)

    temp_pdf.save(output_path)
    temp_pdf.close()
    doc.close()


def run_compress():
    input_dir = Path("workspace/compress/input")
    output_dir = Path("workspace/compress/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        print("⚠️  Tidak ada file PDF di folder input.")
        return

    print("=== KOMPRESS PDF ===")
    print("Level kompresi (1 = ringan, 9 = maksimal): ", end="")
    try:
        level = int(input().strip())
        if not (1 <= level <= 9):
            raise ValueError
    except ValueError:
        print("❌ Level tidak valid. Gunakan angka 1–9.")
        return

    for file in pdf_files:
        outpath = output_dir / file.name
        print(f"🔧 Mengompres: {file.name} (level {level})...")
        try:
            compress_images_in_pdf(file, outpath, level)
            print(f"✅ {file.name} selesai → {outpath.name}")
        except Exception as e:
            print(f"❌ Gagal kompres {file.name}: {e}")

    input("\nTekan Enter untuk kembali ke menu utama...")
    os.system("clear")


if __name__ == "__main__":
    run_compress()
