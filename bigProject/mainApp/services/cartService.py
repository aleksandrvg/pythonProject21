from ..models import Cart
import mainApp.services.productService as PS
cart = Cart()

def GetCart():
    return cart
def AddProductInCart(id):
    product = PS.FindProductById(id)
    cart.AddProduct(product)
