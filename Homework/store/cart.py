from random import Random

#_cart = []

_carts: dict[str, list] = {}
_is_private = []

def make_new_cart():
     id = str(Random().randint(0, 9999999999))
     _carts[id] = []
     return id

def add_item_to_cart(cart_id, item):
     _carts[cart_id].append(item)

def get_cart(cart_id): 
     return _carts[cart_id]   

def is_private(cart_id):
     return cart_id in _is_private




class CartItem:

     def __init__(self, name: str, price: float):
          self.name = name
          self.price = price


class Cart:

     
     def __init__(self, is_private: bool):
          self.id = str(Random().randint(0, 9999999999))
          self.is_private = is_private
          self.items = []

     
     def add_item(self, item: CartItem):
          self.items.append(item)


     
