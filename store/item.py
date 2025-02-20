""" An Item with name and price """
class Item:
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
    def get_item(self) -> str:
        """ Returns item's name and price in a printable format
        Returns:
            str: "name: price"
        """
        return f"{self.name}: {self.price}"