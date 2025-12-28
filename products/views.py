from django.shortcuts import render, get_object_or_404
from .models import Product

def homepage(request):
    # \"\"\"Homepage displaying featured products\"\"\"
    featured_products = Product.objects.filter(available=True)[:6]  # Show first 6 products
    return render(request, 'products/homepage.html', {'featured_products': featured_products})

def product_list(request):
    # \"\"\"All products page\"\"\"
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    # \"\"\"Single product details\"\"\"
    product = get_object_or_404(Product, pk=pk, available=True)
    return render(request, 'products/product_detail.html', {'product': product})