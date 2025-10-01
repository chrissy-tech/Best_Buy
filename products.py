class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a product with name, price and quantity."""

        if not isinstance(name, str) or not name:
            raise TypeError("Name can not be empty")

        # Ensure price is a non-negative number.
        if not isinstance(price, (int, float)) or price < 0:
            raise TypeError("Price must be a number >0")

        # Ensure quantity is a non-negative integer.
        if not isinstance(quantity, int) or quantity < 0:
            raise TypeError("Quantity must be a number >0")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = self.quantity > 0

    def get_quantity(self):
        """Return the quantity of the product."""
        return int(self.quantity)

    def set_quantity(self, quantity):
        """Set the quantity of the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        self.active = quantity > 0

    def is_active(self):
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Display the products."""
        print(f"{self.name}, Price: {self.price}, " f"Quantity: {self.quantity}")

    def buy(self, amount):
        """Reduce stock by given quantity and return total price."""
        if not self.active:
            raise Exception("Product is not available.")
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")
        if amount > self.quantity:
            raise ValueError("Not enough quantity in stock.")

        total_price = amount * self.price
        self.quantity -= amount

        # deactivate when no product available anymore
        if self.quantity == 0:
            self.deactivate()

        return total_price

