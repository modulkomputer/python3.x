import datetime
import date as dt

# Belajar latihan date time
print("Masukan tanggal bulan tahun anda lahir: ")
tanggal = int(input("tanggal \t"))
bulan = int(input("bulan \t\t"))
tahun = int(input("tahun \t\t"))

# untuk menghitung bulan, tanggal, tahun
tgl_lahir = dt.datetime(tahun, bulan, tanggl)
print(f"tanggal lahir: {tgl_lahir}")

# menghitung umur
hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur = hari_ini - tgl_lahir
print(f"umur anda adalah: {umur}")
