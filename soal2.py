# import math
print("=========== Selamat datang di toko andi tersenyum ===========")
total = int(input("Total Belanja : "))
diskper = int(total-(total*0.02))
diskdua = int(total-(total*0.05))
disktiga = int(total-(total*10/100))
if total < 100000:
    print("Tidak ada diskon Maka yang anda bayar adalah Rp ",total)
elif total <= 100000:
    print("Biaya yang harus di bayarkan adalah Rp ",diskper)
elif total >= 500000:
    print("Biaya yang harus di bayarkan adalah Rp ",diskdua)
elif total >= 1000000:
    print("Biaya yang harus di bayarkan adalah Rp ",disktiga)
    
