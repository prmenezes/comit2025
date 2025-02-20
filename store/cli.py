from store.inventory import Inventory

def get_selection(inventory: Inventory) -> int | None:
    """_summary_


    Args:

    Returns:
    """
    while True:
        user_selection = input(
            "Enter 'C' to checkout or select item number from above: "
        )

        if user_selection == "🥰":
            print("Awwww, that's cute! 10% discount!")

        if user_selection.lower() == "c":
            return None
        
        try:
            selected_index = int(user_selection)
        except:
            print("Invalid input")
            continue
        
        number_of_items_in_inventory = inventory.get_number_of_items_in_inventory()
        if selected_index <= 0 or selected_index > number_of_items_in_inventory:
            print(f"Invalid input, select a number from 1 to {number_of_items_in_inventory}")
            continue

        return selected_index


# def print_inventory(inventory: list[tuple[str, float]]) -> float:
#     """Prints a list of inventory to the console

#     Args:
#         inventory (list[tuple[str, float]]): List of items to print.
#     """
#     index = 0
#     total = 0
#     for name, cost in inventory:
#         index = index + 1
#         print(f"  {index}. {name}: ${cost}")
#         total = total + cost
#     return total


def welcome_prompt():
    # Prompt user to enter selection
    print("Please select an item to purchase:")


def goodbye_message(cart_total):
    print("Total is ", cart_total)
    print("Thank you, come again!")
