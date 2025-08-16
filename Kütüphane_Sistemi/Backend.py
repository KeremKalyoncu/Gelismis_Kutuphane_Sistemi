import sqlite3
import time
import logging
from pathlib import Path
import sys
Kod_Dizini =Path(__file__).resolve().parent
Path.mkdir(Kod_Dizini / "Veritabanı-Log-AdminLog",parents=True,exist_ok=True)  # Log dosyası ve veritabanı dosyalarının bulunduğu dizin / farklı bilgisayarlarda çalışması içinde resolve() kullandım.
Kod_Log_Dizini = Kod_Dizini / "Veritabanı-Log-AdminLog"  # Log dosyalarının bulunduğu dizin


# Loglama ayarları
logging.basicConfig(
    filename=Kod_Log_Dizini / 'kütüphane_sistemi.log',
    level=logging.INFO,
    format="[%(asctime)s] -- [%(levelname)s] : %(message)s",
)


class kitap():
    def __init__(self,ad,yazar,yili,dagitim,baski,tarih,buradami=1,kimde=None):
        self.ad = ad
        self.yazar = yazar
        self.yili = yili
        self.dagitim = dagitim
        self.baski = baski
        self.tarih = tarih if tarih else time.strftime("%Y-%m-%d %H:%M:%S")  # Tarih bilgisi yoksa mevcut tarih kullanılır
        self.burdami = buradami
        self.kimde = kimde

    def __str__(self):
        return (f"Kitap Adi : {self.ad} \n"
                f"Yazar : {self.yazar} \n"
                f"Yili : {self.yili} \n"
                f"Dagitim Şirketi : {self.dagitim} \n"
                f"Baski Sayisi : {self.baski} \n"
                f"Eklenilme Tarihi : {self.tarih} \n"
                f"Kütüphanedemi = {'evet' if self.burdami == 1 else 'hayir'} \n" 
                f"Kimde : {'Kütüphanede' if self.kimde == None else self.kimde} \n")
    
class Kutuphane():
    def __init__(self):
        self.baglanti_oldumu = False

    def baglan(self):
        self.baglanti = sqlite3.connect(Kod_Log_Dizini / "veritabani.db") # Veritabanı dosyası
        self.islem = self.baglanti.cursor()
        self.islem.execute("CREATE TABLE IF NOT EXISTS kitaplar (ad TEXT , yazar TEXT , yili INT , dagitim TEXT , baski INT , tarih TEXT, burdami INT, kimde TEXT)")
        self.baglanti.commit()
        

        self.logbaglanti = sqlite3.connect(Kod_Log_Dizini / "log.db") # Log dosyası
        self.logislem = self.logbaglanti.cursor()
        self.logislem.execute("CREATE TABLE IF NOT EXISTS log (islem TEXT, kitap_ad TEXT, yazar TEXT, yil INT, dagitim TEXT, baski INT, islem_tarihi TEXT, kod INT)")
        self.logbaglanti.commit()

        self.baglanti_oldumu = True


    def baglantikes(self): # Bağlantıyı kapatır
        self.islem.close()
        self.baglanti.close()
        self.logislem.close()
        self.logbaglanti.close()
        self.baglanti_oldumu = False



    def Veritabani_Ekle(self,islem,veri,birim1,birim2=None):
     try:
        metin = ""
        if birim2 == None:
            if islem == 1: # Kitap ekleme işlemi
                metin = f"{birim1} adli kitap eklendi."
            elif islem == 2: # Kitap sorgulama işlemi
                metin = f"{birim1} adli kitap sorgulandi."
            elif islem == 3: # Kitap silme işlemi
                metin = f"{birim1} Veri Tabanindan silindi"
            elif islem == 6: # Kitap iade alma işlemi
                metin = f"{birim1} adli kitap kütüphaneye iade edildi."
        else :
            if islem == 4: # Kitap güncelleme işlemi
                metin = f"{birim1} adli kitabin {birim2} bilgisi güncellendi."
            elif islem == 5: # Kitap ödünç verme işlemi
                metin = f"{birim1} adli kitap {birim2} kişisine ödünç verildi."
        islemtarih = time.strftime("%Y-%m-%d %H:%M:%S") # Log kaydi için tarih
        self.logislem.execute("INSERT INTO log VALUES(?,?,?,?,?,?,?,?)",(metin,veri[0],veri[1],veri[2],veri[3],veri[4],islemtarih,islem))
        self.logbaglanti.commit()
        logging.info(metin)
     except Exception:
        logging.error("Veritabanı ekleme işlemi sırasında bir hata oluştu.", exc_info=True)
        sys.exit(1)
        


    def kitap_ekle(self, kitapbilgileri): # Kitap ekleme işlemi
        try:
         eklekitap = kitap(kitapbilgileri[0],kitapbilgileri[1],kitapbilgileri[2],kitapbilgileri[3],kitapbilgileri[4], kitapbilgileri[5],1,None)
         varmi = self.islem.execute("SELECT ad FROM kitaplar WHERE ad = ?",(eklekitap.ad,))
         varmi = varmi.fetchone()
         if (varmi):
             print("Bu kitap zaten eklenmiş.")
         else:
             print("Kitap ekleniyor")
             self.islem.execute("INSERT INTO kitaplar VALUES(?,?,?,?,?,?,?,?)",(eklekitap.ad,eklekitap.yazar,eklekitap.yili,eklekitap.dagitim,eklekitap.baski,eklekitap.tarih,eklekitap.burdami,eklekitap.kimde))
             self.baglanti.commit()
             time.sleep(2)
             self.Veritabani_Ekle(1, [eklekitap.ad, eklekitap.yazar, eklekitap.yili, eklekitap.dagitim, eklekitap.baski], eklekitap.ad)
             logging.info(f"{eklekitap.ad} adli kitap eklendi.")
             print("Kitap başariyla eklendi.")
        except:
            sys.stderr.write("Kitap eklenirken bir hata oluştu. Lütfen tekrar deneyin.\n")
            logging.error("Kitap eklenirken bir hata oluştu.", exc_info=True)
            sys.exit(1)
            

    
    def kitap_sorgula(self, deger,neye): # Kitap sorgulama işlemi
        try:
         ss = f"SELECT * FROM kitaplar WHERE {neye} = ?"
         self.islem.execute(ss,(deger,))
         sonuc = self.islem.fetchall()
         for i in sonuc:
            sorgula = kitap(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print(sorgula)
         self.Veritabani_Ekle(2, [sorgula.ad, sorgula.yazar, sorgula.yili, sorgula.dagitim, sorgula.baski], deger)
         logging.info(f"{deger} adli kitap {neye} alaninda sorgulandi.")
         print("Kitap sorgulandi.")
        except:
            sys.stderr.write("Kitap Bulunamadı.\n")
            logging.error("Aranan Kitap Bulunamadı", exc_info=True)
            sys.exit(1)

    
    def kitap_silme(self,deger,neye): # Kitap silme işlemi
        try:
           sas = f"SELECT * FROM kitaplar WHERE {neye} = ? "
           self.islem.execute(sas,(deger,))
           ssa = self.islem.fetchall()
           if len(ssa) == 0:
               print("Silinecek kitap bulunamadi.")
           else:
              print("Kitap siliniyor")
              time.sleep(2)
              ss = f"DELETE FROM kitaplar WHERE {neye} = ? "
              self.islem.execute(ss,(deger,))
              self.baglanti.commit()
              self.Veritabani_Ekle(3, [ssa[0][0], ssa[0][1], ssa[0][2], ssa[0][3], ssa[0][4]], deger)
              logging.info(f"{deger} adli kitap {neye} alaninda silindi.")
              print("Kitap silindi.")
        except:
            sys.stderr.write("Degişken adi yanliş girildi. Tekrar deneyin.\n")
            logging.error("Kitap silinirken bir hata oluştu.", exc_info=True)
            sys.exit(1)
    
    def kitap_guncelle(self, neye,deger, neye2,deger2,neyini, yeni_deger): # Kitap güncelleme işlemi
        try:
            kontrol = [neye,neye2,neyini]
            if all(x in ["ad", "yazar", "yili", "dagitim", "baski"] for x in kontrol):
             self.islem.execute(f"SELECT * FROM kitaplar WHERE {neye} = ? AND {neye2} = ?", (deger,deger2))
             sonuc = self.islem.fetchall()
             self.Veritabani_Ekle(4, [sonuc[0][0], sonuc[0][1], sonuc[0][2], sonuc[0][3], sonuc[0][4]], deger, deger2)
             logging.info(f"{deger} adli kitabin {neyini} bilgisi {deger2} alaninda güncellendi.")
             ss = f"UPDATE kitaplar SET {neyini} = ? WHERE {neye} = ? and {neye2} = ?"
             self.islem.execute(ss, (yeni_deger, deger, deger2))
             self.baglanti.commit()
             print("Kitap bilgisi güncellendi.")
            else:
                print("Güncelleme işlemi için geçersiz degişken adi girdiniz. Lütfen tekrar deneyin.")
        except: 
            sys.stderr.write("Güncelleme sirasinda bir hata oluştu. Lütfen tekrar deneyin. \n")
            logging.error("Kitap güncelleme işlemi sırasında bir hata oluştu.", exc_info=True)
            sys.exit(1)
    
    def tum_kitaplari_listele(self): # Tüm kitapları listeleme işlemi
        try:
            self.islem.execute("SELECT * FROM kitaplar")
            kitaplar = self.islem.fetchall()
            if (kitaplar == []):
                print("Kütüphanede hiç kitap bulunmamaktadir.")
            else:
                for kitapliste in kitaplar:
                    k = kitap(kitapliste[0], kitapliste[1], kitapliste[2], kitapliste[3], kitapliste[4], kitapliste[5], kitapliste[6], kitapliste[7])
                    print(k, "\n")
                logging.info("Tüm kitaplar listeleme işlemi başarıyla tamamlandı.")
        except:
            sys.stderr.write("Kitaplar listelenirken bir hata oluştu. Lütfen tekrar deneyin. \n")
            logging.error("Kitaplar listelenirken bir hata oluştu.", exc_info=True)
            sys.exit(1)
    
    def oduncver(self,kitap_ad,kim): # Kitap ödünç verme işlemi
        try:
            self.islem.execute("SELECT * FROM kitaplar WHERE ad = ?",(kitap_ad,))
            kitap = self.islem.fetchall()
            self.Veritabani_Ekle(5, [kitap[0][0], kitap[0][1], kitap[0][2], kitap[0][3], kitap[0][4]], kitap_ad, kim)
            self.islem.execute("UPDATE kitaplar SET burdami = ? , kimde = ? WHERE ad = ?",(0,kim,kitap_ad))
            self.baglanti.commit()
            logging.info(f"{kitap_ad} adli kitap {kim} kişisine ödünç verildi.")
            print(f"{kitap_ad} adli kitap {kim} kişisine ödünç verildi.")
        except:
            sys.stderr.write("Ödünç verme işlemi sirasinda bir hata oluştu. Lütfen tekrar deneyin. \n")
            logging.error("Ödünç verme işlemi sırasında bir hata oluştu.", exc_info=True)
            sys.exit(1)
    
    def oduncal(self,kitap_ad): # Kitap iade alma işlemi
        try:
            self.islem.execute("UPDATE kitaplar SET burdami = ? , kimde = ? WHERE ad = ? ",(1,None,kitap_ad))
            self.baglanti.commit()
            self.islem.execute("SELECT * FROM kitaplar WHERE ad = ?",(kitap_ad,))
            kitap = self.islem.fetchall()
            self.Veritabani_Ekle(6, [kitap[0][0], kitap[0][1], kitap[0][2], kitap[0][3], kitap[0][4]], kitap_ad)
            logging.info(f"{kitap_ad} adli kitap kütüphaneye iade edildi.")
        except:
            sys.stderr.write("Ödünç alma işlemi sirasinda bir hata oluştu. Lütfen tekrar deneyin. \n")
            logging.error("Ödünç alma işlemi sırasında bir hata oluştu.", exc_info=True)
            sys.exit(1)

    
    def log_listele(self,nekadar): # Logları listeleme işlemi
        try:
            self.logislem.execute("SELECT * FROM log")
            self.loglar = self.logislem.fetchall()
            nekadar = min(nekadar, len(self.loglar))
            for i in range(max(0, len(self.loglar)-nekadar), len(self.loglar)):
             log = self.loglar[i]
             print(f"İşlem: {log[0]} \n, Kitap Adı: {log[1]} \n , Yazar: {log[2]} \n, Yıl: {log[3]} \n, Dağıtım: {log[4]} \n, Baskı: {log[5]} \n, İşlem Tarihi: {log[6]} \n, Kod: {log[7]} \n")
            logging.info(f"Son {nekadar} log kaydı başarıyla listelendi.")
        except:
            sys.stderr.write("Loglar listelenirken bir hata oluştu. Lütfen tekrar deneyin. \n")
            logging.error("Loglar listelenirken bir hata oluştu.", exc_info=True)
            sys.exit(1)
