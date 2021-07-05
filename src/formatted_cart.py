class Item:
    def __init__(self, quantity: int, measure: str, name: str, price:int):
        self.quantity   =  quantity
        self.measure    =  measure
        self.name       =  name
        self.price      =  price
        self.real_price =  f"${price}..${price*quantity}"

    def __str__(self):
        return f'    {self.quantity} {self.measure} {self.name}       @ {self.real_price}'

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)
    
    def __format__(self, format_spec):
        if format_spec == "short":
            return ", ".join(sorted(x.name for x in self.items))
        elif format_spec == "long":
            return "\n".join(str(item) for item in self.items)
        else:
            return f'unknown format code {format_spec}'

cart = Cart()
cart.add(Item(2, 'kg', 'cucumbers', 4))
cart.add(Item(1, 'tube', 'toothpaste',2))
cart.add(Item(1, 'box', 'tissues',4))
cart.add(Item(1.5, 'kg', 'a-tomatoes',5))

item = Item(1, 'box', 'tissues', 4)

print(f"Your cart contains: {cart:short}")
print(f"Your cart:\n{cart:long}")

print(f"{item}")



