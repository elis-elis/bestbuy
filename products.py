from typing import Optional
from promotion import Promotion


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
        self.promotion: Optional[Promotion] = None

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
        if self.promotion:
            promotion_info = f" (Promotion: {self.promotion.name})"
        else:
            promotion_info = ""
        return f"{self.name}, price: {self.price}, quantity: {self._quantity}{promotion_info}"

    def set_promotion(self, promotion: Promotion):
        # promotion: Promotion: expects an object of the Promotion class (or any subclass of Promotion).
        # It represents the promotion that we want to apply to the product.
        self.promotion = promotion
        # this method "attaches" a specific promotion to the product.

    def remove_promotion(self):
        self.promotion = None

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
            raise Exception("product is not active.")
        if quantity < 1:
            raise ValueError("quantity must be at least 1.")
        if quantity > self._quantity:
            # Ensures that there is enough stock to fulfill the purchase request.
            raise Exception("not enough quantity in stock.")

        if self.promotion:
            # Calculate the price using the promotion
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            # Regular price calculation
            total_price = self.price * quantity

        self._quantity -= quantity  # Updates the stock
        if self._quantity == 0:
            self.deactivate()
        # or this way:
        # Use the set_quantity method to update the stock and automatically deactivate the product if necessary
        #     self.set_quantity(self._quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        """
            Initialize a NonStockedProduct with name and price.
            The quantity is always set to 0.
        """
        super().__init__(name, price, 0)  # Quantity is always 0 for non-stocked products.

    def set_quantity(self, quantity: int):
        """
            Override set_quantity to prevent changing the quantity.
        """
        raise Exception("Cannot set quantity for NonStockedProduct.")

    def buy(self, quantity: int) -> float:
        """
            Override buy method to allow purchasing any quantity,
            since we don't track stock.
        """
        if not isinstance(quantity, int):
            raise TypeError("quantity must me an integer.")
        if quantity < 1:
            raise ValueError("quantity must be at least 1.")
        return self.price * quantity

    def show(self) -> str:
        """
            Show the details of the NonStockedProduct.
        """
        return f"{self.name}, price: {self.price} (Non-stocked, unlimited availability)"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
            Initialize a LimitedProduct with name, price, and max_quantity.
            Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
            maximum (int): The maximum quantity that can be purchased in a single order.
        """
        super().__init__(name, price, quantity)
        if not isinstance(maximum, int):
            raise TypeError("Maximum quantity must be integer")
        if maximum < 1:
            raise ValueError("Maximum quantity must be at least 1.")

        self.max_quantity = maximum     # Set the maximum purchase limit

    def buy(self, quantity) -> float:
        # The method is expected to return a float, which will be the total price of the purchase.
        """
            Override buy method to limit the purchase quantity.
        """
        if not isinstance(quantity, int):
            raise TypeError("quantity must me an integer.")
        if quantity < 1:
            raise ValueError("quantity must be at least 1.")
        if quantity > self.max_quantity:
            # This checks if the quantity requested is greater than the allowed max_quantity for this product.
            raise ValueError(f" cannot buy more than {self.max_quantity} units of this product.")

        return super().buy(quantity)
        # super().buy(quantity) is called, which runs the buy method in Product.
        # The Product class's buy method subtracts the quantity from the stock,
        # calculates the total price, and returns it. This result (the total price) is then
        # returned by the buy method of LimitedProduct as well.

    def show(self) -> str:
        """
        Show the details of the LimitedProduct.
        """
        return f"{self.name}, price: {self.price}, quantity: {self._quantity} max per order: {self.max_quantity}"
