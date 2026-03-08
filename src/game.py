from .grid import Grid
from .player import Player
from . import pickups


player = Player(10, 5)  # start near center
score = 0
inventory = []
original_items_left = 0

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)

# Count original collectible things needed before exit works
for y in range(g.height):
    for x in range(g.width):
        cell = g.get(x, y)
        if isinstance(cell, pickups.Item) and cell.name not in ["shovel", "key", "chest"]:
            original_items_left += 1


def print_status(game_grid):
    """Show the game world and score."""
    print("--------------------------------------")
    point_word = "point" if abs(score) == 1 else "points"
    print(f"You have {score} {point_word}.")
    print(game_grid)


def has_item(item_name):
    return item_name in inventory


def remove_item(item_name):
    if item_name in inventory:
        inventory.remove(item_name)


command = "a"

while command not in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, I for inventory, Q/X to quit: ")
    command = command.casefold().strip()

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
        continue
    elif command in ["q", "x"]:
        break
    else:
        continue

    target_x = player.pos_x + dx
    target_y = player.pos_y + dy
    maybe_item = g.get(target_x, target_y)

    # Version 2 J: shovel breaks next wall
    if maybe_item == g.wall:
        if has_item("shovel"):
            print("You use the shovel and break the wall!")
            remove_item("shovel")
            g.clear(target_x, target_y)
        else:
            print("You hit a wall!")
        continue

    player.move(dx, dy)
    score -= 1  # floor is lava

    current_tile = g.get(player.pos_x, player.pos_y)

    # Version 2 I: traps
    if isinstance(current_tile, pickups.Trap):
        score -= 10
        print("You stepped on a trap! -10 points.")

    # Version 2 M: exit
    elif isinstance(current_tile, pickups.Exit):
        if original_items_left == 0:
            print("You reached the exit and won the game!")
            break
        else:
            print("The exit is locked. Collect all original fruits first.")

    # Version 2 K: normal items, shovel, key, chest
    elif isinstance(current_tile, pickups.Item):
        if current_tile.name == "chest":
            if has_item("key"):
                remove_item("key")
                score += 100
                inventory.append("treasure")
                print("You opened a chest with a key! +100 points.")
                g.clear(player.pos_x, player.pos_y)
            else:
                print("You found a chest, but you need a key.")
        else:
            score += current_tile.value
            inventory.append(current_tile.name)

            if current_tile.name == "key":
                print("You found a key.")
            elif current_tile.name == "shovel":
                print("You found a shovel.")
            else:
                print(f"You found a {current_tile.name}, +{current_tile.value} points.")
                original_items_left -= 1

            g.clear(player.pos_x, player.pos_y)

print("Thank you for playing!")