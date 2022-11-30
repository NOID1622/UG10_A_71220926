nilaiSatu = int(input("Masukan Nilai soal 1 :"))
nilaiDua = int(input("Masukan Nilai soal 2 :"))
nilaiTiga = int(input("Masukan Nilai soal 3 :"))
nilaiEmpat = int(input("Masukan Umur anda : "))
jumlahSatu = (nilaiSatu*50/100)
jumlahDua = (nilaiDua*30/100)
jumlahTiga = (nilaiTiga*20/100)
ratanilai = (jumlahSatu+jumlahDua+jumlahTiga)
print("Rata-rata nilai anda : " + str(ratanilai))
if nilaiEmpat <= 25 :
    if ratanilai >= 80:
        print("Selamat anda lulus")
    else: 
        print("Coba lagi tahun depan")
else : 
    if ratanilai >= 90:
        print("Selamat anda Lulus")
    else : 
        print("Coba lagi tahun depan")
