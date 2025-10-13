# DataNilaiSiswa
Projek untuk memudahkan para guru dalam menginput data nilai siswa dan secara otomatis mendapatkan output yang mereka inginkan

  Program ini dibuat dengan tujuan untuk memudahkan para guru dalam menginput nilai siswa dan mendapatkan output yang mereka inginkan secara otomatis. Misalnya: rata-rata kelas, rekapitulasi nilai per mata pelajaran, ranking siswa, list siswa yang remedial, dll

  Program ini dimulai dengan function main() yang dimana akan memunculkan 11 menu yang dapat dipilih oleh user.

  Menu 1:
    - Menu ini dimulai dengan meminta para guru untuk menginput Student ID Siswa yang mau diinput nilainya
    - ketika penginputan akan ada 2 pengecekan: 
      1. pengecekan regex terhadap format Student ID
      2. fungsi cek_id_siswa
      Fungsi cek_id_siswa itu isinya adalah ngeloop ke list of dictionary data_siswa untuk mengecek apakah Student ID yang diinput ada terdaftar, jika iya maka akan    mengembalikan (f"✅ Data Siswa Ditemukan: {siswa_ditemukan['nama_lengkap']}\n") dan jika tidak maka akan mengembalikan ("❌ Data Siswa Tidak Ditemukan!\n")
    untuk regex nya sendiri akan mengecek apakah Student IDnya dimulai dengan A-Z untuk 3 huruf pertamanya dan diakhiri dengan ankga di ketiga huruf akhirnya
    Jika Siswa tidak ditemukan atau formatnya salah, maka akan diminta untuk menginput data yang benar

    Setelah Siswa Ditemukan,
    Program akan mengecek dulu apakah murid yang dipilih sudah terisi nilainyua atau belum, kalau sudah maka akan menampilkan nilai siswa dengan bantuan function tampilkan_nilai_siswa yang mana akan ngeloop ke list mata_pelajaran dan ngeprint title mapel dan nilainya aja dalam bentuk tabulate (tabel yang rapi)

    Lalu program akan bertanya, apakah anda ingin merubah 
