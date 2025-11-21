from django.shortcuts import render, get_object_or_404
from .models import Haber, Kategori

def ana_sayfa(request):
    haberler = Haber.objects.filter(yayinda=True)
    kategoriler = Kategori.objects.all()
    
    context = {
        'haberler': haberler,
        'kategoriler': kategoriler,
        'sayfa_basligi': 'Ana Sayfa - Tüm Haberler'
    }
    return render(request, 'haberler/ana_sayfa.html', context)

def haber_detay(request, haber_id):
    haber = get_object_or_404(Haber, id=haber_id, yayinda=True)
    kategoriler = Kategori.objects.all()
    
    context = {
        'haber': haber,
        'kategoriler': kategoriler,
    }
    return render(request, 'haberler/haber_detay.html', context)

def kategori_haberleri(request, kategori_id):
    kategori = get_object_or_404(Kategori, id=kategori_id)
    haberler = Haber.objects.filter(kategori=kategori, yayinda=True)
    kategoriler = Kategori.objects.all()
    
    context = {
        'haberler': haberler,
        'kategoriler': kategoriler,
        'secili_kategori': kategori,
        'sayfa_basligi': f'{kategori.isim} - Haberler'
    }
    return render(request, 'haberler/kategori_haberleri.html', context)

