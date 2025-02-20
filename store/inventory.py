from store.item import Item
class Inventory:
    
    def __init__(self):
        self.items = []
        
    def add_items(self, item: Item):
        self.items.append(item)
        
    def print_inventory(self):
        index = 1
        for item in self.items:
            print(f'{index}. {item.get_item()}')
            index += 1

    def get_number_of_items_in_inventory(self):
        return len(self.items)






# _inventory = [
#     ("Nintendo Switch 2", 999.99),
#     ("BBQ Chips", 3.50),
#     ("Pokemon Booster: Flaming Tides", 7.00),
#     ("Gaterade", 5.00),
#     ("Milk", 4.99),
#     ("Advil", 9.99),
#     ("Cat Fud", 49.99)
# ]


# def get_inventory():
#      return _inventory