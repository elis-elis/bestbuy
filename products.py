"""
Product Class:
Represents a product with attributes: name, price, quantity, and active.
Contains methods for getting and setting quantity, checking if the product is active, showing product details,
and buying the product.
"""


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        # The name, price, and quantity parameters annotate with their types, not assigned default type values.
        self.name = name
        self.price = price
        self._quantity = quantity  # Use a private variable to avoid conflict
        self.active = True

    def get_quantity(self) -> int:  # Getter method for quantity
        return self._quantity

    def set_quantity(self, quantity: int):  # Setter method for quantity
        if quantity < 0:
            raise ValueError("Not possible, quantity cannot be negative.")
        self._quantity = quantity
        self.active = self._quantity > 0

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, price: {self.price}, quantity: {self._quantity}"

    def buy(self, quantity) -> float:
        # parameter representing how many units of the product the user wants to buy
        # return type: the total price of the purchase
        if not self.active:  # Ensures that the product is available for sale
            raise Exception("product is not active")
        if quantity > self._quantity:  # Ensures that there is enough stock to fulfill the purchase request.
            raise Exception("not enough quantity in stock.")

        self._quantity -= quantity  # Updates the stock
        total_price = self.price * quantity

        if self._quantity == 0:
            self.deactivate()

        return total_price
