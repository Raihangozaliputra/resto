from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import kategori, produk
from .form import FromProduk
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def products(request):
    data = produk.objects.all()
    submitted = False
    if request.method == "POST":
        form = FromProduk(request.POST, request.FILES)
        if form.is_valid():
            simpanData = produk.objects.create(
                namaProduk=form.cleaned_data.get("nama"),
                harga=form.cleaned_data.get("harga"),
                gambar_produk=form.cleaned_data.get("gambar_produk"),
                kategori=form.cleaned_data.get("kategori"),
            )
            simpanData.save()
            return HttpResponseRedirect("/product?submitted=True")
        else:
            form = FromProduk
            if "submitted" in request.get:
                submitted = True

    contenxt = {
        "judul": "selamat datang di website",
        "subjudul": "my website no 2",
        "kategori": data,
        "form": FromProduk,
    }
    template = loader.get_template("products.html")
    return HttpResponse(template.render(contenxt, request))

def hapus_produk(request, produk_id):
    hapus_produk = produk.objects.get(id=produk_id)
    hapus_produk.delete()
    return redirect("products")

def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())

def details(request, id):
  data = produk.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': data,
  }
  return HttpResponse(template.render(context, request))
