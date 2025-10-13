# DataNilaiSiswa
Projek untuk memudahkan para guru dalam menginput data nilai siswa dan secara otomatis mendapatkan output yang mereka inginkan

  Program ini dibuat dengan tujuan untuk memudahkan para guru dalam menginput nilai siswa dan mendapatkan output yang mereka inginkan secara otomatis. Misalnya: rata-rata kelas, rekapitulasi nilai per mata pelajaran, ranking siswa, list siswa yang remedial, dll

  Program ini dimulai dengan function main() yang dimana akan memunculkan 11 menu yang dapat dipilih oleh user.

  Menu 1 (Input Nilai Siswa) :
  
  Menu ini dimulai dengan meminta para guru untuk menginput Student ID Siswa yang mau diinput nilainya. Ketika penginputan akan ada 2 pengecekan yaitu pengecekan regex terhadap format Student ID dan fungsi cek_id_siswa.
    
  Fungsi cek_id_siswa itu isinya adalah ngeloop menggunakan for loop melalui list dictionary data_siswa untuk mengecek apakah Student ID yang diinput ada terdaftar. Jika iya, maka akan mengembalikan "✅ Data Siswa Ditemukan: {siswa_ditemukan['nama_lengkap']" dan jika tidak maka akan mengembalikan "❌ Data Siswa Tidak Ditemukan!".

  Fungsi regex nya sendiri akan mengecek apakah Student IDnya dimulai dengan A-Z untuk 3 huruf pertamanya dan diakhiri dengan angka di ketiga huruf terakhirnya.

  Jika Siswanya tidak ditemukan melalui fungsi cek_id_siswa atau formatnya salah tidak sesuai dengan regexnya maka sistem akan meminta guru untuk menginput data yang benar.

  Setelah siswa ditemukan, maka sistem akan mengecek terlebih dahulu apakah murid yang dipilih telah diisi nilainya atau belum. Kalau sudah, maka akan menampilkan nilai siswa dengan bantuan function tampilkan_nilai_siswa yang mana akan ngeloop menggunakan for loop ke list mata_pelajaran dan ngeprint tile mata pelajaran dan nilainya aja dalam bentuk tabel yang rapi dengan bantuan tabulate.

  Jika guru ingin mengubah nilai yang sudah diinput sebelumnya, maka guru bisa menekan "Y" saat sistem bertanya "Apakah Anda ingin mengubah nilai yang sudah ada? (Y/N)". Jika mengubah maka sistem akan mengarahkan ke function ubah_nilai_siswa yang dimana function ini akan menggunakan for loop untuk mengeloop ke list mata_pelajaran untuk ditampilin ke guru index dan judulnya. Jadi, guru bisa memilih 1-8 untuk mata pelajaran yang ingin diganti. Disini juga ada pengecekan inputnya harus angka menggunakan isDigit(). Setelah pilihan mata pelajaran sudah didapatkan dan tepat, maka sistem akan meminta guru untuk menginput nilai barunya dan akan mengupdate langsung ke listnya.

  Namun, apabila siswa yang diinput diawal tadi ternyata nilainya masih 0 semua atau belum diinput sama sekali, maka sistem akan mengarahkan guru ke input semua mata pelajaran menggunakan for loop ke list mata_pelajaran dengan function input_nilai_mata_pelajaran. Hampir sama dengan function ubah_nilai_mata_pelajaran, function ini akan menggunakan kombinasi antara for loop dan while loop untuk menglooping ke mata_pelajaran untuk meminta guru untuk menginput nilai mata pelajaran 1 per 1. Sama seperti sebelumnya juga, disini bakal ada pengecekan harus angka menggunakan regex = isDigit() dan nilai yang diinput harus diantara 0-100.

  Setelah menginput, maka sama seperti flow diatas tadi, sistem akan menunjukkan semua nilai siswa yang bersangkutan dan menanyakan apakah ada yang mau diubah nilainya? Jika iya maka akan mengeloop untuk menunjukkan pilihan mata pelajaran mana yang mau diubah dan bisa langsung menginput nilai baru. Tetapi jika tidak ingin mengubah maka bisa langsung menulis 'N' dan sistem akan mengakhiri flownya dengan menunjukkan nama siswa, rata-rata nilai siswa, dan list pelajaran remedial yang perlu diikuti siswa melalui function tampilan_rekap_nilai. Function tampilan_rekap_nilai ini menjalankan logikanya dengan menggunakan list comprehension untuk mencari list mata pelajaran yang nilainya dibawah 60 untuk dimasukin ke list remedial siswa.

  Jika semua flow diatas telah selesai, maka sistem akan menanyakan "🔁 Apakah Anda Ingin Input Data Nilai Siswa Lainnya? (Y/N): ", Jika Y maka akan mengulangi flow diatas lagi. Tetapi, jika "N" Maka sistem akan menanyakan "Kembali ke menu utama? (Y/N): ". Jika "Y" maka sistem akan mengarahkan ke menu utama awal lagi dan jika tidak maka sistem akan mengeprint "👋 Terima kasih! Program selesai.".

  Menu 2 (Tampilkan Data Siswa - Semua) :

  Menu ini cukup straightforward karena sistem hanya akan membuat list tabel baru, lalu menggunakan for loop untuk mengeloop ke data siswa. Next, sistem akan membuat row yang berisi Student ID, Nama Lengkap Siswa, lalu disambung dengan menggunakan method extend yang berfungsi untuk memasukkan nilai siswa dari setiap mata pelajaran yang didapatkan dengan menggunakan for list comprehension dan lalu di append ke list table yang telah dibuat tadi. Lalu, sistem aka mengeprint ke dalam bentuk tabel yang rapi lagi dengan bantuan tabulate.

  Menu 3  (Tampilkan Data Siswa - Spesifik) :

  Menu ini sama dengan Menu ke 2 tetapi bedanya ini ditujukan untuk menampilkan nilai siswa spesifik.

  Menu ini akan mengcombine flow-flow yang ada di menu 1. 

  Menu ini akan dimulai dengan meminta Student ID Siswa yang ingin dilihat nilainya. Semua pengecekan dan Cara input akan sama dengan menu 1. Lalu setelah siswa ditemukan maka sistem penampilannya juga sama dengan di menu 1 yaitu dengan menggunakan bantuan function tampilkan_nilai_siswa. Flow akan diakhiri dengan pertanyaan yang sama dengan di menu 1 juga yaitu "🔁  Apakah Anda Ingin Input Data Nilai Siswa Lainnya? (Y/N):".

  Menu 4 (Hapus Data Nilai Siswa) :

  Menu ini akan dimulai dengan hal yang sama lagi seperti menu sebelumnya yaitu meminta untuk menginput Student ID Siswa dengan pengecekan yang sama. Jika sudah ditemukan maka akan dilanjutkan dengan menggunakan for loop untuk mengeloop ke dalam list data_siswa lalu meremove dengan menggunakan method list.remove(index) lalu diappend ke list yang sudah dibuat dia awal yaitu delete_history dengan menggunakan method append untuk ditambah di index paling akhirnya terus. Lalu, flow juga akan diakhiri dengan pertanyaan "🔁 Hapus siswa lain? (Y/N):"

  Menu 5 (Tampilkan Delete History) :

  Menu ini sangat simple, hanya akan menggunakan tabel delete_history yang telah ditambah dengan menggunakan append di menu ke 4 untuk di show sekarang. Jadi, flownya adalah menggunakan for loop in enumerate untuk menampilkan isi list delete_history tersebut.

  Menu 6 (Rata Rata Kelas) :

  Menu ini akan dimulai dengan membuat 1 list data baru yaitu rata_rata_nilai. Lalu untuk menambahkan data list ini dengan menggunakan method append, sistem akan menggunakan for loop untuk mengeloop ke list data_siswa untuk mendapatkan nilai-nilai mata pelajaran per siswa lalu menambahkan ke list rata_rata_nilai tadi. Sistem akan mengeprint Nama Lengkapdan rata_rata_nilai tadi. Lalu, sistem juga akan menghitung rata_rata_kelas dengan cara menghitung semua rata_rata_kelas dibagi dengan jumlah orang. Di flow ini, sistem akan coba menggunakan sistem Ternary Operator dimana formatnya adalah operasi trs dibelakangnya ada if dan else yang dimana nilai akan mengikuti if jika ada dan else jika tidak ada.

  Menu 7 (Tampilkan Ranking Siswa) :

  Di Menu ini, sistem akan membuat 1 list kosong bernama ranking, lalu sistem akan menggunakan for loop lagi untuk mengeloop ke data_siswa untuk mengambil nilai dan menghitung rata_siswa lalu akan diappend ke list ranking tadi. Lalu, rata_siswa di dalam list ranking tadi akan di sorted menggunakan tipe lambda. Next, sistem akan menggunakan for loop lagi untuk mengeloop dan menggunakan enumerate juga untuk mendapatkan rankingnya. Setelah itu, sistem tinggal mengeprint hasil for loop terakhir yang sudah ada index (ranking) nama dan nilainya rata-ratanya.

  Menu 8 (Rekapitulasi Nilai Mata Pelajaran) :

  Flow Menu ke 8 ini akan dimulai dengan membuat 2 list kosong yaitu tabel dan nilai_mapel untuk menampung nilai rata-rata per mata pelajaran dan lalu bisa di append ke tabel untuk dibentuk dalam bentuk tabulate. Sistem akan menggunakan for loop untuk mendapatkna key mata pelajaran yang disimpan dalam bentuk huruf kecil dan disambungin dengan _. Setelah mendapatkannya, sistem akan melakukan for loop lagi untuk mendapatkan nilai dari semua siswa untuk dihitung rata-ratanya. Rumus nya akan menggunakan ternary operator lagi seperti berikut.

  rata_mapel = round(sum(nilai_mapel) / len(nilai_mapel) if nilai_mapel else 0, 1)

  yang artinya kalau nilai_mapel ada maka akan menggunaka nilai nilai_mapel jika tidak maka 0. Lalu setiap nilai akan di append ke list table yang telah dibuat tadi untuk dimasukin dan di print ke dalam bentuk tabel yang rapi dengan bantuan tabulate.

  Menu 9 (Daftar Siswa yang Perlu Remedial) :

  Untuk Menu ini, sama seperti yang saya bilang di awal, program ini dibuat untuk memudahkan para guru untuk mendapatkan output dari menginput nilai siswa. Jadi menu ini akan mengeluarkan list-list siswa yang nilainya dibawah 60 atau mengikuti remedial. Jadi, flownya akan dimulai dengan membuat list table kosong untuk menampung listnya. Next, menggunakan for loop untuk mengeloop ke data_siswa untuk mencari siswa yang nilainya diatas 0 dan dibawah 60 dengan bantuan format list comprehension. Kenapa diatas 0, dikarenakan jika 0 semuanya maka ada kemungkinan bahwa nilai siswa tersebut memang belum diinput sama sekali oleh guru dan belum dikualifikasi untuk mengikuti ujian remedial. Setelah dapat datanya semua, maka akan diappend ke list table dan di print lagi dalam bentuk tabel yang rapi dengan bantuan tabulate.

  Menu 10 (Cetak / Export ke CSV) :

  Menu ini akan dimulai dengan pertanyaan ke guru, Apakah mereka ingin mengexport data semua siswa atau spesifik ke dalam bentuk CSV. Saat memilih akan ada penjagaan bawah input hanya bisa 1 atau 2 aja. Input diluar itu maka akan mendapatkan Error Message berupa "⚠️ Pilih 1 atau 2 saja.". Flow berikutnya adalah untuk mengexport kedalam bentuk CSVnya. Jadi, kita mulai dengan menuliskan headersnya terlebih dahulu, kira-kira headers apa saja yang ingin dimasukin ke CSV Filenya. Disini ada Student Id, Nama Siswa, dan semua Mata Pelajaran. Lalu, akan dilanjutkan dengan filename. Untuk pilihan 1, maka akan menggunakan filename "rekap_nilai_siswa.csv" dan jika pilihan 2 maka filenamenya adalah "{siswa_ditemukan['studentId'].lower()}_{siswa_ditemukan['nama_lengkap'].lower().replace(' ', '_')}.csv" yaitu mengambil studentId nya misalnya "MUR001" dan di lower jadi mur001 lalu dicombine dengan _ dan nama lengkap nya lalu mengganti spasi dengan _ jadi hasil akhir "mur001_alvin_edward.csv". Setelah ada 2 hal ini, maka kita tinggal menggunakan with open dan writer untuk menambahkan hal-hal yang telah kita buat tadi ke dalam bentuk CSV file. 

 ~ Kira-kira begini lah program yang telah saya buat ini, Semoga Bermanfaat dan Terima Kasih! ~


  
