from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
            Apply promotion to the product and return the discounted price.
        """
        pass


class PercentDiscount(Promotion):
    """
        This will apply a percentage discount to the total price.
    """
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        # product: instance of the Product class. represents the product to which promotion is being applied.
        # quantity: integer representing the number of units of the product being purchased.
        discount = (self.percent / 100) * product.price * quantity
        # (self.percent / 100): Converts the percentage discount into a decimal.
        # product.price: The price of a single unit of the product.
        # product.price * quantity: Calculates total price for the given quantity of the product
        # before any discounts are applied.
        return (product.price * quantity) - discount
        # The result is the final price after applying the discount.


class SecondHalfPrice(Promotion):
    """
        This will give the second item in a pair at half price.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        if quantity == 1:   # checks if the customer is purchasing only one unit of the product.
            return product.price    # If only one unit is purchased, no promotion can be applied
        else:
            # quantity // 2 uses integer division to determine how many pairs of items are in total quantity.
            # For every two items, one will be at full price, and the second will be at half price.
            half_price_items = quantity // 2
            full_price_items = quantity - half_price_items
            return (product.price * full_price_items) + (half_price_items * product.price / 2)


class ThirdOneFree(Promotion):
    """
        This will give one item free for every two items purchased.
    """
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        free_items = quantity // 3
        payable_items = quantity - free_items
        return payable_items * product.price
