from PyPDF2 import PdfReader, PdfWriter
import os

input_pdf_path = "PDF_ATURAN_HC/PERDIR-2022.0030-Kebijakan Strategis Human Experience Management System (HXMS).pdf"
output_dir = "PDF_SPLIT"
os.makedirs(output_dir, exist_ok=True)

reader = PdfReader(input_pdf_path)
for i in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[i])

    output_path = os.path.join(output_dir, f"halaman_{i+1}.pdf")
    with open(output_path, "wb") as f:
        writer.write(f)

print("✅ PDF berhasil di-split per halaman.")
