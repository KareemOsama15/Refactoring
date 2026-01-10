class ShoppingCart:
    """
    the goal is to remove the field above, using a list of prices instead:
    def __init__(self):
        self.prices = []
    """

    def __init__(self) -> None:
        self.price = 0
        self.prices = []

    def add(self, price):
        self.price = price
        self.prices = [price]

    def add_item(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.prices.append(price)

    def calculate_total_price(self):
        if self.prices:
            return sum(self.prices)
        return self.price

    def has_discount(self):
        if self.prices:
            return sum(self.prices) >= 100
        return self.price >= 100

    def number_of_products(self):
        if self.prices:
            return len(self.prices)
        return 1


class SomeConsumer:
    def do_stuff():
        shoppingCart = ShoppingCart()
        shoppingCart.add(100)
        print("other consumer", shoppingCart.calculate_total_price())


if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    # shoppingCart.add(10)
    shoppingCart.add_item(20)
    shoppingCart.add_item(100)
    print("number of products:", shoppingCart.number_of_products())
    print("total price:", shoppingCart.calculate_total_price())
    print("has discount:", shoppingCart.has_discount())
