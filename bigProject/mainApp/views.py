from django.shortcuts import render
from mainApp.services.productService import GetAllProducts, FindProductById
from mainApp.services.toppingService import GetAllTopping
# Create your views here.
def Main(request):
    products = GetAllProducts()
    return render(request, 'index.html', {'products': products})
def Product(request, product_id):
    product = FindProductById(product_id)
    toppings = GetAllTopping()
    return render(request, 'product.html', {"product": product, "toppings": toppings})
