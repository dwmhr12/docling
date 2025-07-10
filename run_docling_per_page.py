import os
import subprocess

# Folder input PDF per halaman
input_folder = "PDF_SPLIT"
# Folder hasil JSON output
output_folder = "HASIL_JSON"

# Pastikan folder output ada
os.makedirs(output_folder, exist_ok=True)

# Ambil semua file PDF
pdf_files = sorted([
    f for f in os.listdir(input_folder)
    if f.endswith(".pdf")
])

# Proses satu per satu
for file in pdf_files:
    print(f"🔄 Processing {file} ...")

    input_path = os.path.join(input_folder, file)

    # Buat folder output khusus untuk setiap file
    file_name = os.path.splitext(file)[0]
    output_path = os.path.join(output_folder, file_name)
    os.makedirs(output_path, exist_ok=True)

    # Jalankan docling CLI
    result = subprocess.run([
        "docling",
        input_path,
        "--to", "json",
        "--output", output_path,
        "--device", "cpu", 
        "--verbose"  # Menampilkan detail proses
    ], capture_output=True, text=True)

    # Tampilkan output proses
    print(result.stdout)
    print(result.stderr)

    # Cek apakah hasil json-nya ada
    json_files = [f for f in os.listdir(output_path) if f.endswith(".json")]
    if json_files:
        print(f"✅ JSON saved for {file}: {json_files}")
    else:
        print(f"❌ No JSON output found for {file}")

print("\n✅ Done processing all PDF files.")
