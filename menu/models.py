from django.db import models

# Create your models here.
class kategori(models.Model):
    nama = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nama}"

class produk(models.Model):
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    namaProduk = models.CharField(max_length=100)
    harga = models.CharField(max_length=30)
    gambar_produk = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.namaProduk} {self.harga}"