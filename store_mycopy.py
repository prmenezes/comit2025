"""An example of how to create a command line selection process for a fictional storefront."""

inventory =  [
("Nintendo Switch 2", 999.99),
("BBQ Chips", 3.50),
("Pokemon Booster: Flaming Tides", 7.00),
("Gatorade", 5.00),
("Milk", 4.99),
("Advil", 9.99),
("Cat Fud", 49.99) 
]

cart = []

print("Please select an item to purchase:")


index = 0
for name, cost in inventory:
    index = index + 1
    print(f" {index}. {name}:\t\t\t\t\t${cost}")

while True:

    user_selection = (input("\nEnter the item number or 'c' to checkout: "))

    if user_selection.lower() == 'c':
        break
    
    user_selection = int(user_selection)
    
    # If the user selection is out of the selection range
    if user_selection > len(inventory):
        print(f"\n Please select a number between 1 and {len(inventory)}")
        continue
    cart.append(inventory[user_selection - 1])

# Calculate the total price
sum = 0
# Calculate sum total only if item exists in the cart
if len(cart):
    for item in cart:
        sum = sum + item[1]
    print(f"\nYour total cost is ${sum}")
# Else nothing to checkout
else:
    print("\nNothing to checkout!")  

print("\nThank you, come again!")