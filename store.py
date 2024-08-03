"""
Store Class:
Contains a list of Product instances.
Methods to add, remove, find, and show products.
Demonstrates class composition by including Product instances within the Store class.
"""

from products import Product
from typing import List, Tuple


class Store:
    def __init__(self, products: List[Product] = None):
        if products:
            self.products = products  # Use the provided list of products
        else:
            self.products = []  # Create an empty list if no products are provided

    def add_products(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        for p in self.products:
            if p == product:  # Check if the current product (p) is the one to be removed.
                self.products.remove(p)
                break  # Exit the loop after removing the product to avoid modifying the list while iterating

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()  #
        return total_quantity

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products
    # or like this: return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        # allows you to purchase multiple products at once and calculates the total cost of the order.
        # takes a list of tuples 'shopping_list'. Each tuple contains a Product object and the quantity you want to buy.
        # returns the total cost (as a float) of purchasing all the specified products in the quantities provided.
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"This {product} is not found in store")
            total_price += product.buy(quantity)
        return total_price
