import products
import store
import sys


def list_all_products(inventory):
    """List all active products"""
    print("------")
    for index, product in enumerate(inventory.get_all_products(), start=1):
        print(
            f"{index}. {product.name}, Price: ${product.price},"
            f" Qty: {product.quantity}"
        )
    print("------")


def show_total_amount(inventory):
    """Show the total amount of items in store"""
    print("------")
    print(f"Total of {inventory.get_total_quantity()} items in the store")
    print("------")


def make_an_order(inventory):
    """Prompt user to create an order and process it."""
    list_all_products(inventory)
    available_products = inventory.get_all_products()

    print("When you are done selecting products, type 'A'" "to finish the order.")
    order_list = []

    while True:
        prod_choice = input(
            "Choose a product number (1-3) " "or 'A' to finish: "
        ).strip()

        # Exit condition if user types A/a
        if prod_choice.lower() == "a":
            break

        # Validation: must be a digit
        if not prod_choice.isdigit():
            print("Please enter a product NUMBER(1-3) or 'A' to finish.")
            continue

        prod_index = int(prod_choice) - 1

        if not (0 <= prod_index < len(available_products)):
            print("Invalid product number! Please try again.")
            continue

        selected_product = available_products[prod_index]

        if not selected_product.is_active():
            print(f"Sorry, {selected_product.name} is currently out of stock!")
            continue

        # Ask for quantity
        try:
            quantity = int(input("How many items would you like to order? "))
        except ValueError:
            print("Invalid quantity! Must be a number.")
            continue

        if quantity <= 0:
            print("Amount must be at least 1.")
            continue

        if quantity > available_products[prod_index].quantity:
            print(
                f"Sorry, only {available_products[prod_index].quantity} "
                f"in stock! Try again!"
            )
            continue

        # Add selected product to order list
        order_list.append((available_products[prod_index], quantity))
        print(
            f"Added {quantity}" f"× {available_products[prod_index].name} to order.\n"
        )

    # Process the order once after all products are selected
    if order_list:
        total_payment = inventory.order(order_list)
        print("********")
        print(f"Order completed! Total payment: ${total_payment}")
    else:
        print("No products were selected. Order canceled.")


def exit_program(_inventory=None):
    print("Thank you for your purchase!\n")
    sys.exit()


def start(store_p):
    """Run the store menu loop until the user quits."""
    while True:
        print()
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            user_input = int(input("Please choose a number: "))
            if 1 <= user_input <= len(FUNCTIONS):
                FUNCTIONS[user_input](store_p)
            else:
                print("Invalid choice! Please choose a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")


# Map menu choices to functions
FUNCTIONS = {
    1: list_all_products,
    2: show_total_amount,
    3: make_an_order,
    4: exit_program,
}


if __name__ == "__main__":
    """Setup initial stock of inventory"""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)

