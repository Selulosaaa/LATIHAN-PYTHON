print("SELAMAT DATANG DI KALKULATOR SEDERHANA!")
print("-" * 40)
print("Kalkulator ini hanya bisa input 2 angka dulu ya!!")
x = float(input('Masukkan angka pertama '))
y = float(input('Masukkan angka ke dua '))
print("-" * 20)
print("baiklah terimakasih sudah memasukkan angka tersebut")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. perkalian")
print("4. pembagian")
print("5. Pangkat")

operasi = float(input("masukkan angka untuk memilih operasi tersebut(1/2/3/4/5) "))
if operasi == 1:
  hasil = x + y
  print(f"hasil dari {x} ditambah dengan {y} adalah {hasil}")
elif operasi == 2:
  hasil = x - y
  print(f"hasil dari {x} dikurangi dengan {y} adalah {hasil}")
elif operasi == 3:
  hasil = x * y
  print(f"hasil dari {x} dikalikan dengan {y} adalah {hasil}")
elif operasi == 4:
  hasil = x / y
  print(f"hasil dari {x} dibagi dengan {y} adalah {hasil}")
elif operasi == 5:
  hasil = x ** y
  print(f"hasil dari {x} dipangkatkan {y} adalah {hasil}")
else:
  print("masukan tidak valid mulai ulang program")