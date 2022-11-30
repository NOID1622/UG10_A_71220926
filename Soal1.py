nameMaha = input("Masukan Nama Mahasiswa : ")
nimMaha = input("Masukan Nim Mahasiswa : ")
if nimMaha [0:2] == "71" and int(nimMaha[2:4]) <=22 and int(nimMaha[2:4]) >=20:
    print(f'{nameMaha}, Merupakan mahasiswa informatika angkatan 20 hingga 22')
else:
    print(f'{nameMaha},bukan merupakan mahasiwa informatika angkatan 20 hingga 22')