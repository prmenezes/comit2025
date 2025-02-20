from store.item import Item
class Cart:
    
    def __init__(self):
        self.cart = []

    def add_item_to_cart(self, item: Item):
        self.cart.append(item)

    def print_cart(self):
        index = 1
        for item in self.cart:
            print(f'{index}. {item.get_item()}')
            index += 1





# _cart = []

# def add_item_to_cart(item):
#      _cart.append(item)

# def get_cart(): 
#      return _cart   