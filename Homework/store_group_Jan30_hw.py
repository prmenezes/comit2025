
def print_inventory(inventory: list[tuple[str, float]]) -> None:
    """Prints a list of inventory to the console

    Args:
        inventory (list[tuple(str, float)]): List of items to print
    """
    index = 0
    for name, cost in inventory:
        index = index + 1
        print(f"  {index}. {name}: ${cost}")

def get_user_input(cart):
    """Gets user input, add items to cart based on selection and return cart

    Args:
    
    
    """
    while True:
        user_selection = input("Enter 'C' to checkout or select item number from above: ")  
        if(user_selection.lower() == 'c'):
            break
            
        user_selection = int(user_selection)
        if(user_selection <= len(inventory) ):
            print("Please select the items listed above")
            continue
        cart.append(inventory[user_selection - 1])
    return cart

def print_cart_total_amount(cart):

    total = 0
    for item in cart:
            total = total + item[1]
    print("Total price is", total)
        

# _variable_name means do not access this varible
inventory = [
    ("Nintendo Switch 2", 999.99),
    ("BBQ Chips", 3.50),
    ("Pokemon Booster: Flaming Tides", 7.00),
    ("Gatorade", 5.00),
    ("Milk", 4.99),
    ("Advil", 9.99),
    ("Cat Fud", 49.99)
]
cart = []

while True:
    print("Please select an item to purchase:")

    # Print inventory
    print_inventory(inventory)

    # Get user selection
    cart = get_user_input(cart)

    break

# Print cart 
#print_inventory(cart)

# Print cart total
print_cart_total_amount(cart)

print("Thank you, come again!")