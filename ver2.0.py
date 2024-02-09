import sqlite3
import os
import time
import datetime
import veri_getir


class stok():
    def __init__(self,veritabanı,urun_adı,urun_tarih,urun_miktar,im):
        self.veritabanı=veritabanı
        self.urun_adı=urun_adı
        self.urun_tarih=urun_tarih
        self.urunmiktar=urun_miktar
        self.im=im


    def baglantı(self):
        self.veritabanı = sqlite3.connect("urun.db")
        self.im = self.veritabanı.cursor()



    def tabloolustur(self):
        self.im.execute("CREATE TABLE İF NOT EXİST urunler""(urun_adı,urun_tarih,urun_miktar)""")

    def veri_ekle(self,kayıt,sayac):
        self.urun_adı=input("Eklenecek Ürün Adını Yazınız")
        self.urun_tarih=datetime.datetime.now()
        self.urunmiktar=int(input("Eklenecek Ürün Miktarını Belirtin"))
        kayıt=self.im.execute("INSERT INTO urunler(self.urun_adı,self.urun_tarih,self.urun_miktrar),(?,?,?)")
        sayac=1
        if kayıt == sayac:
            print("Veriler Başarı ile Eklendi")
        else:
            print("Veri Eklenirken Bir Hata İle Karşılaşıldı!")

    def veri_getir(self):
        data=self.im.execute("SELECT * FROM urunler")
        getir=data.fetch()
        print("Çağırılan Veriler"+getir)






























