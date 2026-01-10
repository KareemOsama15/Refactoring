class ShoppingCart:
    """
    the goal is to remove the field above, using a list of prices instead:
    def __init__(self):
        self.prices = []
    """

    def __init__(self) -> None:
        self.prices = []

    def add(self, price) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.prices.append(price)

    def calculate_total_price(self) -> int:
        return sum(self.prices)

    def has_discount(self) -> bool:
        return sum(self.prices) >= 100

    def number_of_products(self) -> int:
        return len(self.prices)


class SomeConsumer:
    def do_stuff():
        shoppingCart = ShoppingCart()
        shoppingCart.add(100)
        print("other consumer", shoppingCart.calculate_total_price())


if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    shoppingCart.add(90)
    shoppingCart.add(20)
    print("number of products:", shoppingCart.number_of_products())
    print("total price:", shoppingCart.calculate_total_price())
    print("has discount:", shoppingCart.has_discount())
