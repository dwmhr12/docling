# 🧾 Pipeline Docling PDF OCR & Text Extraction

Proyek ini digunakan untuk memproses file PDF halaman per halaman dengan bantuan [Docling](https://github.com/docling-ai/docling), lalu menyimpan hasil ekstraksi teks ke dalam format `.json`, `.jsonl`, dan `.txt`.

## 📂 Struktur Folder

- `PDF_SPLIT/` — Folder berisi file PDF yang telah dipecah per halaman.
- `HASIL_JSON_RJP/` — Hasil ekstraksi Docling dalam format `.json`.
- `HASIL_BERSIH_JSONL/` — Hasil pembersihan teks ke format `.jsonl`.
- `HASIL_BERSIH_TXT/` — Hasil pembersihan teks ke format `.txt`.

## 🛠️ Tools yang Digunakan

- Python 3.10+
- Docling CLI
- PaddleOCR (di bawah kap Docling)
- Git
- Linux terminal

## 🚀 Cara Jalankan

1. **Aktifkan virtual environment**  
   ```bash
   source venv/bin/activate
   ```

2. **Pisahkan PDF per halaman (jika belum):**  
   Gunakan `split_pdf.py`.

3. **Jalankan Docling untuk tiap halaman:**  
   ```bash
   python run_docling_per_page.py
   ```

4. **Bersihkan hasil output:**  
   ```bash
   python clean_docling_output.py
   ```

## 📝 Catatan

- Folder `venv/` tidak diikutkan ke Git (sudah diatur di `.gitignore`).
- Docling saat ini lebih optimal dijalankan di GPU.

