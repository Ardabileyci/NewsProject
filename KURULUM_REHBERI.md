# 📚 Detaylı Kurulum Rehberi

Bu rehber, projeyi hiç Django bilmeyen biri için adım adım anlatmaktadır.

## 1. Python'u Kontrol Edin

Terminal veya Komut İstemi'ni açın ve şu komutu yazın:

```bash
python --version
```

veya

```bash
python3 --version
```

Python 3.8 veya üzeri bir sürüm görmelisiniz. Görmüyorsanız, [Python'u indirin](https://www.python.org/downloads/).

## 2. Proje Klasörüne Gidin

```bash
cd /Users/ardabileyci/Documents/projects/haber
```

## 3. Sanal Ortam Oluşturun

Sanal ortam, projenizin bağımlılıklarını izole eder.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Başarılı olursa, terminalinizde `(venv)` yazısını göreceksiniz.

## 4. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

Bu komut Django ve Pillow'u yükleyecek.

## 5. Veritabanını Hazırlayın

Django'nun veritabanı tablolarını oluşturması için:

```bash
python manage.py makemigrations
python manage.py migrate
```

Bu komutlar `db.sqlite3` adında bir dosya oluşturacak.

## 6. Admin Kullanıcısı Oluşturun

```bash
python manage.py createsuperuser
```

Size şunları soracak:
- **Username**: İstediğiniz kullanıcı adını girin (örn: admin)
- **Email**: E-posta adresiniz (boş bırakabilirsiniz)
- **Password**: Şifrenizi girin (yazarken ekranda görünmez, bu normaldir)
- **Password (again)**: Şifrenizi tekrar girin

## 7. Sunucuyu Başlatın

```bash
python manage.py runserver
```

Terminal'de şöyle bir mesaj göreceksiniz:
```
Starting development server at http://127.0.0.1:8000/
```

## 8. Siteyi Açın

Tarayıcınızda şu adresi açın:
```
http://127.0.0.1:8000
```

Henüz haber olmadığı için boş bir sayfa göreceksiniz.

## 9. Admin Paneline Girin

```
http://127.0.0.1:8000/admin
```

Oluşturduğunuz kullanıcı adı ve şifre ile giriş yapın.

## 10. İçerik Ekleyin

### Kategoriler Ekleyin:
1. Admin panelde "Kategoriler" yazan yere tıklayın
2. Sağ üstteki "Kategori Ekle" butonuna tıklayın
3. Kategori bilgilerini doldurun:
   - **İsim**: Spor
   - **Açıklama**: Spor haberleri
4. "Kaydet" butonuna tıklayın
5. Bu işlemi farklı kategoriler için tekrarlayın (Ekonomi, Teknoloji, Sağlık, vb.)

### Haber Ekleyin:
1. Admin panelde "Haberler" yazan yere tıklayın
2. Sağ üstteki "Haber Ekle" butonuna tıklayın
3. Haber bilgilerini doldurun:
   - **Başlık**: Haber başlığınız
   - **İçerik**: Haber metni
   - **Kategori**: Açılır listeden kategori seçin
   - **Resim**: İsterseniz bir resim yükleyin
   - **Yayında mı?**: İşaretli bırakın
4. "Kaydet" butonuna tıklayın

## 11. Siteyi Tekrar Kontrol Edin

Ana sayfayı yenileyin (`http://127.0.0.1:8000`), eklediğiniz haberler görünecek!

## Sık Karşılaşılan Sorunlar

### "No module named django" hatası
```bash
pip install django
```

### Port zaten kullanılıyor hatası
```bash
python manage.py runserver 8001
```
(Farklı bir port kullanın)

### Statik dosyalar yüklenmiyor
```bash
python manage.py collectstatic
```

### Veritabanını sıfırlamak isterseniz
```bash
# Önce sunucuyu durdurun (Ctrl+C)
# Veritabanını silin
rm db.sqlite3
# Tekrar oluşturun
python manage.py migrate
python manage.py createsuperuser
```

## Sunucuyu Durdurmak

Terminal'de `Ctrl+C` tuşlarına basın.

## Sanal Ortamdan Çıkmak

```bash
deactivate
```

## İlerisi İçin

- Yeni editörler eklemek için admin panelinde "Users" bölümünü kullanın
- Her kullanıcıya "Staff status" verin ki admin paneline girebilsin
- Haberleri düzenlemek veya silmek için admin panelini kullanın

Başarılar! 🎉

