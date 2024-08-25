from typing import List, Tuple
from store import Store
from products import Product, NonStockedProduct, LimitedProduct


def display_menu():
    """
        Displays the main menu options for the store.
    """
    print()
    print("Store Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_all_products(store: Store):
    """
        Lists all active products in the store.
    """
    # pass the Store object to interact with its methods.
    # The store parameter should be an instance of the Store class.
    products = store.get_all_products()
    # Retrieve Products: Use store method to get a list of active products.
    if not products:  # If there are no active products:
        print("no products available.")
        return  # immediately exits the function, if there are no products to list
    print("------")
    for index, product in enumerate(products):
        product_num = index + 1
        print(f"{product_num}. {product.show()}")


def show_total_amount(store: Store):
    """
        Shows the total quantity of all products in the store.
    """
    total_quantity = store.get_total_quantity()
    print(f"Total of {total_quantity} items in store.")


def make_order(store: Store):
    """
       Prompts the user to make an order by selecting products and specifying quantities.
       Args:
           store (Store): The store instance containing the products.
       Raises:
           ValueError: If the input for product number or amount is not a valid integer.
           Exception: If the product is not found in the store.
    """
    print("When you want to finish order, enter empty text.")
    shopping_list: List[Tuple[Product, int]] = []
    products = store.get_all_products()
    while True:
        try:
            product_num = input("Which product # do you want? ")
            if product_num == "":
                break

            product_num = int(product_num)
            if product_num < 1 or product_num > len(products):
                continue

            product = products[product_num - 1]
            # If product_num is 1, subtracting 1 gives 0, index for the first element in the list.

            amount = int(input("What amount do you want? "))
            if amount < 1:
                continue

            shopping_list.append((product, amount))
            print("Product added to your list!")
            print()
        except ValueError:
            print()
            continue

    try:
        total_order = store.order(shopping_list)
        print("********")
        print(f"Order accepted! Total payment: ${total_order}")
    except ValueError as value_error:
        print(str(value_error))
    except Exception as general_exception:
        print(str(general_exception))


def start(store: Store):
    """
        Starts the store application, displaying the menu and processing user input.
    """
    while True:
        display_menu()
        enter_choice = input("Please choose a number (1-4): ")
        print()
        if enter_choice == "1":
            list_all_products(store)
            print("------")
            continue
        if enter_choice == "2":
            show_total_amount(store)
            print("------")
            continue
        if enter_choice == "3":
            list_all_products(store)
            print("------")
            make_order(store)
            print("------")
            continue
        if enter_choice == "4":
            break


# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
                NonStockedProduct("Windows License", price=125),
                LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]
best_buy = Store(product_list)

if __name__ == "__main__":
    start(best_buy)  # Ensure you're passing the instance, not the class
