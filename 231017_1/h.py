class House:
    def __init__(self,price):
        self.price = price

obj = House(2000)
print(obj.price)
obj.price = 4000
print(obj.price)
