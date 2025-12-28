from django.shortcuts import render, redirect

def cart_detail(request):
    """Display shopping cart"""
    return render(request, 'cart/cart_detail.html')

def cart_add(request, product_id):
    """Add product to cart"""
    return redirect('cart_detail')

def cart_remove(request, product_id):
    """Remove product from cart"""
    return redirect('cart_detail')