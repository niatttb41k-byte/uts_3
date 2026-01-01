import os 
from luas_bangun_datar import *

while True:
    os.system("clear")
	
    pil = int(input("pilihan : "))
    if pil == 1:
        sisi = int(input("masukkan sisi : "))
        print(luas_persegi(sisi))
		
    elif pil == 2:
        panjang = int(input("masukkan panjang : "))
        lebar = int(input("masukkan lebar : "))            
        print(luas_persegi_panjang(panjang,lebar))
	
    elif pil == 3:
            alas = int(input("masukkan alas : "))
            tinggi = int(input("masukkan tinggi : "))
            print(luas_segitiga(alas,tinggi))
            
    elif pil == 4:
            jari_jari = int(input("masukkan jari_jari : "))
            jari_jari = int(input("masukkan jari_jari : "))
            print(luas_lingkaran(jari_jari,jari_jari))
    elif pil == 5:
            alas       = int(input("masukkan alas : "))
            tinggi     = int(input("masukkan tinggi :"))
            print(luas_jajargenjang(alas,tinggi))
    elif pil == 6:
            alas = int(input("masukkan sisi sejajar_a : "))
            b      = int (input("masukkan sisi sejajar_b : "))
            tinggi = int(input("masukkan tinggi"))
            print(luas_trapesium(sisi_a ,sisi_b ,tinggi))
           
    elif pil == 7:
            d1 = int(input("masukkan diagonal d1 : "))
            d2 = int(input("masukkan diagonal d2 : "))
            print(luas_belah_ketupat(d1,d2))
          
    elif pil == 8:
            d1 = int(input("masukkan diagonal d1 : "))
            d2 = int(input("masukkan diagonal d2 : "))
            print(luas_layang_layang(d1,d2))
          
    elif pil == 9:
            jari_jari = int(input("masukkan jari_jari : "))
            print(luas_setengah_lingkaran(jari_jari))
            
    elif pil == 10:
            sisi = int(input("masukkan sisi : "))
            
            print(luas_segi_enam(sisi))
       
    else:
        break
        
    input()
    