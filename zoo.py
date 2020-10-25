class Zoo:
    def __init__(self, price=0, discount=0):
        self.price = price
        self.discount = discount

    def __str__(self):
        return "[Price=" + str(self.price) + "; Discount=" + str(self.discount) + ";]"
