from store.item import Item

class Cart:
    def __init__(self, is_private: bool = True):
        self.cart = []
        self.is_private = is_private

    def add_item_to_cart(self, item: Item):
        self.cart.append(item)

    def print_cart(self):
        for index, item in enumerate(self.cart, start = 1):
            print(f'{index}. {item.get_item()}')
     #    index = 1
     #    for item in self.cart:
     #        print(f"{index}. {item.get_item()}")
     #        index += 1


    def get_cart_total(self) -> float:
        total = 0
        for item in self.cart:
            total += item.price
        return total
            
        
        


# _cart = []

# def add_item_to_cart(item):
#      _cart.append(item)

# def get_cart():
#      return _cart
