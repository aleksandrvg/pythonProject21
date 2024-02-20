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
