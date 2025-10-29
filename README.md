# 🧰 PDF Toolkit (Terminal Edition)

Aplikasi berbasis Python untuk mengolah file PDF secara **offline** lewat terminal.  
Dapat dijalankan di **Linux dan Windows (via PyInstaller)**.  
Dirancang modular — setiap fitur punya folder kerja (workspace) sendiri.

---

## 🚀 Fitur Utama
- ✅ **Merge PDF** – Gabungkan beberapa file menjadi satu.
- ✅ **Split PDF** – Pisahkan halaman tertentu.
- ✅ **Watermark PDF** – Tambahkan watermark otomatis ke seluruh halaman.
- ✅ **Compress PDF** – Kompres ukuran PDF (1–9 level).
- ✅ **Rotate PDF** – Putar halaman.
- ✅ **Convert PDF ↔ Image / Word / Excel** (dengan OCR Indonesia & Inggris).


---

## 🛠️ Instalasi

### 1️⃣ Clone repository
```bash
git clone https://github.com/plafound/pdf_toolkit.git
cd pdf_toolkit
```
### 2️⃣ Buat virtual environment
````bash
python3 -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows
````
### 3️⃣ Install dependensi
````bash
pip install -r requirements.txt
````


🧠 Dependensi Tambahan (Linux)
````bash
Pastikan kamu menginstal:

sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ind pandoc texlive-latex-base
````
### 3️⃣ Buat Folder Workspace
````bash
mkdir workspace
mkdir -p workspace/compress/{input,output} workspace/convert/{input,output} workspace/merge/{input,output} workspace/rotate/{input,output} workspace/split/{input,output} workspace/watermark/{input,output,template}
````

▶️ Cara Menjalankan
````bash
python main.py
````

Akan muncul menu utama seperti:

=== PDF TOOLKIT ===
1. Merge PDF
2. Split PDF
3. Watermark PDF
4. Compress PDF
5. Rotate PDF
6. Convert PDF (Image/Word/Excel)
0. Keluar

## 🧩 Konversi ke EXE (Windows)

Jika ingin membuat versi portable:
````bash

pyinstaller --onefile main.py
````

Hasilnya akan ada di folder dist/.

## 💡 Catatan

Semua input/output disimpan di folder workspace/ masing-masing modul.

OCR mendukung bahasa Indonesia dan Inggris.

Kompresi PDF bekerja optimal untuk file hasil scan.

---
