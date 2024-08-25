import pytest
from products import Product


def test_create_valid_product():
    """
    The test checks that all attributes of the 'Product' are set as expected
    when an object is created.
    """
    product = Product("MacBook Air M2", price=1450, quantity=100)
    # The Product constructor (__init__ method) is called with these values, initializing the product object.
    # 'assert' statements are used to verify that the product's attributes are correctly set.
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_empty_name():
    """
    The test checks that creating a product with an empty name raises an exception.
    """
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        Product("", price=1450, quantity=100)


def test_create_product_with_negative_price():
    """
    The test checks that creating a product with a negative price raises an exception.
    """
    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-115, quantity=100)


def test_product_deactivation_when_quantity_reaches_zero():
    """
    The test checks that the product becomes inactive when its quantity reaches zero.
    """
    product = Product("MacBook Air M2", price=1450, quantity=1)
    # The quantity is set to 1 so that buying this single unit will bring the product's quantity down to zero.
    # This sets up the condition we want to test.
    product.buy(1)  # Buying the last unit
    assert product.is_active() is False
    # After buying the last unit, we check that product.is_active() returns False.
    assert product.get_quantity() == 0
    # This line checks that the product's quantity is indeed zero after the purchase.


def test_product_purchase_modifies_quantity_and_returns_total_price():
    """
    The test checks that purchasing a product modifies quantity correctly and returns the right total price.
    """
    product = Product("MacBook Air M2", price=1450, quantity=10)
    total_price = product.buy(3)    # buy 3 units
    assert total_price == 3 * 1450  # total price should be 3 units times price per unit
    assert product.get_quantity() == 7  # remaining quantity should be 7


def test_buying_more_than_available_quantity():
    """
    The test checks that buying a larger quantity than exists invokes exception.
    """
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(Exception, match="not enough quantity in stock."):
        product.buy(10)     # Attempt to buy more than available
