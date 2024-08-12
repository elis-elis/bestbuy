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
        if products and not isinstance(products, list):
            raise TypeError("Products must be a list.")
        if products and any(not isinstance(product, Product) for product in products):
            raise TypeError("All items in products list must be of type Product.")
        # This part checks if the products variable is not empty or None.
        # an empty list or None evaluates to False, while a non-empty list evaluates to True.
        # The code checks whether the products list is provided and not empty.
        # If it is, the code then checks each item in the list to ensure that
        # every item is an instance of the Product class.

        if products:
            self.products = products
            # Use the provided list of products
        else:
            self.products = []
            # Create an empty list if no products are provided
        # or like this:   self.products = products if products else []

    def add_products(self, product: Product):
        """
            Add a product to the store.
        """
        # The isinstance() function checks whether the variable product is an instance of the Product class.
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of the Product class")

        self.products.append(product)

    def remove_product(self, product: Product):
        """
            Remove a product from the store.
        """
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of the Product class.")
            # Check if the product exists in the store's product list
        if product not in self.products:
            raise ValueError("Product not found in store inventory.")

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

    # or like this:         return sum(product.get_quantity() for product in self.products)

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
        if not isinstance(shopping_list, list):
            raise TypeError("Shopping list must be a list.")
        if any(not isinstance(item, tuple) for item in shopping_list):
            raise TypeError("Each item in shopping list must be a tuple of [Product, int]")

        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"This {product} is not found in store")
            total_price += product.buy(quantity)
        return total_price
