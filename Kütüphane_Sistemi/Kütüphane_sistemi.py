import Backend
import os
import platform
import time
def ekran_temizle():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
isle = Backend.Kutuphane()
isle.baglan()
ekran_temizle()
print("Kütüphane Sistemine Hoşgeldiniz.\n")
while True:
    print("\n 1. Kitap Ekle \n 2. Kitap Sil \n 3. Kitapları Listele \n 4. Kitap Arama \n 5. Kitap Ödünç Verme \n 6. Kitap İade Alma \n 7. Çıkış \n\n")
    secim = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
    if secim == "1":
        ekran_temizle()
        kitap_ad = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yili = input("Yılı: ")
        dagitim = input("Dağıtım Şirketi: ")
        baski = input("Baskı Sayısı: ")
        tarih = time.strftime("%Y-%m-%d %H:%M:%S")
        burdami = 1
        kimde = None
        isle.kitap_ekle([kitap_ad, yazar, yili, dagitim, baski, tarih, burdami, kimde])
        input("Listeleme işlemi tamamlandı. Devam etmek için bir tuşa basınız...")
        ekran_temizle()
    elif secim == "2":
        ekran_temizle()
        kitap_ad = input("hangi kitabı silmek istersiniz: ")
        isle.kitap_silme(kitap_ad, "ad")
        input("Listeleme işlemi tamamlandı. Devam etmek için bir tuşa basınız...")
        ekran_temizle()
    elif secim == "3":
        ekran_temizle()
        isle.tum_kitaplari_listele()
        input("Listeleme işlemi tamamlandı. Devam etmek için bir tuşa basınız...")
        ekran_temizle()
    elif secim == "4":
        ekran_temizle()
        deger = input("Aramak istediğiniz değeri giriniz: ")
        neye = input("Aramak istediğiniz alanı giriniz (ad, yazar, yili, dagitim, baski): ")
        ekran_temizle()
        isle.kitap_sorgula(deger, neye)
        input("Listeleme işlemi tamamlandı. Devam etmek için bir tuşa basınız...")
        ekran_temizle()
    elif secim == "5":
        ekran_temizle()
        kitap_ad = input("Ödünç vermek istediğiniz kitabın adını giriniz: ")
        kim = input("Kitabı ödünç vereceğiniz kişinin adını giriniz: ")
        isle.oduncver(kitap_ad, kim)
        input("Listeleme işlemi tamamlandı. Devam etmek için bir tuşa basınız...")
        ekran_temizle()
    elif secim == "6":
        ekran_temizle()
        kitap_ad = input("İade almak istediğiniz kitabın adını giriniz: ")
        isle.oduncal(kitap_ad)
        input("Listeleme işlemi tamamlandı. Devam etmek için bir tuşa basınız...")
        ekran_temizle()
    elif secim == "7":
        ekran_temizle()
        isle.baglantikes()
        print("Kütüphane sisteminden çıkılıyor...")
        time.sleep(1)
        break
    elif secim == "5348":
        ekran_temizle()
        print("Geliştirici Modu Aktif Edildi.")
        print("1. Veritabanı Bağlantısını Aç")
        print("2. Veritabanı Bağlantısını Kapat")
        print("3. Logları Listele")
        secim_gel = input("Lütfen bir seçim yapınız: ")
        if secim_gel == "1":
            ekran_temizle()
            isle.baglan()
            print("Veritabanı bağlantısı açıldı.")
            time.sleep(1)
        elif secim_gel == "2":
            ekran_temizle()
            isle.baglantikes()
            print("Veritabanı bağlantısı kapatıldı.")
            time.sleep(1)
        elif secim_gel == "3":
            ekran_temizle()
            nekadar = int(input("Kaç adet log görmek istersiniz: "))
            if nekadar < 0:
                print("Negatif bir sayı girdiniz. Lütfen pozitif bir sayı giriniz.")
            isle.log_listele(nekadar)
            input("Listeleme işlemi tamamlandı. Devam etmek için bir tuşa basınız...")
            ekran_temizle()
            time.sleep(1)
    else:
        ekran_temizle()
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        time.sleep(1)
        ekran_temizle()


