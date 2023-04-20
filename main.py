"""Create a dataclass named "Product" that has the following attributes: product_id: int name: str price: float quantity: int 
The class should also have a method named "total_cost" that calculates and returns the total cost of the product, which is the price multiplied by the quantity. 
Create a list of Product objects and write a function that takes this list as input and returns the product with the highest total cost. 
Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost."""


from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def get_total_cost(self) -> float:
        return self.price * self.quantity


def get_highest_total_cost(list_of_products: List) -> "Product":
    highest_cost_product = None
    hihgest_cost = 0
    for item in list_of_products:
        cost = item.get_total_cost()
        if cost > hihgest_cost:
            hihgest_cost = cost
            highest_cost_product = item
    return highest_cost_product


products = [
    Product(product_id=1, name="Pienas", price=1.83, quantity=5),
    Product(product_id=2, name="Dripsniai", price=0.83, quantity=5),
    Product(product_id=3, name="Geresnis viskis", price=70.30, quantity=2),
    Product(product_id=4, name="Gavome ismoka", price=258, quantity=1),
    Product(product_id=5, name="Kur mano taksi?", price=7, quantity=1),
]

for item in products:
    print(
        f"Product ID - {item.product_id}, product name - {item.name}, it's price - {item.price}, there are {item.quantity} items left"
    )

highest_value_product = get_highest_total_cost(products)
print(highest_value_product)
