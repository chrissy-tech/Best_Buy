from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total = 0.0
        for product, quantity in shopping_list:
            try:
                if not product.is_active():
                    print(f"⚠️ {product.name} is no longer available.")
                    continue
                if quantity > product.quantity:
                    print(
                        f"⚠️ Not enough stock for {product.name}. "
                        f"Only {product.quantity} available."
                    )
                    continue

                if quantity <= product.quantity:
                    total += product.buy(quantity)

            except Exception as e:
                print(f"⚠️ Error ordering {product.name}: {e}")
                continue

        return total
