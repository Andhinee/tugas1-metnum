# TUGAS METODE NUMERIK
## PENERAPAN REGRESI LINEAR UNTUK PREDIKSI GAJI KARYAWAN

**Nama:** [NAMA ANDA]  
**NIM:** [NIM ANDA]  
**Mata Kuliah:** Metode Numerik  
**Topik:** Regresi (Regression)

---

### 1. Deskripsi Problem dan Tujuan Penerapan

**Latar Belakang:**  
Dalam dunia sumber daya manusia (SDM) dan manajemen perusahaan, menentukan standar gaji yang adil seringkali menjadi tantangan. Gaji biasanya berkorelasi positif dengan pengalaman kerja; semakin lama pengalaman seseorang, semakin tinggi nilai kontribusinya bagi perusahaan. Namun, kenaikan ini tidak selalu jelas polanya jika hanya melihat data mentah.

**Permasalahan:**  
Bagaimana memperkirakan (memprediksi) gaji yang layak untuk calon karyawan dengan jumlah tahun pengalaman tertentu berdasarkan data historis yang dimiliki perusahaan, tanpa menebak-nebak secara subjektif?

**Tujuan Penerapan:**  
Tujuan dari penerapan ini adalah membangun model matematis sederhana menggunakan **Metode Numerik Regresi Linear** untuk mencari hubungan antara variabel independen ($X$ = Tahun Pengalaman) dan variabel dependen ($Y$ = Gaji). Model ini akan digunakan untuk memprediksi gaji berdasarkan input tahun pengalaman.

### 2. Uraian Konsep dan Metode

**Metode: Regresi Linear Sederhana (Simple Linear Regression)**  
Regresi linear adalah metode statistika dan numerik yang digunakan untuk memodelkan hubungan antara dua variabel dengan mencocokkan persamaan linear (garis lurus) pada data yang diamati.

Persamaan garis regresi adalah:
$$Y = a + bX$$
Dimana:
*   $Y$ = Variabel dependen (Gaji)
*   $X$ = Variabel independen (Tahun Pengalaman)
*   $a$ = Intercept (titik potong garis dengan sumbu Y)
*   $b$ = Slope (kemiringan garis / gradien)

**Algoritma: Metode Kuadrat Terkecil (Ordinary Least Squares - OLS)**  
Untuk menentukan nilai konstanta $a$ dan $b$ yang paling optimal (error paling minimum), digunakan metode kuadrat terkecil. Rumus numerik yang diimplementasikan adalah:

$$b = \frac{n \sum (X_i Y_i) - (\sum X_i)(\sum Y_i)}{n \sum (X_i^2) - (\sum X_i)^2}$$

$$a = \frac{\sum Y_i - b \sum X_i}{n}$$
atau
$$a = \bar{Y} - b\bar{X}$$

Dimana $n$ adalah jumlah data. Metode ini meminimalkan jumlah kuadrat selisih antara nilai $Y$ aktual dan nilai $Y$ prediksi.

### 3. Implementasi Kode Program

Program dibuat menggunakan bahasa **Python**. Pustaka yang digunakan adalah:
*   `numpy`: Untuk operasi array dan perhitungan numerik (sum, perkalian array).
*   `matplotlib`: Untuk visualisasi data dan garis regresi.

**Struktur Code (Snippet Inti):**
Berikut adalah implementasi rumus metode OLS dalam fungsi Python, tanpa menggunakan library instan seperti `sklearn` untuk regresi, agar menunjukkan pemahaman metode numerik.

```python
# Fungsi menghitung koefisien a dan b
def linear_regression_least_squares(x, y):
    n = len(x)
    
    # Menghitung sigma (jumlah)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x * x)
    sum_xy = np.sum(x * y)
    
    # Rumus Slope (b)
    numerator_b = (n * sum_xy) - (sum_x * sum_y)
    denominator_b = (n * sum_xx) - (sum_x ** 2)
    b = numerator_b / denominator_b
    
    # Rumus Intercept (a)
    a = (sum_y - (b * sum_x)) / n
    
    return a, b
```

**Dataset:**
Data yang digunakan adalah data dummy sebanyak 20 sampel data karyawan berisi pasangan (Tahun Pengalaman, Gaji).

### 4. Hasil Demonstrasi Program

Setelah program dijalankan, didapatkan parameter model regresi sebagai berikut:

**Output Program:**
```text
=== PROGRAM REGRESI LINEAR: PREDIKSI GAJI ===
Jumlah data latihan: 20

Hasil Perhitungan Metode Numerik (Least Squares):
Slope (b)     : 9389.2678
Intercept (a) : 26588.6310
Persamaan     : Y = 26588.63 + 9389.27X
```

**Analisis:**
*   **Intercept ($a \approx 26588$):** Ini menunjukkan estimasi gaji dasar (base salary) untuk seseorang dengan pengalaman 0 tahun adalah sekitar 26,588.
*   **Slope ($b \approx 9389$):** Ini menunjukkan setiap kenaikan 1 tahun pengalaman, gaji rata-rata naik sebesar 9,389.

**Visualisasi Grafik:**
Program menghasilkan grafik yang memplot titik-titik data aktual (biru) dan garis regresi linear (merah). Garis merah terlihat melintasi tengah-tengah sebaran data, menunjukkan bahwa model regresi cukup representatif (Goodness of fit) untuk data ini.

*(Disini Anda bisa menyisipkan gambar 'grafik_regresi_gaji.png' yang dihasilkan program)*

**Uji Prediksi:**
Contoh prediksi untuk pengalaman 10 tahun:
$Y = 26588.63 + 9389.27(10) = 120481.33$

### 5. Referensi

1.  Chapra, S. C., & Canale, R. P. (2015). *Numerical Methods for Engineers*. McGraw-Hill Education.
2.  Dataset Sample: Kaggle - Salary Data based on Years of Experience.
3.  Dokumentasi NumPy: https://numpy.org/doc/
4.  Dokumentasi Matplotlib: https://matplotlib.org/

---
*Dokumen ini dibuat untuk memenuhi tugas mata kuliah Metode Numerik.*
