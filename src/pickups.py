class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


class Trap:
    def __init__(self):
        self.name = "trap"
        self.symbol = "T"

    def __str__(self):
        return self.symbol


class Exit:
    def __init__(self):
        self.name = "exit"
        self.symbol = "E"

    def __str__(self):
        return self.symbol


pickups = [
    Item("carrot"),
    Item("apple"),
    Item("strawberry"),
    Item("cherry"),
    Item("watermelon"),
    Item("radish"),
    Item("cucumber"),
    Item("meatball"),
    Item("shovel", value=0, symbol="S"),
    Item("key", value=0, symbol="K"),
    Item("chest", value=0, symbol="C"),
]


def place_random(grid, thing):
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, thing)
            break


def randomize(grid):
    for item in pickups:
        place_random(grid, item)

    # Version 2 extras
    place_random(grid, Trap())
    place_random(grid, Exit())