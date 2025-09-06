# 📌 PortfolioBot

> 🚀 Discord üzerinde projelerinizi **yönetmenizi, organize etmenizi ve portföyünüzü takip etmenizi sağlayan akıllı bot.**

PortfolioBot sayesinde:
- Projelerinizi ekleyebilir ve güncelleyebilirsiniz.  
- Projelerinize **beceriler (skills)** tanımlayabilirsiniz.  
- Projelerinizin **durumunu takip edebilirsiniz** (*Prototip, Geliştirme, Tamamlandı, Güncellendi, Bırakılmış*).  
- Tüm bu veriler **SQLite veritabanında kalıcı olarak saklanır.**

---

## ✨ Özellikler

✅ Yeni proje ekleme, düzenleme ve silme  
✅ Kendi projelerinizi listeleme  
✅ Projelere beceri ekleme (örn. *Python, SQL, Discord*)  
✅ Projelerin durumlarını kolayca değiştirme  
✅ Kalıcı veritabanı desteği (*SQLite*)  
✅ `modal.py` ile buton & modal örnekleri  

---

## 🤖 Bot ile Neler Yapabilirsiniz?

PortfolioBot, Discord sunucusunda size yardımcı olmak için çeşitli komutlara sahiptir:

- `!start` → Botu başlatır ve bilgi mesajı gösterir  
- `!info` → Kullanılabilir tüm komutları listeler  
- `!new_project` → Yeni proje ekler (ad, bağlantı, durum)  
- `!projects` → Tüm projelerinizi listeler  
- `!update_projects` → Seçtiğiniz projeyi günceller  
- `!skills` → Bir projeye beceri ekler (*örn: Python, SQL, API*)  
- `!delete` → Bir projeyi kalıcı olarak siler  

**Örnek akış:**
!new_project
👉 Projenin adını girin
👉 Proje bağlantısını girin
👉 Durum seçin (örn: Geliştirme Aşamasında)
✅ Proje başarıyla kaydedildi!


---

## 📂 Proje Yapısı



portfoliobot/
├── bot.py # Discord botunun ana dosyası (komutlar burada)
├── logic.py # SQLite veritabanı yöneticisi (CRUD işlemleri)
├── modal.py # Modal ve buton örnekleri
├── config.py # TOKEN ve veritabanı yapılandırması
└── portfolio.db # (Otomatik oluşturulur) SQLite veritabanı
