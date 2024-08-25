class Product:
    """
        Initialize a Product instance.
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
    """
    def __init__(self, name: str, price: float, quantity: int):
        # The name, price, and quantity parameters annotate with their types,
        # not assigned default type values.
        if not name:
            raise ValueError("Product name cannot be empty.")
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self._quantity = quantity  # Use a private variable to avoid conflict
        self.active = True

    def get_quantity(self) -> int:  # Getter method for quantity
        """
            Get the quantity of the product in stock
        """
        return self._quantity

    def set_quantity(self, quantity: int):  # Setter method for quantity
        """
            Set the quantity of the product in stock.
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity < 0:
            raise ValueError("Not possible, quantity cannot be negative.")
        self._quantity = quantity
        self.active = self._quantity > 0

    def is_active(self) -> bool:
        """
            Check if the product is active (in stock).
            Returns:
                bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
            Activate the product, making it available for sale.
        """
        self.active = True

    def deactivate(self):
        """
            Deactivate the product, making it unavailable for sale.
        """
        self.active = False

    def show(self) -> str:
        """
            Show the details of the product.
            Returns:
                str: A string representation of the product's details.
        """
        return f"{self.name}, price: {self.price}, quantity: {self._quantity}"

    def buy(self, quantity) -> float:
        """
            Buy a specified quantity of the product.
            Args:
                quantity (int): The number of units to buy.

            Returns:
                float: The total price of the purchase.
            Raises:
                Exception: If the product is not active
                or if there is not enough quantity in stock.
        """
        if not isinstance(quantity, int):
            raise TypeError("quantity must me an integer.")
        if not self.active:  # Ensures that the product is available for sale
            raise Exception("product is not active")
        if not self.active:
            raise Exception("Product is not active.")
        if quantity < 1:
            raise ValueError("quantity must be at least 1.")
        if quantity > self._quantity:
            # Ensures that there is enough stock to fulfill the purchase request.
            raise Exception("not enough quantity in stock.")

        self._quantity -= quantity  # Updates the stock
        total_price = self.price * quantity

        if self._quantity == 0:
            self.deactivate()
        # or this way:
        # Use the set_quantity method to update the stock and automatically deactivate the product if necessary
        #     self.set_quantity(self._quantity - quantity)
        return total_price
