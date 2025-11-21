# 📰 Çağrı Haber - Django Haber Sitesi

Django ve Bootstrap kullanarak yapılmış modern bir haber sitesi projesi.

## 🎯 Özellikler

- ✅ Kırmızı modern tema ile profesyonel görünüm
- ✅ Manşet haber özelliği (en yeni haber öne çıkar)
- ✅ Ana sayfada tüm haberler
- ✅ Kategorilere göre haber filtreleme
- ✅ Haber detay sayfası
- ✅ Farklı editörler (kullanıcılar) haber ekleyebilir
- ✅ Admin paneli ile kolay yönetim
- ✅ Responsive (mobil uyumlu) tasarım
- ✅ Haber resimleri yükleme
- ✅ Örnek verilerle hazır

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

## 🚀 Kurulum

### 1. Projeyi İndirin

```bash
cd haber
```

### 2. Sanal Ortam Oluşturun (Önerilen)

```bash
python -m venv venv
```

Sanal ortamı aktif edin:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### 3. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Veritabanını Oluşturun

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Admin Kullanıcısı (Otomatik Oluşturulur)

Migration sırasında admin kullanıcısı otomatik olarak oluşturulur:

**Admin Giriş Bilgileri:**
- **Kullanıcı Adı**: `admin`
- **Şifre**: `admin123`
- **E-posta**: admin@haberler.com

> ⚠️ **Not**: Bu bilgiler kod içinde tanımlıdır (ödev projesi için). Gerçek projelerde bu yöntem kullanılmamalıdır!

İsterseniz yeni kullanıcı da oluşturabilirsiniz:
```bash
python manage.py createsuperuser
```

### 6. Sunucuyu Başlatın

```bash
python manage.py runserver
```

Tarayıcınızda `http://127.0.0.1:8000` adresine gidin.

**Örnek veriler zaten mevcut!** Site hazır olarak açılacak.

## 🔧 Kullanım

### Admin Paneline Giriş

1. `http://127.0.0.1:8000/admin` adresine gidin
2. Oluşturduğunuz kullanıcı adı ve şifre ile giriş yapın

### Kategori Ekleme

1. Admin panelinde "Kategoriler" bölümüne gidin
2. "Kategori Ekle" butonuna tıklayın
3. Kategori adı ve açıklama girin
4. Kaydet

Örnek kategoriler:
- Spor
- Ekonomi
- Teknoloji
- Sağlık
- Dünya

### Haber Ekleme

1. Admin panelinde "Haberler" bölümüne gidin
2. "Haber Ekle" butonuna tıklayın
3. Haber başlığı, içerik, kategori seçin
4. İsterseniz resim yükleyin
5. Kaydet

### Yeni Editör (Kullanıcı) Ekleme

1. Admin panelinde "Kullanıcılar" bölümüne gidin
2. "Kullanıcı Ekle" butonuna tıklayın
3. Kullanıcı bilgilerini girin
4. "Staff status" seçeneğini işaretleyin (admin paneline giriş yapabilmesi için)
5. Kaydet

## 📁 Proje Yapısı

```
haber/
├── manage.py                 # Django yönetim dosyası
├── requirements.txt          # Python paketleri
├── db.sqlite3               # Veritabanı (oluşturulduktan sonra)
├── haber_sitesi/            # Ana proje klasörü
│   ├── settings.py          # Ayarlar
│   ├── urls.py              # Ana URL yönlendirmeleri
│   └── ...
├── haberler/                # Haberler uygulaması
│   ├── models.py            # Veritabanı modelleri
│   ├── views.py             # Görünüm fonksiyonları
│   ├── urls.py              # URL yönlendirmeleri
│   ├── admin.py             # Admin panel ayarları
│   └── templates/           # HTML şablonları
└── media/                   # Yüklenen resimler (otomatik oluşur)
```

## 📱 Sayfalar

- **Ana Sayfa** (`/`): Tüm haberler
- **Kategori Sayfası** (`/kategori/<id>/`): Belirli kategorideki haberler
- **Haber Detay** (`/haber/<id>/`): Haberin tam içeriği
- **Admin Panel** (`/admin/`): Yönetim paneli

## 🎨 Kullanılan Teknolojiler

- **Django 4.2.7**: Python web framework
- **Bootstrap 5.3**: CSS framework (CDN üzerinden)
- **SQLite**: Veritabanı
- **Pillow**: Resim işleme

## 💡 İpuçları

1. Projeyi ilk çalıştırdığınızda mutlaka admin kullanıcısı oluşturun
2. Önce kategoriler ekleyin, sonra haberleri ekleyin
3. Her haberin bir kategorisi ve editörü olmalı
4. Resimler `media/haber_resimleri/` klasörüne yüklenir
5. "Yayında mı?" seçeneğini kullanarak haberleri gizleyebilirsiniz

## 📝 Notlar

- Bu proje eğitim amaçlıdır
- Gerçek bir projede `SECRET_KEY` değiştirilmeli
- Gerçek bir projede `DEBUG = False` yapılmalı
- Üretim ortamında başka bir veritabanı (PostgreSQL, MySQL) kullanılmalı

## 🤝 Destek

Sorun yaşarsanız:
1. `python manage.py runserver` komutunu tekrar çalıştırın
2. Tarayıcınızın önbelleğini temizleyin
3. Sanal ortamın aktif olduğundan emin olun

İyi çalışmalar! 🎉

