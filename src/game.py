from .grid import Grid
from .player import Player
from . import pickups


player = Player(10, 5)  # start near center
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)


def print_status(game_grid):
    """Show the game world and score."""
    print("--------------------------------------")
    point_word = "point" if abs(score) == 1 else "points"
    print(f"You have {score} {point_word}.")
    print(game_grid)


command = "a"

# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, I for inventory, Q/X to quit: ")
    command = command.casefold()[:1]

    dx, dy = 0, 0

    if command == "d":
        dx, dy = 1, 0
    elif command == "a":
        dx, dy = -1, 0
    elif command == "w":
        dx, dy = 0, -1
    elif command == "s":
        dx, dy = 0, 1
    elif command == "i":
        print("Inventory:", inventory)

    if (dx != 0 or dy != 0) and player.can_move(dx, dy, g):
        maybe_item = g.get(player.pos_x + dx, player.pos_y + dy)

        player.move(dx, dy)

        # lose 1 point for each step
        score -= 1

        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            inventory.append(maybe_item.name)

            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")

            g.clear(player.pos_x, player.pos_y)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")