import os
import json

input_dir = "HASIL_JSON_RJP"
output_txt_dir = "HASIL_BERSIH_TXT"
output_jsonl_dir = "HASIL_BERSIH_JSONL"

os.makedirs(output_txt_dir, exist_ok=True)
os.makedirs(output_jsonl_dir, exist_ok=True)

#label penting yang diambil
allowed_labels = ["text", "section_header", "title", "heading"]

# Nentuin ada di kolom kiri atau kanan berdasarkan posisi l (left)
# if l < 280 -> brt kolom kiri, sisanya kolom kanan
column_split_threshold = 280  

for root, _, files in os.walk(input_dir):
    for file in files:
        if not file.endswith(".json"):
            continue

        full_path = os.path.join(root, file)
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # list kosong untuk menyimpan teks kolom kiri dan kanan
        left_col = []
        right_col = []

        #ambil dan filter teks yang valid
        for text_obj in data.get("texts", []):
            label = text_obj.get("label", "").lower()
            text = text_obj.get("text", "").strip()
            prov = text_obj.get("prov", [{}])[0]
            bbox = prov.get("bbox", {})
            charspan = prov.get("charspan", [])
            l_pos = bbox.get("l", 0)

            if label in allowed_labels and len(text) > 2 and not text.lower().startswith("halaman"):
                entry = {
                    "filename": file,
                    "label": label,
                    "bbox": bbox,
                    "charspan": charspan,
                    "text": text
                }

                #berdasarkan posisi (l_pos) -> dimasukkan ke left_col atau right_col
                if l_pos < column_split_threshold:
                    left_col.append(entry)
                else:
                    right_col.append(entry)

        # Sort per kolom berdasarkan posisi vertikal dari atas ke bawah (t descending)
        # masalah e ada teks yang kek baca e dari kiri ke kanan tapi kebaca e ttp atas ke bawah (halaman 3 kalau gak salah)
        left_col.sort(key=lambda x: -x["bbox"].get("t", 0))
        right_col.sort(key=lambda x: -x["bbox"].get("t", 0))

        # Gabungin kiri dulu, lalu kanan
        entries = left_col + right_col

        # Simpan ke .txt
        cleaned_texts = [e["text"] for e in entries]
        output_txt_path = os.path.join(output_txt_dir, file.replace(".json", ".txt"))
        with open(output_txt_path, "w", encoding="utf-8") as out_txt:
            out_txt.write("\n\n".join(cleaned_texts))

        # Simpan ke .jsonl
        output_jsonl_path = os.path.join(output_jsonl_dir, file.replace(".json", ".jsonl"))
        with open(output_jsonl_path, "w", encoding="utf-8") as out_jsonl:
            for e in entries:
                json.dump(e, out_jsonl)
                out_jsonl.write("\n")

        print(f"✅ Done: {file} ➜ {output_txt_path} & {output_jsonl_path}")
