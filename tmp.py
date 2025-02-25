# _inventory = [
#     ("Nintendo Switch 2", 999.99),
#     ("BBQ Chips", 3.50),
#     ("Pokemon Booster: Flaming Tides", 7.00),
#     ("Gaterade", 5.00),
#     ("Milk", 4.99),
#     ("Advil", 9.99),
#     ("Cat Fud", 49.99)
# ]

class Items:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    
    def print_item(self):
        return f"{self.id} - {self.name}: {self.price},  Stock: {self.stock}"
    
    def available_to_purchase(self):
        if self.stock > 0:
            return True
        else:
            return False
    
    def add_stock(self, stock):
        self.stock = self.stock + stock
    
new_item = Items(1, "Nintendo Switch", 299.99, 0)
new_item_2 = Items(2, "BBQ Chips", 299.99, 20)

print(new_item.print_item())
print("Is it available?", new_item.available_to_purchase())
print("Is it available?", new_item_2.available_to_purchase())
new_item.add_stock(5)
print(new_item.print_item())
print("Is it available?", new_item.available_to_purchase())