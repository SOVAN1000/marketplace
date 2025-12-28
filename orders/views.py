from django.shortcuts import render

def order_create(request):
    """Create new order"""
    return render(request, 'orders/order_create.html')