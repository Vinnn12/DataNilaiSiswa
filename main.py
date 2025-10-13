import regex as re
from tabulate import tabulate
from data_siswa import data_siswa
from mata_pelajaran import mata_pelajaran
import csv

# Daftar untuk menyimpan data yang dihapus
delete_history = []

# ==========================
# FUNGSI MENCOBA LAGI
# ==========================
def tanya_lagi(pesan="Apakah Anda ingin mencoba lagi? (Y/N): "):
    while True:
        jawaban = input(pesan).strip().upper()
        if jawaban == "Y":
            return True
        elif jawaban == "N":
            return False
        else:
            print("⚠️ Pilih Y atau N saja.")

# ==========================
# FUNGSI PENGECEKAN ID SISWA
# ==========================
def cek_id_siswa(id_siswa, data_siswa):
    siswa_ditemukan = None

    for siswa in data_siswa:
        if siswa["studentId"] == id_siswa:
            siswa_ditemukan = siswa

    if not siswa_ditemukan:
        print("❌ Data Siswa Tidak Ditemukan!\n")
    else: 
        print(f"✅ Data Siswa Ditemukan: {siswa_ditemukan['nama_lengkap']}\n")

    return siswa_ditemukan

# ==========================
# FUNGSI INPUT NILAI MAPEL
# ==========================
def input_nilai_mata_pelajaran(siswa_ditemukan):
    print("Input Data Nilai Mata Pelajaran")
    print("-------------------------------")
    for pelajaran in mata_pelajaran:
        while True:
            nilai_input = input(f"Masukkan nilai {pelajaran}: ").strip()
            if not re.match(r"^\d+$", nilai_input):
                print("⚠️ Harus angka 0–100!\n")
                continue
            nilai = int(nilai_input)
            if 0 <= nilai <= 100:
                key = pelajaran.lower().replace(" ", "_")
                siswa_ditemukan["nilai"][key] = nilai
                break
            else:
                print("⚠️ Nilai harus antara 0–100!")

# ==========================
# FUNGSI UBAH NILAI MAPEL
# ==========================
def ubah_nilai_mata_pelajaran(siswa_ditemukan):
    while True:
        pilihan = input("Masukkan nomor pilihan: ").strip()
        if not pilihan.isdigit():
            print("⚠️ Harus angka.")
            continue
        pilihan = int(pilihan)

        if 1 <= pilihan <= len(mata_pelajaran):
            pelajaran = mata_pelajaran[pilihan - 1]
            key = pelajaran.lower().replace(" ", "_")
            while True:
                nilai_baru = input(f"Masukkan nilai baru untuk {pelajaran}: ").strip()
                if not re.match(r"^\d+$", nilai_baru):
                    print("⚠️ Harus angka 0–100!")
                    continue
                nilai_baru = int(nilai_baru)
                if 0 <= nilai_baru <= 100:
                    siswa_ditemukan["nilai"][key] = nilai_baru
                    print(f"✅ Nilai {pelajaran} berhasil diubah.")
                    return  
                else:
                    print("⚠️ Nilai harus antara 0–100!")
        elif pilihan == len(mata_pelajaran) + 1:
            print("Batal ubah nilai.")
            return
        else:
            print("⚠️ Pilihan tidak valid.")

# ==========================
# MENU 1 : FUNGSI INPUT NILAI SISWA 
# ==========================
def input_nilai_siswa(data_siswa):
    while True:
        print()
        print("Input Data Nilai Siswa")
        print("----------------------")
        # Input Student ID
        id_siswa = input("Masukkan Student ID Siswa: ").strip().upper()
        # Cek Input Student ID
        if not re.match(r"^[A-Z]{3}\d{3}$", id_siswa):
            print("⚠️ Format Student ID salah! Contoh yang benar: MUR001, GUR002.\n")
            continue
        # Cari siswa berdasarkan Student ID
        siswa_ditemukan = cek_id_siswa(id_siswa, data_siswa)
        # Jika tidak ditemukan, minta input ulang
        if not siswa_ditemukan:
            if tanya_lagi("\n🔁 Apakah Anda Ingin Mencoba Lagi? (Y/N): "):
                continue
            else:
                break
        
        nilai_siswa = siswa_ditemukan["nilai"]
        if any(nilai != 0 for nilai in nilai_siswa.values()):
            print("\nℹ️ Nilai siswa ini sudah pernah diisi sebelumnya:")
            tampilkan_nilai_siswa(siswa_ditemukan)

            while True:
                pilihan = input("\nApakah Anda ingin mengubah nilai yang sudah ada? (Y/N): ").strip().upper()
                if pilihan == "Y":
                    ubah_nilai_siswa(siswa_ditemukan)
                    break
                elif pilihan == "N":
                    print("❎ Tidak ada perubahan yang dilakukan.")
                    break
                else:
                    print("⚠️ Pilih Y atau N saja.")
        else:
            input_nilai_mata_pelajaran(siswa_ditemukan)

        while True:
            tampilkan_nilai_siswa(siswa_ditemukan)
            konfirmasi = input("\nApakah ada yang ingin diubah? (Y/N): ").strip().upper()
            if konfirmasi == "Y":
                ubah_nilai_siswa(siswa_ditemukan)
            elif konfirmasi == "N":
                tampilkan_rekap_nilai(siswa_ditemukan)
                break
            else:
                print("⚠️ Pilih Y atau N saja.")

        if tanya_lagi("\n🔁 Apakah Anda Ingin Input Data Nilai Siswa Lainnya? (Y/N): "):
            continue
        else:
            return

# ==========================
# FUNGSI UBAH NILAI SISWA
# ==========================
def ubah_nilai_siswa(siswa_ditemukan):
        print("\nPilih Mata Pelajaran yang ingin diubah:")
        for index, pelajaran in enumerate(mata_pelajaran, 1):
            print(f"{index}. {pelajaran}")
        print(f"{len(mata_pelajaran)+1}. Batal \n")

        ubah_nilai_mata_pelajaran(siswa_ditemukan)

# ==========================
# FUNGSI TAMPIL NILAI SISWA
# ==========================
def tampilkan_nilai_siswa(siswa):
    data_tabulate = [
        {"Mata Pelajaran": judul.capitalize().replace("_", " "), "Nilai": nilai}
        for judul, nilai in siswa["nilai"].items()
    ]

    print("\n📋 Data Nilai Terbaru:")
    print(tabulate(data_tabulate, headers="keys", tablefmt="rounded_outline"))

# ==========================
# FUNGSI REKAP: RATA-RATA & REMEDIAL
# ==========================
def tampilkan_rekap_nilai(siswa):
    print("\n📊 Rekapitulasi Nilai:")
    nilai_list = list(siswa["nilai"].values())
    rata_rata = sum(nilai_list) / len(nilai_list)

    print(f"Nama: {siswa['nama_lengkap']}")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")

    remedial = [judul.replace("_", " ").capitalize() for judul, nilai in siswa["nilai"].items() if nilai < 60]

    if remedial:
        print("\n❌ Mata Pelajaran yang Perlu Remedial:\n")
        for i in remedial:
            print(f" - {i}")
    else:
        print("\n✅ Tidak ada mata pelajaran yang perlu remedial.\n")

# ==========================
# MENU 2: Tampilkan Seluruh Data Nilai Siswa
# ==========================
def tampilkan_semua_data_siswa():
    table = []
    for siswa in data_siswa:
        row = [siswa["studentId"], siswa["nama_lengkap"]]
        row.extend([siswa["nilai"].get(p.lower().replace(" ", "_"), "-") for p in mata_pelajaran])
        table.append(row)
    headers = ["Student ID", "Nama"] + mata_pelajaran
    print("\n📋 Semua Data Nilai Siswa:")
    print(tabulate(table, headers=headers, tablefmt="rounded_outline"))

# ==========================
# MENU 3: Cari Data Nilai Siswa Tertentu
# ==========================
def cari_data_siswa():    
    while True:
        print()
        print("Cari Data Nilai Siswa")
        print("----------------------")
        # Input Student ID
        id_siswa = input("Masukkan Student ID Siswa: ").strip().upper()
        # Cek Input Student ID
        if not re.match(r"^[A-Z]{3}\d{3}$", id_siswa):
            print("⚠️ Format Student ID salah! Contoh yang benar: MUR001, GUR002.\n")
            continue
        # Cari siswa berdasarkan Student ID
        siswa_ditemukan = cek_id_siswa(id_siswa, data_siswa)
        # Jika tidak ditemukan, minta input ulang
        if not siswa_ditemukan:
            if tanya_lagi("\n🔁 Apakah Anda Ingin Mencoba Lagi? (Y/N): "):
                continue
            else:
                break
        tampilkan_nilai_siswa(siswa_ditemukan)

        if tanya_lagi("\n🔁  Apakah Anda Ingin Input Data Nilai Siswa Lainnya? (Y/N): "):
            continue
        else:
            return

# ==========================
# MENU 4: Hapus Data Nilai Siswa
# ==========================
def hapus_data_siswa(data_siswa):
    while True:
        print()
        id_siswa = input("Masukkan Student ID yang ingin dihapus: ").strip().upper()
        # Cek Input Student ID
        if not re.match(r"^[A-Z]{3}\d{3}$", id_siswa):
            print("⚠️ Format Student ID salah! Contoh yang benar: MUR001, GUR002.\n")
            continue
        # Cari siswa berdasarkan Student ID
        siswa_ditemukan = cek_id_siswa(id_siswa, data_siswa)
        # Jika tidak ditemukan, minta input ulang
        if not siswa_ditemukan:
            if tanya_lagi("\n🔁 Apakah Anda Ingin Mencoba Lagi? (Y/N): "):
                continue
            else:
                break

        for i in data_siswa:
            if i["studentId"] == id_siswa:
                siswa_ditemukan = True
                data_siswa.remove(i)
                delete_history.append(i)
                print(f"✅ Data siswa {id_siswa} berhasil dihapus.")
                break

        if not siswa_ditemukan:
            if tanya_lagi("\n❌ Data tidak ditemukan. Coba lagi? (Y/N): "):
                continue
            else:
                break

        if not tanya_lagi("\n🔁 Hapus siswa lain? (Y/N):"):
            break

    return data_siswa

# ==========================
# MENU 5: Hapus Data Nilai Siswa
# ==========================
def tampilkan_delete_history():
    print("\n🗑️  Riwayat Penghapusan:")
    if not delete_history:
        print("Belum ada data yang dihapus.")
        return

    for i, s in enumerate(delete_history, start=1):
        print(f"{i}. {s['studentId']} - {s['nama_lengkap']}")

# ==========================
# MENU 6: Hitung Rata-Rata Nilai Kelas
# ==========================
def rata_rata_kelas():
    print("\n📊 Rata-Rata Nilai Kelas:")
    rata_rata_nilai = []
    for siswa in data_siswa:
        nilai_list = list(siswa["nilai"].values())
        #Ternary Operator
        rata_siswa = sum(nilai_list) / len(nilai_list) if nilai_list else 0
        rata_rata_nilai.append(rata_siswa)
        print(f"{siswa['nama_lengkap']}: {rata_siswa:.1f}")
    rata_rata_kelas = sum(rata_rata_nilai) / len(rata_rata_nilai) if rata_rata_nilai else 0
    print(f"\nRata-rata keseluruhan kelas: {rata_rata_kelas:.1f}")

# ==========================
# MENU 7: Tampilkan Ranking Siswa
# ==========================
def ranking_siswa():
    ranking = []

    for siswa in data_siswa:
        nilai_list = list(siswa["nilai"].values())
        rata_siswa = sum(nilai_list) / len(nilai_list) if nilai_list else 0
        ranking.append({
            "nama": siswa["nama_lengkap"],
            "rata": round(rata_siswa, 1)
        })
    ranking_sorted = sorted(ranking, key=lambda x: x["rata"], reverse=True)
    for idx, siswa in enumerate(ranking_sorted, start=1):
        siswa["ranking"] = idx

    print("\n🏆 Ranking Siswa Berdasarkan Rata-Rata:")
    print(tabulate(
        ranking_sorted,
        headers={"ranking": "Ranking", "nama": "Nama", "rata": "Rata-Rata"},
        tablefmt="rounded_outline"
    ))

# ==========================
# MENU 8: Rekapitulasi Nilai per Mata Pelajaran
# ==========================
def rekap_per_mapel():
    print("\n📊 Rekap Nilai per Mata Pelajaran:")
    table = []
    nilai_mapel = []

    for nilai in mata_pelajaran:
        key = nilai.lower().replace(" ", "_")
        
        for siswa in data_siswa:
            nilai_siswa = siswa["nilai"].get(key, 0)
            nilai_mapel.append(nilai_siswa)
        rata_mapel = round(sum(nilai_mapel) / len(nilai_mapel) if nilai_mapel else 0, 1)
        table.append([nilai, min(nilai_mapel), max(nilai_mapel), rata_mapel])
    print(tabulate(table, headers=["Mata Pelajaran", "Min", "Max", "Rata-Rata"], tablefmt="rounded_outline"))

# ==========================
# MENU 9: Daftar Siswa yang Perlu Remedial
# ==========================
def daftar_remedial():
    print("\nDaftar Siswa yang Perlu Remedial:")
    table = []
    for siswa in data_siswa:
        remedial = [k.replace("_", " ").capitalize() for k, v in siswa["nilai"].items() if v < 60 and v > 0]
        if remedial:
            table.append([siswa["studentId"], siswa["nama_lengkap"], ", ".join(remedial)])
    if table:
        print(tabulate(table, headers=["ID", "Nama", "Mata Pelajaran"], tablefmt="rounded_outline"))
    else:
        print("✅ Tidak ada siswa yang perlu remedial.")

# ==========================
# MENU 10: Cetak / Export ke CSV
# ==========================
def export_csv():
    print("\n📤 Export Data Nilai Siswa")
    print("--------------------------")
    print("1. Export semua siswa")
    print("2. Export siswa tertentu")

    pilihan = input("\nSilahkan Pilih Opsi (1/2): ").strip()
    if pilihan == "1" or pilihan == "2":
        True
    else:
        print("⚠️ Pilih 1 atau 2 saja.")

    headers = ["Student ID", "Nama"] + mata_pelajaran

    if pilihan == "1":
        filename = "rekap_nilai_siswa.csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
                
            for siswa in data_siswa:
                row = [siswa["studentId"], siswa["nama_lengkap"]]
                row.extend([siswa["nilai"].get(p.lower().replace(" ", "_"), "") for p in mata_pelajaran])
                writer.writerow(row)

            print(f"✅ Semua data siswa berhasil diexport ke '{filename}'")

    elif pilihan == "2":
        while True:
            # Input Student ID
            id_siswa = input("Masukkan Student ID Siswa: ").strip().upper()
            # Cek Input Student ID
            if not re.match(r"^[A-Z]{3}\d{3}$", id_siswa):
                print("⚠️ Format Student ID salah! Contoh yang benar: MUR001, GUR002.\n")
                continue
            # Cari siswa berdasarkan Student ID
            siswa_ditemukan = cek_id_siswa(id_siswa, data_siswa)
            # Jika tidak ditemukan, minta input ulang
            if not siswa_ditemukan:
                if tanya_lagi("\n🔁 Apakah Anda Ingin Mencoba Lagi? (Y/N): "):
                    continue
                else:
                    break

            filename = f"{siswa_ditemukan['studentId'].lower()}_{siswa_ditemukan['nama_lengkap'].lower().replace(' ', '_')}.csv"

            if siswa_ditemukan:
                with open(filename, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)

                    row = [siswa_ditemukan["studentId"], siswa_ditemukan["nama_lengkap"]]
                    row.extend([siswa_ditemukan["nilai"].get(p.lower().replace(" ", "_"), "") for p in mata_pelajaran])
                    writer.writerow(row)
                print(f"✅ Data siswa {id_siswa} berhasil diexport ke {filename}")
            else:
                print("❌ Data siswa tidak ditemukan. Tidak ada yang diexport.")

            if tanya_lagi("\n🔁  Apakah Anda Ingin Export Data Nilai Siswa Lainnya? (Y/N): "):
                continue
            else:
                return

# ==========================
# MAIN MENU
# ==========================
def main():
    while True:
        print()
        print("Menu Utama:")
        print("1. Input Data Nilai Siswa")
        print("2. Tampilkan Seluruh Data Nilai Siswa")
        print("3. Cari Data Nilai Siswa Tertentu")
        print("4. Hapus Data Nilai Siswa")
        print("5. Tampilkan Riwayat Penghapusan Data")
        print("6. Hitung Rata-Rata Nilai Kelas")
        print("7. Tampilkan Ranking Siswa")
        print("8. Rekapitulasi Nilai per Mata Pelajaran")
        print("9. Daftar Siswa yang Perlu Remedial")
        print("10. Cetak / Laporan Nilai")
        print("11. Keluar dari Program")
        print()
        choice = input("Silahkan Pilih Menu (1-11): ").strip()

        if choice == "1":
            input_nilai_siswa(data_siswa)
        elif choice == "2":
            tampilkan_semua_data_siswa()
        elif choice == "3":
            cari_data_siswa()
        elif choice == "4":
            hapus_data_siswa(data_siswa)
        elif choice == "5":
            tampilkan_delete_history()
        elif choice == "6":
            rata_rata_kelas()
        elif choice == "7":
            ranking_siswa()
        elif choice == "8":
            rekap_per_mapel()
        elif choice == "9":
            daftar_remedial()
        elif choice == "10":
            export_csv()
        elif choice == "11":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("⚠️ Pilihan tidak valid. Silahkan pilih 1–11.")

        if tanya_lagi("\nKembali ke menu utama? (Y/N): "):
            continue
        else:
            print("👋 Terima kasih! Program selesai.")
            break

if __name__ == "__main__":
    main()
