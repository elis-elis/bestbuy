from typing import Type


class Product:
    def __init__(self, name=str, price=float, quantity=int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product attributes.")
        self.name = name
        self.price = price
        self._quantity = quantity   # Use a private variable to avoid conflict
        self.active = True

    def get_quantity(self) -> int:  # Getter method for quantity
        return self._quantity

    def set_quantity(self, quantity: int):  # Setter method for quantity
        if quantity < 0:
            raise ValueError("Not possible, quantity cannot be negative.")
        self._quantity = quantity
        if self._quantity == 0:
            self.active = False
        else:
            self.active = True  # Ensure product is active if quantity is non-zero

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, price: {self.price}, quantity: {self._quantity}"

    def buy(self, quantity: int) -> float:
        # parameter representing how many units of the product the user wants to buy
        # return type: the total price of the purchase
        if not self.active:     # Ensures that the product is available for sale
            raise Exception("product is not active")
        if quantity > self._quantity:    # Ensures that there is enough stock to fulfill the purchase request.
            raise Exception("not enough quantity in stock.")

        self._quantity -= quantity   # Updates the stock

        if self._quantity == 0:
            self.active = False     # Automatically deactivates the product if all units have been sold

        return self.price * quantity
