import math

# 1. Luas permukaan kubus
def luas_kubus(s):
    return 6 * s * s

# 2. Luas permukaan balok
def luas_balok(p, l, t):
    return 2 * (p*l + p*t + l*t)

# 3. Luas permukaan prisma segitiga
def luas_prisma_segitiga(luas_alas, keliling_alas, t):
    return (keliling_alas * t) + 2 * luas_alas

# 4. Luas permukaan limas segitiga
def luas_limas_segitiga(luas_alas, luas_sisi_tegak):
    return luas_alas + luas_sisi_tegak

# 5. Luas permukaan tabung
def luas_tabung(r, t):
    return 2 * math.pi * r * (r + t)

# 6. Luas permukaan kerucut
def luas_kerucut(r, s):
    return math.pi * r * (r + s)  

# 7. Luas permukaan bola
def luas_bola(r):
    return 4 * math.pi * r * r

# 8. Luas permukaan prisma segi empat
def luas_prisma_segiempat(luas_alas, keliling_alas, t):
    return 2 * luas_alas + keliling_alas * t

# 9. Luas permukaan limas segi empat
def luas_limas_segiempat(luas_alas, luas_sisi_tegak):
    return luas_alas + luas_sisi_tegak

# 10. Luas permukaan prisma segi lima
def luas_prisma_segilima(luas_alas, keliling_alas, t):
    return 2 * luas_alas + keliling_alas * t