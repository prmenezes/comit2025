"""An example of how to create a command line selection process for a fictional storefront."""

from store.item import Item
from store.inventory import Inventory
from store.cart import Cart
from store import cli

        
# welcome user
cli.welcome_prompt()

# create inventory 
# item1 = Item("Gatorade", 4.99)
# item2 = Item("Nintendo Switch", 999.99)

_inventory = [
    ("Nintendo Switch 2", 999.99),
    ("BBQ Chips", 3.50),
    ("Pokemon Booster: Flaming Tides", 7.00),
    ("Gatorade", 5.00),
    ("Milk", 4.99),
    ("Advil", 9.99),
    ("Cat Fud", 49.99)
]

# Write logic to get _inventory (list of tuples) and create an item object for each product in the inventory
# items = []
# for item in _inventory:
#     items.append(Item(item[0], item[1]))

# Create a list of Item objects
items = [ Item(name, price) for name, price in _inventory]


inventory1 = Inventory()

# Write a loop to add item objects from _inventory to inventory1
# inventory1.add_items(item1)
# inventory1.add_items(item2)

for item in items:
    inventory1.add_items(item)

# print inventory 
inventory1.print_inventory()

#get user selection
cart1 = Cart()
while True:
    # Get the user's choice
    selection = cli.get_selection(inventory1)

    if selection is None:
        break
    
    product = inventory1.items[selection - 1]

    
    cart1.add_item_to_cart(product)

cart1.print_cart()
#cart_total = cli.print_inventory(cart.get_cart())
#cli.goodbye_message(cart_total)


# display cart 


# display cart total









# from store import inventory
# from store import cart
# from store import cli

# # Prompt user to enter selection
# cli.welcome_prompt()

# # Print the inventory
# cli.print_inventory(inventory.get_inventory())

# while True:
#     # Get the user's choice
#     selection = cli.get_selection(inventory.get_inventory())

#     if selection is None:
#         break

#     cart.add_item_to_cart(selection)

# cart_total = cli.print_inventory(cart.get_cart())
# cli.goodbye_message(cart_total)
