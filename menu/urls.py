from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/", views.products, name="products"),
    path("product/details/<int:id>", views.details, name="details"),
    path("hapus_produk/<produk_id>", views.hapus_produk, name="hapus_produk"),
    path("about/", views.about, name="about"),
]