print("-" * 65)
print("SELAMAT DATANG DI KALKULATOR ARITMATIKA SOSIAL")
print("-" * 65)

print("Silahkan pilih operasi yang diinginkan")
#RUMUS DASAR Bunga=Modal*suku bunga*waktu
print("1. Mencari Bunga")
print("2. Mencari modal")
print("3. Mencari Waktu(Bulan)")
operasi = int(input("pilih operasi yang diinginkan!(1/2/3) "))

if operasi == 1:
  modal_awal = float(input("Masukkan modal awalmu! "))
  modal_akhir = float(input("Masukkan modal Akhirmu!"))
  hasil = modal_akhir - modal_awal
  print(f"Hasil bunga yang kamu terima adalah Rp.{hasil}")
elif operasi == 2:
  pilih = input("apakah sudah diketahui bunga dan modal akhir?(iya/tidak) ")
  if pilih.lower() == "iya": 
    modal_akhir = float(input("Isi modal akhirmu "))
    bunga = float(input("Isi bunga yang sudah kamu hitung "))
    hasil = modal_akhir - bunga
    print(f"Modal awal kamu adalah Rp.{hasil}")
  else:
    waktu = input("Kamu mencari modal tahun?(iya/tidak) ")
    if waktu.lower() == "iya":
      bunga = float(input("Isi bunga yang sudah kamu hitung "))
      suku_bunga = int(input("Masukkan suku bunga kamu(angka saja) "))
      suku = suku_bunga / 100
      waktu_tahun = int(input("Masukkan waktu kamu dalam tahun! "))
      hasil = bunga / (suku * waktu_tahun)
      print(f"Modal kamu sudah dihitung dengab hasil Rp.{hasil}")
    else:
      bunga = float(input("Isi bunga yang sudah kamu hitung "))
      suku_bunga = int(input("Masukkan suku bunga kamu(angka saja) "))
      suku = suku_bunga / 100
      waktu_bulan = int(input("Masukkan waktu kamu dalam bulan! ")) / 12
      hasil = bunga / (suku * waktu_bulan)
      print(f"Modal kamu sudah dihitung dengab hasil Rp.{hasil}")
elif operasi == 3:
  print("masih dalam pengerjaan!")