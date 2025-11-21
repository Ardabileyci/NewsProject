from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Kategori(models.Model):
    isim = models.CharField(max_length=100, verbose_name='Kategori Adı')
    aciklama = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    
    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
        ordering = ['isim']
    
    def __str__(self):
        return self.isim

class Haber(models.Model):
    baslik = models.CharField(max_length=200, verbose_name='Haber Başlığı')
    icerik = models.TextField(verbose_name='Haber İçeriği')
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='haberler', verbose_name='Kategori')
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='haberler', verbose_name='Editör')
    resim = models.ImageField(upload_to='haber_resimleri/', blank=True, null=True, verbose_name='Haber Resmi')
    olusturma_tarihi = models.DateTimeField(default=timezone.now, verbose_name='Oluşturma Tarihi')
    guncelleme_tarihi = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')
    yayinda = models.BooleanField(default=True, verbose_name='Yayında mı?')
    
    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'
        ordering = ['-olusturma_tarihi']
    
    def __str__(self):
        return self.baslik
    
    def kisa_ozet(self):
        if len(self.icerik) > 100:
            return self.icerik[:100] + '...'
        return self.icerik

