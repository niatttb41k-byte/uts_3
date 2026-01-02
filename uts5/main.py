import os
from bangun_ruang import *
while True:
    input()
    os.system("clear")
    pil = int(input("pilihan : "))

    if pil == 1:
        s = int(input("masukkan sisi : "))
        print("Luas =", luas_kubus(s))

    elif pil == 2:
        p = int(input("masukkan panjang : "))
        l = int(input("masukkan lebar   : "))
        t = int(input("masukkan tinggi  : "))
        print("Luas =", luas_balok(p, l, t))

    elif pil == 3:
        luas_alas = int(input("masukkan luas alas : "))
        keliling = int(input("masukkan keliling alas : "))
        t = int(input("masukkan tinggi : "))
        print("luas =" , luas_prisma_segitiga(luas_alas,                          keliling, t))

    elif pil == 4:
        luas_alas = int(input("masukkan luas alas : "))
        luas_sisi = int(input("masukkan luas sisi tegak            : "))
        print("luas =" ,luas_limas_segitiga(luas_alas,               luas_sisi))


    elif pil == 5:
        r = int(input("masukkan jari-jari : "))
        t = int(input("masukkan garis pelukis : "))
        print("Luas =", luas_tabung(r, t))

    elif pil == 6:
        r = int(input("masukkan jari-jari : "))
        s = int(input("masukkan garis pelukis : "))
        print("Luas =", luas_kerucut(r, s))

    elif pil == 7:
        r = int(input("masukkan jari-jari : "))
        print("Luas =", luas_bola(r))

    elif pil == 8:
        luas_alas = int(input("masukkan luas alas : "))
        keliling = int(input("masukkan keliling alas : "))
        t = int(input("masukkan tinggi : "))
        print("luas =" ,luas_prisma_segiempat(luas_alas,keliling,          t))
        
    elif pil == 9:
        luas_alas = int(input("masukkan luas alas : "))
        luas_sisi_tegak = int(input("masukkan luas sisi           tegak : "))
        print("luas =" , luas_limas_segiempat(luas_alas,                         luas_sisi_tegak))
        
    elif pil == 10:
        luas_alas = int(input("masukkan luas alas : "))
        keliling = int(input("masukkan keliling alas : "))
        t = int(input("masukkan tinggi : "))
        print("luas =" , luas_prisma_segilima(luas_alas,                           keliling, t))
                        
    else:        
        break    
    input()  
        