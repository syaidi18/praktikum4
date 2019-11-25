nilai = []
ulang = True

while ulang:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    tugas = int(input("Masukkan Nilai Tugas: "))
    uts = int(input("Masukkan Nilai UTS: "))
    uas = int(input("Masukkan Nilai UAS: "))
    akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)

    nilai.append([nama, nim, int(tugas), int(uts), int(uas), int(akhir)])
    if (input("Tambah data (y/t)?") == 't'):
        ulang = False

print("\nDaftar Nilai Mahasiswa")
print("====================================================================")
print("|No. |     Nama     |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir |")
print("====================================================================")
i = 0
for item in nilai:
    i += 1
    print("| {no:2d} | {nama:12s} | {nim:9s} | {tugas:7d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |"
          .format(no=i, nama=item[0], nim=item[1], tugas=item[2], uts=item[3], uas=item[4], akhir=item[5]))
print("====================================================================")
