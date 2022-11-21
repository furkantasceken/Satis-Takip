import os
import ProductGeneric
import CustomerGeneric
import PriceGeneric
import InvoiceGeneric

pg=ProductGeneric
cg=CustomerGeneric
prg=PriceGeneric
ig=InvoiceGeneric

def Main():
    os.system('cls')
    while True:
        print("""
1 - ÜRÜN TANIMLAMA
2 - FİYAT TANIMLAMA
3 - MÜŞTERİ TANIMLAMA
4 - FATURA GİRİŞİ
5 - ÇIKIŞ
        """)
        s = input("Yapmak istediğiniz işlemi seçiniz : ")
        os.system('cls')
        if s=='1':
            PnlProduct()
        elif s=='2':
            PnlPrice()
        elif s=='3':
            PnlCustomer()
        elif s=='4':
            PnlInvoice()
        elif s=='5':
            os.system('cls')
            exit()
        else:
            os.system('cls')
            print("Hatalı giriş yaptınız.")

def PnlProduct():
    os.system('cls')
    pg.ListProduct()
    while True:
        print("""
1 - ÜRÜN EKLE
2 - ÜRÜN GÜNCELLE
3 - ÜRÜN SİL
4 - GERİ
            """)
        s = input("Yapmak istediğiniz işlemi seçiniz : ")
        if s == '1':
            PnlAddProduct()
        elif s == '2':
            PnlUpdateProduct()
        elif s == '3':
            PnlRemoveProduct()
        elif s == '4':
            Main()
        else:
            os.system('cls')
            print("Hatalı giriş yaptınız.")

def PnlPrice():
    os.system('cls')
    prg.ListProduct()
    while True:
        print("""
    1 - FIYAT EKLE
    2 - FIYAT BILGISI GUNCELLE
    3 - FIYAT SİL
    4 - GERİ
                """)
        s = input("Yapmak istediğiniz işlemi seçiniz : ")
        if s == '1':
            PnlAddPrice()
        elif s == '2':
            PnlUpdatePrice()
        elif s == '3':
            PnlRemovePrice()
        elif s == '4':
            Main()
        else:
            os.system('cls')
            print("Hatalı giriş yaptınız.")

def PnlCustomer():
    os.system('cls')
    cg.ListProduct()
    while True:
        print("""
    1 - MUSTERİ EKLE
    2 - MÜŞTERİ BİLGİSİ GÜNCELLE
    3 - MÜŞTERİ SİL
    4 - GERİ
                """)
        s = input("Yapmak istediğiniz işlemi seçiniz : ")
        if s == '1':
            PnlAddCustomer()
        elif s == '2':
            PnlUpdateCustomer()
        elif s == '3':
            PnlRemoveCustomer()
        elif s == '4':
            Main()
        else:
            os.system('cls')
            print("Hatalı giriş yaptınız.")

def PnlInvoice():
    pass

#   ----------------------Product Table Information--------------------------   #

def PnlAddProduct():
    os.system('cls')
    while True:
        pg.ListProduct()
        print("\n")
        uad = input("Ürün adını girin : ")
        ustkdv = input("Satış kdv oranını % olarak girin : ")
        ualkdv = input("Alış kdv oranını % olarak girin : ")
        pg.Add(uad,ustkdv,ualkdv)
        os.system('cls')
        print("Ürün başarıyla eklendi. Menüye dönülüyor..","\n")
        PnlProduct()

def PnlUpdateProduct():
    os.system('cls')
    while True:
        pg.ListProduct()
        print("\n")
        id=int(input("Ürün id giriniz: "))
        os.system('cls')
        pg.ListProducts(id)
        print("""
        1 - ÜRÜN ADI GÜNCELLE
        2 - ÜRÜN ALIŞ KDV GÜNCELLE
        3 - ÜRÜN SATIŞ KDV GÜNCELLE
        4 - ÜRÜN DURUM DEĞİŞTİRME4
        5 - GERİ
        """)
        secim = input("Hangi işlemi yapmak istersiniz? ")

        if secim=="1":
            os.system('cls')
            pg.ListProducts(id)
            print("\n")
            yeniAd=input("Yeni giriniz: ")
            pg.UpdateAd(id,yeniAd)
            os.system('cls')
            print("Ad başarıyla değiştirilmiştir. Üst menüye dönülüyor..","\n")
            PnlProduct()

        if secim == "2":
            os.system('cls')
            pg.ListProducts(id)
            print("\n")
            yeniAKdv=float(input("Yeni alış KDV değerini giriniz: "))
            pg.UpdateKdvAlis(id,yeniAKdv)
            os.system('cls')
            print("Alış KDV başarıyla değiştirilmiştir. Üst menüye dönülüyor..","\n")
            PnlProduct()

        if secim == "3":
            os.system('cls')
            pg.ListProducts(id)
            print("\n")
            yeniSKdv=float(input("Yeni satış KDV değerini giriniz: "))
            pg.UpdateKdvSatis(id,yeniSKdv)
            os.system('cls')
            print("Satış KDV başarıyla değiştirilmiştir. Üst menüye dönülüyor..","\n")
            PnlProduct()

        if  secim == "4":
            os.system('cls')
            pg.ListProducts(id)
            print("\n")
            yeniDurum = input("Yeni durumu giriniz (1=aktif, 0=pasif): ")
            pg.UpdateDurum(id, yeniDurum)
            os.system('cls')
            print("Durum başarıyla değiştirilmiştir. Üst menüye dönülüyor..","\n")
            PnlProduct()

        else:
            os.system('cls')
            PnlProduct()

def PnlRemoveProduct():
    os.system('cls')
    while True:
        pg.ListProduct()
        print("\n")
        id = int(input("Ürün id giriniz: "))
        pg.Remove(id)
        os.system('cls')
        print("Ürün başarıyla kaldırılmıştır. Üst menüye dönülüyor..","\n")
        PnlProduct()

#   ----------------------Price Table Information--------------------------   #

def PnlAddPrice():
    os.system('cls')
    while True:
        pg.ListProduct()
        print("\n")
        uid = input("Ürün ID'sini girin : ")
        fiyatsatis = input("Satış Fiyatını 'TL' olarak girin : ")
        fiyatalis = input("Alış Fiyatını 'TL' olarak girin : ")
        prg.Add(uid, fiyatsatis, fiyatalis)
        print("Fiyat başarıyla eklendi. Menüye dönülüyor..", "\n")
        PnlPrice()

def PnlUpdatePrice():
    os.system('cls')
    while True:
        prg.ListProduct()
        print("\n")
        id = int(input("Ürün id giriniz: "))
        os.system('cls')
        prg.ListProducts(id)
        print("""
            1 - SATIŞ FİYAT GÜNCELLE
            2 - ALIŞ FİYAT GÜNCELLE
            3 - FİYATI PASİFE AL
            4 - GERİ
            """)
        secim = input("Hangi işlemi yapmak istersiniz? ")

        if secim == "1":
            os.system('cls')
            prg.ListProducts(id)
            print("\n")
            yeniSfiyat = input("Yeni satış fiyatını giriniz: ")
            prg.UpdateFiyatSatis(id, yeniSfiyat)
            print("Satış Fiyatı başarıyla değiştirilmiştir. Üst menüye dönülüyor..", "\n")
            PnlPrice()

        if secim == "2":
            os.system('cls')
            prg.ListProducts(id)
            print("\n")
            yeniAfiyat = float(input("Yeni alış fiyatı giriniz: "))
            prg.UpdateFiyatAlis(id, yeniAfiyat)
            print("Alış fiyatı başarıyla değiştirilmiştir. Üst menüye dönülüyor..", "\n")
            PnlPrice()

        if secim == "3":
            os.system('cls')
            prg.ListProducts(id)
            print("\n")
            yeniPDurum = input("Yeni durumu giriniz (1=aktif, 0=pasif): ")
            prg.UpdateDurum(id, yeniPDurum)
            print("Durum başarıyla değiştirilmiştir. Üst menüye dönülüyor..", "\n")
            PnlPrice()

        if secim == "4":
            os.system('cls')
            PnlPrice()

def PnlRemovePrice():
    os.system('cls')
    while True:
        prg.ListProduct()
        print("\n")
        id = int(input("Ürün id giriniz: "))
        prg.Remove(id)
        print("Fiyat başarıyla kaldırılmıştır. Üst menüye dönülüyor..","\n")
        os.system('cls')
        PnlPrice()

#   ----------------------Customer Table Information--------------------------   #

def PnlAddCustomer():
    os.system('cls')
    while True:
        cg.ListProduct()
        print("\n")
        unvan = input("Ünvan giriniz : ")
        tcvn = input("TC Kimlik veya Vergi numarası giriniz : ")
        cg.Add(unvan, tcvn)
        os.system('cls')
        print("Müşteri başarıyla eklendi. Menüye dönülüyor..", "\n")
        PnlCustomer()

def PnlUpdateCustomer():
    os.system('cls')
    while True:
        cg.ListProduct()
        print("\n")
        id = int(input("Ürün id giriniz: "))
        os.system('cls')
        cg.ListProducts(id)
        print("""
                1 - UNVAN GÜNCELLE
                2 - TC KIMLIK VEYA VERGİ NUMARASI GÜNCELLE
                3 - DURUM GÜNCELLE
                4 - GERİ
                """)
        secim = input("Hangi işlemi yapmak istersiniz? ")

        if secim == "1":
            os.system('cls')
            cg.ListProducts(id)
            print("\n")
            yeniUnvan = input("Yeni ünvanı giriniz: ")
            cg.UpdateUnvan(id, yeniUnvan)
            os.system('cls')
            print("Ünvan başarıyla değiştirilmiştir. Üst menüye dönülüyor..", "\n")
            PnlCustomer()

        if secim == "2":
            os.system('cls')
            cg.ListProducts(id)
            print("\n")
            yeniTcvn = float(input("Yeni Tc Kimlik veya Vergi Numarasını giriniz: "))
            cg.UpdateTcvn(id, yeniTcvn)
            os.system('cls')
            print("İşlem başarıyla gerçekleştirilmiştir. Üst menüye dönülüyor..", "\n")
            PnlCustomer()

        if secim == "3":
            os.system('cls')
            cg.ListProducts(id)
            print("\n")
            yeniCDurum = input("Yeni durumu giriniz (1=aktif, 0=pasif): ")
            cg.UpdateDurum(id, yeniCDurum)
            os.system('cls')
            print("Durum başarıyla değiştirilmiştir. Üst menüye dönülüyor..", "\n")
            PnlCustomer()

        if secim == "4":
            os.system('cls')
            PnlCustomer()

def PnlRemoveCustomer():
    os.system('cls')
    while True:
        cg.ListProduct()
        print("\n")
        id = int(input("Ürün id giriniz: "))
        cg.Remove(id)
        os.system('cls')
        print("Ürün başarıyla kaldırılmıştır. Üst menüye dönülüyor..", "\n")
        PnlCustomer()


#   ----------------------Invoice Table Information--------------------------(EMPTY RIGHT NOW)   #

def PnlAddInvoice():
    pass

def PnlUpdateInvoice():
    pass

def PnlRemoveInvoice():
    pass


Main()