#kali ini kita lakukan hal hal unik dengan string

kursus = "Python untuk pemula"

#1. upper = adalah memaksa isi kursus untuk menjadi kapital semua
print(kursus.upper())
print('-' * 20)
#2. lower = kebalika dari upper, ini memaksa menjadi semua nya huruf kecil
BESAR = "INI ADALAH HURUF BESAR YANG DIPAKSA MENJADI KECIL"
print(BESAR.lower())
print('-' * 20)
#3 find = mencari unsur huruf yang ada di kalimat yang ada di variabel
#4 replace = menggantikan kata menjadi kata lain dengan format '(variabel.replace("kata", "kata ganti")'
#ingat, PYTHON MENGHITUNG DARI 0! JADINYA 0123  
kata = "JavaScript for Beginners"
print(kata.find('a'))
print(kata.replace("for", "4"))

#5 in = mengecek apakah kata tersebut ada atau tidak
#jika ada maka true jika tidak ada maka false
contoh = "di sini kota ini"
print("di" in contoh)
print("desa" in contoh)
