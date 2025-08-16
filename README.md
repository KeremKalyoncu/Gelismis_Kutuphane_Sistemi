# 📚 Kütüphane Yönetim Sistemi

**Kütüphane Yönetim Sistemi**, kitapların düzenli bir şekilde yönetilmesini sağlayan güçlü ve kullanıcı dostu bir Python tabanlı komut satırı uygulamasıdır. 📖 Kitap eklemekten ödünç işlemlerine, detaylı loglamadan geliştirici moduna kadar her şeyi bu sistemde bulabilirsiniz! Modern kütüphaneler için tasarlanmış bu uygulama, hem pratik hem de platform bağımsız bir çözüm sunar. 🚀

Bu proje, kitap tutkunlarının ve kütüphane yöneticilerinin hayatını kolaylaştırmak için geliştirildi. SQLite veritabanı ile desteklenen sistem, tüm işlemlerinizi güvenli bir şekilde kaydeder ve geliştirici dostu özellikleriyle özelleştirmeye açıktır.

## ✨ Temel Özellikler

- **📖 Kitap Yönetimi**: Kitapları kolayca ekleyin, silin veya güncelleyin.
- **🔍 Kitap Arama**: Kitapları ad, yazar, yıl, dağıtım şirketi veya baskı sayısına göre hızlıca bulun.
- **📤 Ödünç İşlemleri**: Kitapları ödünç verin veya iade alın, her adımı takip edin.
- **📜 Loglama Sistemi**: Tüm işlemler SQLite veritabanında ve bir log dosyasında kaydedilir.
- **🛠️ Geliştirici Modu**: Özel kod (`5348`) ile logları görüntüleyin ve veritabanı bağlantısını yönetin.
- **🌐 Platform Bağımsızlığı**: Windows, Linux ve macOS'ta sorunsuz çalışır.

## 🛠️ Kullanılan Teknolojiler

- **Python 3.x**: Güçlü ve esnek programlama dili.
- **SQLite3**: Hafif ve güvenilir veritabanı yönetimi.
- **Python Kütüphaneleri**: 
  - `sqlite3`: Veritabanı işlemleri için.
  - `pathlib`: Platform bağımsız dosya yolu yönetimi.
  - `logging`: Detaylı işlem kayıtları.
  - `os`, `platform`, `time`: Sistem uyumluluğu ve zaman yönetimi.

## 🚀 Kurulum

Kütüphane Yönetim Sistemi'ni birkaç basit adımda çalıştırabilirsiniz:

1. **Depoyu Klonlayın**:
   ```bash
   git clone https://github.com/[kullanici-adi]/kutuphane-yonetim-sistemi.git
   ```
2. **Proje Dizinine Gidin**:
   ```bash
   cd kutuphane-yonetim-sistemi
   ```
3. **Bağımlılık Kontrolü**: Proje yalnızca Python'un yerleşik kütüphanelerini kullanır. Python 3.x'in yüklü olduğundan emin olun.
4. **Uygulamayı Başlatın**:
   ```bash
   python Kütüphane_sistemi.py
   ```

## 📖 Kullanım

Uygulama, sezgisel bir komut satırı arayüzü ile sizi karşılar. İşte yapabilecekleriniz:

1. **Kitap Ekle**: Yeni kitapları kütüphanenize ekleyin.
2. **Kitap Sil**: İstenmeyen kitapları veritabanından kaldırın.
3. **Kitapları Listele**: Kütüphanenizdeki tüm kitapları görün.
4. **Kitap Arama**: Kitapları farklı kriterlerle sorgulayın.
5. **Ödünç Verme**: Kitapları bir kişiye ödünç verin.
6. **İade Alma**: Ödünç verilen kitapları geri alın.
7. **Çıkış**: Sistemi güvenli bir şekilde kapatın.
8. **Geliştirici Modu**: `5348` kodunu girerek gelişmiş özelliklere erişin.

### Örnek Kullanım
```bash
Kütüphane Sistemine Hoşgeldiniz.

 1. Kitap Ekle
 2. Kitap Sil
 3. Kitapları Listele
 4. Kitap Arama
 5. Kitap Ödünç Verme
 6. Kitap İade Alma
 7. Çıkış

Lütfen yapmak istediğiniz işlemi seçiniz: 1
Kitap Adı: Sefiller
Yazar: Victor Hugo
Yılı: 1862
Dağıtım Şirketi: Can Yayınları
Baskı Sayısı: 3
Kitap ekleniyor...
Kitap başarıyla eklendi.
```

## 💾 Veritabanı ve Loglama

- **Veritabanı**: Kitap bilgileri `Veritabanı-Log-AdminLog/veritabani.db` dosyasında saklanır.
- **Loglar**: İşlem kayıtları hem `Veritabanı-Log-AdminLog/log.db` SQLite dosyasında hem de `Veritabanı-Log-AdminLog/kutuphane_sistemi.log` metin dosyasında tutulur.
- Loglar, işlem türü, tarih ve kitap detaylarını içerir, böylece her adımı takip edebilirsiniz.

## 🔐 Geliştirici Modu

Ana menüde `5348` kodunu girerek geliştirici moduna erişebilirsiniz. Bu modda:
- Veritabanı bağlantısını açıp kapatabilirsiniz.
- Son `n` adet log kaydını görüntüleyebilirsiniz.

## 🤝 Katkıda Bulunma

Bu projeyi daha da geliştirmek ister misiniz? Katkılarınızı bekliyoruz! İşte adımlar:
1. Depoyu fork edin.
2. Yeni bir dal oluşturun: `git checkout -b yeni-ozellik`
3. Değişikliklerinizi yapın ve commit edin: `git commit -m "Yeni özellik eklendi"`
4. Dalınızı ana depoya itin: `git push origin yeni-ozellik`
5. Bir Pull Request oluşturun.

## 📬 İletişim

Proje hakkında sorularınız, önerileriniz veya geri bildirimleriniz varsa, bana ulaşabilirsiniz:
- **Ad**: Kerem Kalyoncu
- **E-posta**: [gskerem200553@outlook.com](mailto:gskerem200553@outlook.com)
- **LinkedIn**: [Kerem Kalyoncu](https://www.linkedin.com/in/kerem-kalyoncu-0753k)


## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atın.

## 📝 Ek Notlar

- **Platform Uyumluluğu**: `pathlib` ile dosya yolları platform bağımsız şekilde yönetilir.
- **Hata Yönetimi**: Güvenilirlik için kapsamlı hata işleme ve loglama uygulanmıştır.
- **Gelecek Planları**: Daha fazla özellik (örneğin, GUI arayüzü veya kullanıcı yönetimi) eklemek için katkılarınızı bekliyoruz!