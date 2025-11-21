from django.urls import path
from . import views

app_name = 'haberler'

urlpatterns = [
    path('', views.ana_sayfa, name='ana_sayfa'),
    path('haber/<int:haber_id>/', views.haber_detay, name='haber_detay'),
    path('kategori/<int:kategori_id>/', views.kategori_haberleri, name='kategori_haberleri'),
]

