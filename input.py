#input adalah cara untuk menerima apa yang diketik oleh user
#istiliah nya ini menyimpan sebuah pemberian oleh user dan biaanya input dopasang oleh variabel

nama =input("siapa nama kamu? ")
print("nama" + nama)
print("nama", nama)

#khusus untuk input nomor harus pakai 'int' untuk builangan ulat dan 'foloat' untuk bilangan yang ada koma nya
#karena python tidak bisa mengkonversi string ke int/float sendiri kadang juga harus dipaksa 'int()'
tahun = int(input("tahun lahirmu berapa?"))
umur = 2026 - int(tahun)

print(umur)