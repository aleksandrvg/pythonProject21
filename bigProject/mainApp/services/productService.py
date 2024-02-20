#productService
from ..models import Product
imgs = ["https://sgastronomy.ru/wp-content/uploads/2022/02/2-85.jpg",
        "https://meat-expert.ru/files/uploads/obzor/_2023/30/01.jpg",
        "https://roscontrol.com/wp-content/uploads/2021/09/3fff4d00a2f81362d59e-1-scaled.jpg",
        "https://www.ermolino-produkty.ru/picts/products/po-domashnemy_new.jpg"]
products = [Product(1, 150.0, "Медвежье ухо", "Пельмени вкусные", imgs[0]),
            Product(2, 250.0, "Вятское ухо", "Пельмени вкусные", imgs[1]),
            Product(3, 100.0, "Татарские", "Пельмени вкусные", imgs[2]),
            Product(4, 300.0, "Пермские", "Пельмени вкусные", imgs[3])]
def GetAllProducts() -> list:
    print("Подключились к базе данных достали все товары")
    return products
def FindProductById(id:int) -> Product:
    for product in products:
        if product.id == id:
            return product
