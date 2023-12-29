from django import forms

from .models import kategori

class FromProduk(forms.Form):
    kategori = forms.ModelChoiceField(queryset=kategori.objects.all())
    nama = forms.CharField()
    harga = forms.CharField(max_length=20)
    gambar_produk = forms.ImageField()