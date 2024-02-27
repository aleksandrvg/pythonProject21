from django.shortcuts import render, redirect
from mainApp.services.productService import GetAllProducts, FindProductById
from mainApp.services.toppingService import GetAllTopping
from mainApp.services.cartService import GetCart as GC, AddProductInCart
from mainApp.EmailSander import EmailSender
# Create your views here.
def Main(request):
    products = GetAllProducts()
    return render(request, 'index.html', {'products': products})
def Product(request, product_id):
    product = FindProductById(product_id)
    toppings = GetAllTopping()
    return render(request, 'product.html', {"product": product, "toppings": toppings})
def AddInCart(request, product_id):
    AddProductInCart(product_id)
    return redirect('main')
def GetCart(request):
    cart = GC()
    context = {
        "products": cart.GetProducts(),
        "summ": cart.GetSum()
    }
    return render(request, 'cart.html', context)
def SendEmail(request):
    if request.method == "POST":
        email = request.POST.get("email")
        cart = GC()
        message = ""
        message += str(cart.GetProducts())+"\n"
        message += str(cart.GetSum)+"\n"
        emailSender = EmailSender(email)
        emailSender.SendEmail("Заказ ", message)
    return redirect('main')
