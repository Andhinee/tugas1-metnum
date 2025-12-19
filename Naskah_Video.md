# SKRIP VIDEO PRESENTASI - TUGAS METODE NUMERIK
**Topik:** Regresi Linear (Prediksi Gaji)
**Durasi Estimasi:** 3 - 5 menit

---

### [00:00 - 00:45] Pembukaan & Perkenalan
**(Tampilkan Slide Judul: Judul Tugas, Nama, NIM)**

"Assalamualaikum Wr. Wb. / Salam sejahtera."

"Halo, perkenalkan nama saya **[SEBUTKAN NAMA ANDA]**, dengan NIM **[SEBUTKAN NIM ANDA]**."

"Pada video kali ini, saya akan mempresentasikan tugas mata kuliah **Metode Numerik**, mengenai penerapan metode **Regresi Linear**."

"Studi kasus yang saya angkat adalah: **Prediksi Gaji Karyawan berdasarkan Tahun Pengalaman (Years of Experience)**."

---

### [00:45 - 02:00] Konsep Dasar & Metode
**(Tampilkan Slide: Rumus Regresi y = a + bx dan Grafik Ilustrasi)**

"Pertama, mari kita bahas konsepnya. Masalah yang sering dihadapi HRD adalah menentukan gaji yang fair. Secara intuitif, makin lama pengalaman, gaji makin tinggi. Tapi berapa kenaikannya?"

"Untuk menjawab ini, kita gunakan **Regresi Linear Sederhana**. Ini adalah metode numerik untuk mencari garis lurus yang paling pas mewakili sebaran data kita."

"Persamaannya adalah `Y = a + bX`.
Dimana:
*   Y adalah Gaji yang diprediksi.
*   X adalah Tahun Pengalaman.
*   a dan b adalah koefisien yang kita cari."

"Dalam metode numerik, untuk mencari a dan b agar error-nya paling kecil, kita menggunakan metode **Least Squares** atau Kuadrat Terkecil. Rumusnya melibatkan jumlah (sigma) dari data X, data Y, X kuadrat, dan perkalian XY."

---

### [02:00 - 04:00] Implementasi Kode & Demo
**(Ganti tampilan ke Share Screen: Teks Editor / VS Code yang membuka file `salary_regression.py`)**

"Sekarang mari kita lihat implementasinya dalam kode program. Di sini saya menulis skrip menggunakan Python."

"Bisa dilihat di sini, saya **TIDAK** menggunakan library regresi instan seperti scikit-learn untuk proses intinya, melainkan saya menulis fungsi `linear_regression_least_squares` sendiri."

**(Highlight kursor mouse ke bagian fungsi rumus)**
"Di dalam fungsi ini, saya menerjemahkan rumus matematika sigma tadi menjadi kode Python menggunakan library `numpy` untuk operasi matematikanya. Ini menghitung slope (b) dan intercept (a)."

**(Jalankan program di terminal)**
"Mari kita coba jalankan programnya."

**(Tampilkan Output Terminal)**
"Nah, program berhasil menghitung koefisien secara otomatis.
Ditemukan persamaannya adalah `Y = 26588 + 9389 X`.
Artinya setiap tambah 1 tahun pengalaman, gaji naik sekitar 9 ribu unit angka."

**(Tampilkan Grafik Pop-up)**
"Dan ini adalah visualisasinya. Titik biru adalah data contoh, dan garis merah adalah hasil perhitungan metode numerik kita. Terlihat garisnya sangat pas membelah data."

---

### [04:00 - 05:00] Penutup
**(Kembali ke wajah pembicara atau slide kesimpulan)**

"Kesimpulannya, Metode Numerik Regresi Linear sangat berguna untuk melakukan prediksi berbasis data data historis. Implementasi dengan Python memudahkan kita melakukan perhitungan kompleks dalam waktu singkat."

"Sekian presentasi dari saya. Terima kasih atas perhatiannya."

"Wassalamualaikum Wr. Wb."
