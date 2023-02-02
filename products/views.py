from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def homepage(request):
    context = {
        "versity": "Dhaka University",
        "course": "Chemistry"
    }
    return render(request, 'products/index.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {
        "product_list": products
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "product": product
    }
    return render(request, 'products/product_detail.html', context)

def product_create(request):
    form = ProductForm()

    # logic for saving the data into the database
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/products")

    context = {
        "form": form
    }
    return render(request, 'products/product_form.html', context)


def product_update(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(request.POST or None, instance=product)
    
    # logic for saving the data into the database
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/products")

    context = {
        "form": form
    }
    return render(request, 'products/product_form.html', context)

def delete_product(request, pk):
    if request.method == "POST":
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect("/products")

    return render(request, 'products/confirm_delete.html')