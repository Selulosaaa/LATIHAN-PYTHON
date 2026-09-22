#kondisi adalah percabangan python pakai if-elif-else
#Pengambilan keputusan (kondisi if) digunakan untuk mengantisipasi kondisi yang terjadi saat jalanya program dan menentukan tindakan 
#apa yang akan diambil sesuai dengan kondisi.
x = 18
if x >= 18:
  print("kamu sudah dewasa")
else:
  print("kamu belum dewasa")

#elif pengambilan lebih dari satu
temperatur = 20

if temperatur > 35:
  print("hari yang panas!")
  print("minum air yang banyak!")
elif temperatur > 25:
  print("hari yang cerah!")
  print("halo dunia! selamat siang!")
else:
  print("cuaca yang dingin! segera pakai jaket!")

#disini ada ternary operator
#sama seperti if-elif-else. namun hanya satu baris!
age = 16
verifikasi = "Dewasa" if age >= 18 else "Anak dibawah umur"
print(verifikasi)