from typing import List, Tuple
from products import Product


class Store:
    """
        Initialize a Store instance.
        Args:
            products (List[Product], optional): A list of Product objects.
            Defaults to an empty list if not provided.
    """
    def __init__(self, products: List[Product] = None):
        if products:
            self.products = products
            # Use the provided list of products
        else:
            self.products = []
            # Create an empty list if no products are provided

    def add_products(self, product: Product):
        """
            Add a product to the store.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
            Remove a product from the store.
        """
        for store_product in self.products:
            if store_product == product:  # Check if the current product is the one to be removed.
                self.products.remove(store_product)
                break
                # Exit the loop after removing product to avoid modifying the list while iterating

    def get_total_quantity(self) -> int:
        """
            Get the total quantity of all products in the store.
            Returns:
                int: The total quantity of all products.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()  #
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
            Get a list of all active products in the store.
            Returns:
                List[Product]: A list of active Product objects.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products
    # or like this: return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Place an order for multiple products and calculate the total cost.
        Args:
            shopping_list (List[Tuple[Product, int]]):
            A list of tuples, where each tuple contains a Product object and the quantity to buy.
        Returns:
            float: Total cost of purchasing all the specified products in the quantities provided.
        Raises:
            Exception: If a product in the shopping list is not found in the store.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"This {product} is not found in store")
            total_price += product.buy(quantity)
        return total_price
