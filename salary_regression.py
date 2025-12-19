import numpy as np
import matplotlib.pyplot as plt

def linear_regression_least_squares(x, y):
    """
    Menghitung koefisien regresi linear sederhana a dan b
    menggunakan metode Least Squares (Kuadrat Terkecil).
    Persamaan: y = a + bx
    """
    n = len(x)
    
    # Menghitung sum needed
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x * x)
    sum_xy = np.sum(x * y)
    
    # Menghitung koefisien a (intercept) dan b (slope)
    # Rumus b = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x**2)
    # Rumus a = (sum_y - b*sum_x) / n
    
    # Pembilang dan Penyebut untuk b
    numerator_b = (n * sum_xy) - (sum_x * sum_y)
    denominator_b = (n * sum_xx) - (sum_x ** 2)
    
    b = numerator_b / denominator_b
    a = (sum_y - (b * sum_x)) / n
    
    return a, b

def predict(a, b, x_val):
    return a + (b * x_val)

def main():
    print("=== PROGRAM REGRESI LINEAR: PREDIKSI GAJI ===")
    
    # 1. Dataset (Years of Experience vs Salary)
    # Sumber data dummy yang mendekati realita
    x_data = np.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7, 
                       3.9, 4.0, 4.0, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6.0])
    y_data = np.array([39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189,
                       63218, 55794, 56957, 57081, 61111, 67938, 66029, 83088, 81363, 93940])

    print(f"Jumlah data latihan: {len(x_data)}")
    
    # 2. Hitung Model Regresi
    a, b = linear_regression_least_squares(x_data, y_data)
    
    print("\nHasil Perhitungan Metode Numerik (Least Squares):")
    print(f"Slope (b)     : {b:.4f}")
    print(f"Intercept (a) : {a:.4f}")
    print(f"Persamaan     : Y = {a:.2f} + {b:.2f}X")
    
    # 3. Visualisasi
    plt.figure(figsize=(10, 6))
    
    # Plot data asli
    plt.scatter(x_data, y_data, color='blue', label='Data Aktual')
    
    # Plot garis regresi
    y_pred_line = a + b * x_data
    plt.plot(x_data, y_pred_line, color='red', label=f'Regresi (Y={a:.0f}+{b:.0f}X)')
    
    plt.title('Prediksi Gaji berdasarkan Pengalaman Kerja (Years of Experience)')
    plt.xlabel('Tahun Pengalaman (Years)')
    plt.ylabel('Gaji (Salary)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    print("\nMenampilkan grafik...")
    # Simpan grafik untuk laporan
    plt.savefig('grafik_regresi_gaji.png')
    print("Grafik disimpan sebagai 'grafik_regresi_gaji.png'")
    # plt.show() # Uncomment jika dijalankan di local dengan display
    
    # 4. Prediksi Interaktif
    print("\n--- Uji Coba Prediksi ---")
    years_input = [1.5, 5.0, 10.0] 
    for yr in years_input:
        pred_salary = predict(a, b, yr)
        print(f"Pengalaman: {yr} tahun -> Prediksi Gaji: {pred_salary:.2f}")

if __name__ == "__main__":
    main()
