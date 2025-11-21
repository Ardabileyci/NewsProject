from django.contrib import admin
from .models import Kategori, Haber

admin.site.site_header = "Çağrı Haber Yönetim Paneli"
admin.site.site_title = "Çağrı Haber Admin"
admin.site.index_title = "Yönetim Paneli"

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim', 'aciklama']
    search_fields = ['isim']

@admin.register(Haber)
class HaberAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'kategori', 'editor', 'olusturma_tarihi', 'yayinda']
    list_filter = ['kategori', 'yayinda', 'olusturma_tarihi']
    search_fields = ['baslik', 'icerik']
    date_hierarchy = 'olusturma_tarihi'
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.editor = request.user
        super().save_model(request, obj, form, change)

