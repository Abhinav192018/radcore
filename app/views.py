from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def product_detail(request):
    return render(request, 'product_detail.html')

def orders(request):
    return render(request, 'orders.html')

def checkout(request):
    return render(request, 'checkout.html')

def profile(request):
    return render(request, 'profile.html')