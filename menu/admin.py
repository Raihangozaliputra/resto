from django.contrib import admin
from .models import produk, kategori

# Register your models here.
class produkcafe(admin.ModelAdmin):
    list_display = ("namaProduk", "harga",)

admin.site.register(produk, produkcafe)
admin.site.register(kategori)