from models import GameMap
import os

class Renderer:

    def __init__(self, game_map : GameMap):
        self.game_map = game_map
        ...

    def render_map(self):

        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        row, col = self.game_map.map_size
        cell_width = 5
        border = f"{'':-^{col * (cell_width + 1) + 1}}"

        print(border)
        for i in range(row):
            print("|", end="")
            for j in range(col):
                num = self.game_map.get_tile_by_pos((i, j))
                cell = "" if num == 0 else num
                print(f"{cell:^{cell_width}}", end="|")
            print("")
            print(border)
        ...

    ...

if __name__ == "__main__":
    ...