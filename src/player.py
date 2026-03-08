class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move(self, dx, dy):
        # Flyttar spelaren. "dx" och "dy" är skillnaden
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        # Returnera True om det inte står något i vägen.

        new_x = self.pos_x + dx
        new_y = self.pos_y + dy

        # Check if there is a wall
        if grid.get(new_x, new_y) == grid.wall:
            return False

        return True