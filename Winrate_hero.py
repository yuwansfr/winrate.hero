import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung pertandingan yang diperlukan
def hitung_pertandingan():
    try:
        # Mendapatkan input dari form
        jumlah_pertandingan = int(entry_pertandingan.get())
        winrate_saat_ini = float(entry_winrate.get())
        target_winrate = float(entry_target_winrate.get())
        
        # Menghitung jumlah kemenangan saat ini
        jumlah_kemenangan_saat_ini = jumlah_pertandingan * (winrate_saat_ini / 100)
        
        # Menyusun persamaan untuk mencari jumlah pertandingan yang diperlukan
        target_winrate = target_winrate / 100  # Mengubah target winrate menjadi desimal
        x = (jumlah_kemenangan_saat_ini - target_winrate * jumlah_pertandingan) / (target_winrate - 1)
        
        # Jika x <= 0, berarti winrate target sudah tercapai
        if x <= 0:
            messagebox.showinfo("Hasil", "Winrate target sudah tercapai atau tidak dapat tercapai dengan kemenangan penuh.")
        else:
            messagebox.showinfo("Hasil", f"Untuk mencapai winrate {target_winrate * 100}%, Anda perlu memainkan {round(x)} pertandingan dan menang semua pertandingan tersebut.")
    
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai yang valid untuk semua field.")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Hitung Winrate Hero")

# Membuat label dan entry (form input) untuk jumlah pertandingan
label_pertandingan = tk.Label(root, text="Jumlah Pertandingan Saat Ini:")
label_pertandingan.pack(padx=10, pady=5)
entry_pertandingan = tk.Entry(root)
entry_pertandingan.pack(padx=10, pady=5)

# Membuat label dan entry (form input) untuk winrate saat ini
label_winrate = tk.Label(root, text="Winrate Saat Ini (%):")
label_winrate.pack(padx=10, pady=5)
entry_winrate = tk.Entry(root)
entry_winrate.pack(padx=10, pady=5)

# Membuat label dan entry (form input) untuk target winrate
label_target_winrate = tk.Label(root, text="Target Winrate yang Diinginkan (%):")
label_target_winrate.pack(padx=10, pady=5)
entry_target_winrate = tk.Entry(root)
entry_target_winrate.pack(padx=10, pady=5)

# Membuat tombol untuk menghitung
button_hitung = tk.Button(root, text="Hitung", command=hitung_pertandingan)
button_hitung.pack(padx=10, pady=20)

# Menjalankan aplikasi
root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung pertandingan yang diperlukan
def hitung_pertandingan():
    try:
        # Mendapatkan input dari form
        jumlah_pertandingan = int(entry_pertandingan.get())
        winrate_saat_ini = float(entry_winrate.get())
        target_winrate = float(entry_target_winrate.get())
        
        # Menghitung jumlah kemenangan saat ini
        jumlah_kemenangan_saat_ini = jumlah_pertandingan * (winrate_saat_ini / 100)
        
        # Menyusun persamaan untuk mencari jumlah pertandingan yang diperlukan
        target_winrate = target_winrate / 100  # Mengubah target winrate menjadi desimal
        x = (jumlah_kemenangan_saat_ini - target_winrate * jumlah_pertandingan) / (target_winrate - 1)
        
        # Jika x <= 0, berarti winrate target sudah tercapai
        if x <= 0:
            messagebox.showinfo("Hasil", "Winrate target sudah tercapai atau tidak dapat tercapai dengan kemenangan penuh.")
        else:
            messagebox.showinfo("Hasil", f" Anda perlu memainkan {round(x)} tanpa kalah , Untuk mencapai winrate {target_winrate * 100}%.")
    
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai yang valid untuk semua field.")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Hitung Winrate Hero")

# Membuat label dan entry (form input) untuk jumlah pertandingan
label_pertandingan = tk.Label(root, text="Jumlah Pertandingan yang Sudah Dimainkan:")
label_pertandingan.pack(padx=10, pady=5)
entry_pertandingan = tk.Entry(root)
entry_pertandingan.pack(padx=10, pady=5)

# Membuat label dan entry (form input) untuk winrate saat ini
label_winrate = tk.Label(root, text="Winrate Saat Ini (%):")
label_winrate.pack(padx=10, pady=5)
entry_winrate = tk.Entry(root)
entry_winrate.pack(padx=10, pady=5)

# Membuat label dan entry (form input) untuk target winrate
label_target_winrate = tk.Label(root, text="Target Winrate yang Diinginkan (%):")
label_target_winrate.pack(padx=10, pady=5)
entry_target_winrate = tk.Entry(root)
entry_target_winrate.pack(padx=10, pady=5)

# Membuat tombol untuk menghitung
button_hitung = tk.Button(root, text="Hitung", command=hitung_pertandingan)
button_hitung.pack(padx=10, pady=20)

# Menjalankan aplikasi
root.mainloop()
