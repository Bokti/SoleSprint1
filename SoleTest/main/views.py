from django.shortcuts import render

def store(request):
    contex={ }
    return render(request,'main/store.html')

def cart(request):
    contex={ }
    return render(request,'main/cart.html')

def checkout(request):
    contex={ }
    return render(request,'main/checkout.html')

