from django.db import models
class Product():
    def __init__(self, id, price, name, description, image):
        self.id = id
        self.price = price
        self.name = name
        self.description = description
        self.image = image
class Topping():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
# Create your models here.
class Cart():
    _products = []
    _summ = 0
    def AddProduct(self, product):
        self._products.append(product)
        self._summ = 0
        for item in self._products:
            self._summ += item.price
    def GetProducts(self):
        return self._products
    def GetSum(self):
        return self._summ
