# AYBÜKE TÜRİDİ YAZILIM MÜHENDİSLİĞİ 2.SINIF 220502005
# ELİF BEYZA BEYAZ YAZILIM MÜHENDİSLİĞİ 2.SINIF 220502033

from sympy import fibonacci
renkler = {"kirmizi": "\033[31m","sari": "\033[33m","reset": "\033[0m"}

def menu():
    while 1:  #menü içindeki döngüyü sağlamak için while true ya da 1 olmalı olmaz ise break fonksiyonu çalışmaz.
        # Görsel menü kodları
        print(f"{renkler['sari']}***////MENÜYE HOŞGELDİNİZ////***{renkler['reset']}".center(100))
        print("\n")
        print(f"{renkler['sari']}Seçeneklerimiz:{renkler['reset']}".center(100))
        print("1")
        print(f"{renkler['kirmizi']}k’nıncı En Küçük Elemanı Bulma{renkler['reset']}")
        print("2")
        print(f"{renkler['kirmizi']}En Yakın Çifti Bulma{renkler['reset']}")
        print("3")
        print(f"{renkler['kirmizi']}Bir Listenin Tekrar Eden Elemanlarını Bulma{renkler['reset']}")
        print("4")
        print(f"{renkler['kirmizi']}Matris Çarpımı{renkler['reset']}")
        print("5")
        print(f"{renkler['kirmizi']}Bir Text Dosyasındaki Kelimelerin Frekansını Bulma{renkler['reset']}")
        print("6")
        print(f"{renkler['kirmizi']}Liste İçinde En Küçük Değeri Bulma{renkler['reset']}")
        print("7")
        print(f"{renkler['kirmizi']}Karekök Fonksiyonu{renkler['reset']}")
        print("8")
        print(f"{renkler['kirmizi']}En Büyük Ortak Bölen{renkler['reset']}")
        print("9")
        print(f"{renkler['kirmizi']}Asallık Testi{renkler['reset']}")
        print("10.")
        print(f"{renkler['kirmizi']}Daha Hızlı Fibonacci Hesabı{renkler['reset']}")
        print("11")
        print(f"{renkler['kirmizi']}Çıkış{renkler['reset']}")
        print()
        secim = input("Lütfen bir işlem seçin (1<-->11): ")
        # Kontrol yapıları ile menüden seçim yaptırıp oluşturulan fonksiyonları çağıracağız ve çalışmasını sağlayacağız.
        if secim == "1":
            kacinci = input("Kaçıncı küçük sayıyı bulmak istediğinizi seçiniz:")
            liste0 = input("Bir liste giriniz:")
            liste = []
            for i in liste0.split(","):
                liste.append(i)

            print(kacinci_kucuk(kacinci, liste))

        elif secim == "2":
            sayi = int(input("Bir sayı giriniz:"))
            liste0 = input("Bir liste giriniz:")
            liste = []
            for i in liste0.split(","):
                liste.append(int(i))

            print(en_yakin_ciftler(sayi, liste))

        elif secim == "3":
            liste0 = input("Bir liste giriniz:")
            liste = []
            for i in liste0.split(","):
                liste.append(int(i))

            print(tekrar_eden(liste))

        elif secim == "4":
            satir_sayisi1 = int(input("Matrisin satır sayısını girin: "))
            sutun_sayisi1 = int(input("Matrisin sütun sayısını girin: "))

            matris1 = []
            for i in range(satir_sayisi1):
                satir = []
                for j in range(sutun_sayisi1):
                    deger = int(input(f"({i + 1}, {j + 1}) elemanını girin: "))
                    satir.append(deger)
                matris1.append(satir)
            satir_sayisi2 = int(input("Matrisin satır sayısını girin: "))
            sutun_sayisi2 = int(input("Matrisin sütun sayısını girin: "))
            matris2 = []
            for i in range(satir_sayisi2):
                satir = []
                for j in range(sutun_sayisi2):
                    deger = int(input(f"({i + 1}, {j + 1}) elemanını girin: "))
                    satir.append(deger)
                matris2.append(satir)

            print(matris_carpimi(matris1, matris2))

        elif secim == "5":
            dosya_konumu = "metin.txt"
            farkli_elemanlar, frekanslar = kelime_frekans(dosya_konumu)

            for kelime, frekans in zip(farkli_elemanlar, frekanslar):
                print(f"{kelime}: {frekans}")

        elif secim == "6":
            liste0 = input("Bir liste giriniz:")
            liste = []
            for i in liste0.split(","):
                liste.append(int(i))

            print(en_kucuk_deger(liste))

        elif secim == "7":
            N = float(input("N değeri giriniz:"))
            x0 = float(input("x0 değeri giriniz:"))
            sonuc, iterasyon = karekok_bul(N, x0)
            print(f"Karekök: {sonuc:}, iterasyon sayısı: {iterasyon}")

        elif secim == "8":
            sayi1 = int(input("Birinci sayiyi giriniz:"))
            sayi2 = int(input("İkinci sayiyi giriniz"))

            print(ebob(sayi1, sayi2))

        elif secim == "9":
            sayi = int(input("Asal olup olmadığını öğrenmek istediğiniz sayıyı giriniz:"))

            print(asallik(sayi))

        elif secim == "10":
            sayi = int(input("Fibonacci değerini öğrenmek istediğiniz sayıyı giriniz:"))
            # k ,fib(k) ve fib(k-1) için başlangıç değerleri:
            sayi2 = fibonacci((sayi - sayi) + 1)
            sayi3 = fibonacci((sayi - sayi) + 1)
            sayi4 = fibonacci(sayi - sayi)

            print(hizlandirici(sayi, sayi2, sayi3, sayi4))

        elif secim == "11":
            print("Programdan çıkılıyor.")
            break

        else:
            print("Geçersiz seçim. Lütfen seçeneklerden birini giriniz.")


# İSTENEN DURUMLARIN FONKSİYONLARI

# 1
def kacinci_kucuk(sayi, liste):
    if int(sayi) <= 0 or int(sayi) > len(liste):
        return "Liste ve sayı değelerini kontrol ediniz."

    siralama = sorted(liste)
    kacinci_kucuk_sonuc = siralama[int(sayi) - 1]
    return kacinci_kucuk_sonuc

# 2
def en_yakin_ciftler(sayi, liste):
    if len(liste) < 2:
        return "Listeye daha fazla eleman giriniz"
    en_yakin = None
    en_yakin_cift = None
    for i in range(0, len(liste)):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]
            fark = abs(sayi - toplam)
            if en_yakin is None or fark < abs(sayi - en_yakin):
                en_yakin = toplam
                en_yakin_cift = liste[i], liste[j]
    if en_yakin_cift is not None:
        en_yakin_ciftler_sonuc = str(en_yakin_cift[0]) + " ve " + str(en_yakin_cift[1])
        return en_yakin_ciftler_sonuc

    return "Uygun çift bulunamadı"


# 3
def tekrar_eden(liste):
    tekrar_edenler = list(set(elemanlar for elemanlar in liste if liste.count(elemanlar) > 1))
    return tekrar_edenler

#4
def matris_carpimi(liste1, liste2):
    if len(liste1[0] or liste1[1]) == len(liste2):
        matris = []
        sutunlar = list(zip(*liste2))
        zip1 = list(zip(liste1[0],sutunlar[0]))
        zip2 = list(zip(liste1[0],sutunlar[1]))
        sonuc1 = sum(x * y for x, y in zip1)
        sonuc2 = sum(x * y for x, y in zip2)
        carpim1 = [sonuc1,sonuc2]
        zip3 = list(zip(liste1[1],sutunlar[0]))
        zip4 = list(zip(liste1[1],sutunlar[1]))
        sonuc3 = sum(x * y for x, y in zip3)
        sonuc4 = sum(x * y for x, y in zip4)
        carpim2 = [sonuc3,sonuc4]
        matris.append(carpim1)
        matris.append(carpim2)
        return matris
    else:
        return "Matris çarpımı yapabilmek için ilk matrisin sütun sayısı, ikinci matrisin satır sayısına eşit olmalıdır."

#5
def kelime_frekans(dosya_konumu):
    with open(dosya_konumu, 'r') as dosya:
        metin = dosya.read()
        kelimeler = metin.split()
        farkli_elemanlar = set(kelimeler)

    frekanslar = list(map(lambda kelime: kelimeler.count(kelime), farkli_elemanlar))
    return farkli_elemanlar, frekanslar

#6
def en_kucuk_deger(liste):
    if len(liste) == 0:
        return None
    else:
        en_kucuk = liste[0]
        for i in range(1, len(liste)):
            if en_kucuk >= en_kucuk_deger(liste[i:]):
                en_kucuk = en_kucuk_deger(liste[i:])
        return en_kucuk

#7
def karekok_bul(N, x0, tol=1e-10, maxiter=10):
    ilk_tahmin = x0
    iterasyon = 0
    while True:
        yeni_tahmin = 0.5 * (ilk_tahmin + N / ilk_tahmin)
        hata = abs(yeni_tahmin**2 - N)
        ilk_tahmin = yeni_tahmin
        iterasyon += 1
        if hata < tol:
            break
        if maxiter <= iterasyon:
            print(f"{maxiter} iterasyonda sonuca ulaşılamadı. 'ilk tahmin' veya 'maxiter' değerlerini değiştirin.")
            return ilk_tahmin, iterasyon

    return ilk_tahmin, iterasyon

#8
def bolen_bul(sayi):
    bolen_listesi = []
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            bolen_listesi.append(i)
    return bolen_listesi

def en_buyuk_deger(liste):
    if len(liste) == 0:
        return None
    else:
        en_buyuk = liste[0]
        for i in range(1, len(liste)):
            if en_buyuk <= en_buyuk_deger(liste[i:]):
                en_buyuk = en_buyuk_deger(liste[i:])
        return en_buyuk

def ebob(int1, int2):
    liste1 = bolen_bul(int1)
    liste2 = bolen_bul(int2)
    ortak_elemanlar = [eleman for eleman in liste1 if eleman in liste2]

    if len(ortak_elemanlar) == 0:
        return None

    return en_buyuk_deger(ortak_elemanlar)

#9
def asallik(sayi,bolen=2):
    if isinstance(sayi, int):
        if sayi <= 1:
            return False
        elif sayi == 2:
            return True
        elif bolen < sayi:
            if sayi % bolen == 0:
                return False
            return asallik(sayi, bolen + 1)
        else:
            return True
    return False

#10
def hizlandirici(int1, int2, int3, int4):
    if int2 == int1:
        return int3
    else:
        return hizlandirici(int1, int2 + 1, int3 + int4, int3)





menu()
