class AssertClass:
    def __init__(self,name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity        

        assert type(name) == str, "Name must be a string"
        assert type(price) == int, "Price must be a positive number"
        assert type(quantity) == int, "quantity must be a number"
        assert quantity >= 0, "Quantity must be a be a positive numer number"
        
    def calculate_total_price(self):
        return self.price * self.quantity


# assert1 = AssertClass('Samsung', 900, "5")
assert1 = AssertClass('Samsung', 900, 2)
assert2 = AssertClass('Oppo', 700)
print(assert1.calculate_total_price())
print(assert2.calculate_total_price())