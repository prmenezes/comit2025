"""An example of how to create a command line selection process for a fictional storefront."""

from store import inventory
from store.cart import CartItem, Cart
from store import cli

# Prompt user to enter selection
cli.welcome_prompt()

# Print the inventory
cli.print_inventory(inventory.get_inventory())

cart_list = []

CART = Cart(is_private=True)
# CART1 = cart.make_new_cart()
# CART2 = cart.make_new_cart()

# cart_list.append(CART1)
# cart_list.append(CART2)

for CART in cart_list:
    while True:
        # Get the user's choice
        selection = cli.get_selection(inventory.get_inventory())

        if selection is None:
            break

        #cart.add_item_to_cart(CART, selection)
        item = CartItem(name=selection[0], price=selection[1])
        CART.add_item(item)
        

# cart_total = cli.print_inventory(cart.get_cart(CART1))
# cart_total2 = cli.print_inventory(cart.get_cart(CART2))
cart_total = cli.print_inventory(cart.get_cart(CART1))
cli.goodbye_message(cart_total)
#cli.goodbye_message(cart_total2)
