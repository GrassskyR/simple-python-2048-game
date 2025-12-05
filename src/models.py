import random
import copy

class GameMap:

    def __init__(self, map_size : tuple[int, int]):
        self.map_size = map_size
        self.game_map : list[list[int]] = []

    def init_map(self):     # init game map
        row, col = self.map_size

        for i in range(row):
            self.game_map.append([])
            for j in range(col):
                self.game_map[i].append(0)

    def get_tile_by_pos(self, pos : tuple[int, int]) -> int:    # return -1 if invalid position is used
        row, col = pos
        max_row, max_col = self.map_size
        # Check for negative indices and out of bounds
        if row < 0 or col < 0 or row >= max_row or col >= max_col:
            return -1
        try:
            return self.game_map[row][col]
        except IndexError:
            return -1

    def set_tile_by_pos(self, pos : tuple[int, int], value : int):
        row, col = pos
        self.game_map[row][col] = value

    def spawn_number(self):
        row, col = self.map_size

        empty_slot = []

        for i in range(row):
            for j in range(col):
                if self.get_tile_by_pos((i, j)) == 0:
                    empty_slot.append((i, j))

        if empty_slot:
            r_pos = random.choice(empty_slot)
            self.set_tile_by_pos(r_pos, 2)

    def get_all_tile_sum(self):
        row, col = self.map_size
        sum = 0
        for i in range(row):
            for j in range(col):
                sum += self.get_tile_by_pos((i, j))
    
    def has_empty_slot(self) -> bool:
        row, col = self.map_size
        for i in range(row):
            for j in range(col):
                return (self.get_tile_by_pos((i, j)) == 0)
        ...

    def is_tile_moveable(self, pos : tuple[int, int]) -> bool:
        row, col = pos
        
        tile = self.get_tile_by_pos((row, col))

        left_tile = self.get_tile_by_pos((row, col - 1))
        right_tile = self.get_tile_by_pos((row, col + 1))
        up_tile = self.get_tile_by_pos((row - 1, col))
        down_tile = self.get_tile_by_pos((row + 1, col))
        
        surrounding_tile = [left_tile, right_tile, up_tile, down_tile]

        if tile in surrounding_tile or 0 in surrounding_tile:
            return True
        else:
            return False
        ...

class CalculateTile():

    def __init__(self, game_map : GameMap):
        self.game_map = game_map
        ...

    def calculate_number(self, direction : str):

        row, col = self.game_map.map_size

        match direction:    # Same col different row
            case 'w':
                row -= 1

                copied_map = copy.deepcopy(self.game_map.game_map)

                while row > 0:
                    for i in range(col):
                        cur_tile_pos = (row, i)
                        next_tile_pos = (row - 1, i)

                        cur_tile = self.game_map.get_tile_by_pos(cur_tile_pos)
                        next_tile = self.game_map.get_tile_by_pos(next_tile_pos)
                        if cur_tile == next_tile or next_tile == 0:
                            t = cur_tile + next_tile
                            self.game_map.set_tile_by_pos(cur_tile_pos, 0)
                            self.game_map.set_tile_by_pos(next_tile_pos, t)
                    row -= 1

                if copied_map != self.game_map.game_map:
                    self.calculate_number(direction)

            case 'a':   # Same row different col
                col -= 1

                copied_map = copy.deepcopy(self.game_map.game_map)

                while col > 0:
                    for i in range(row):
                        cur_tile_pos = (i, col)
                        next_tile_pos = (i, col - 1)

                        cur_tile = self.game_map.get_tile_by_pos(cur_tile_pos)
                        next_tile = self.game_map.get_tile_by_pos(next_tile_pos)
                        if cur_tile == next_tile or next_tile == 0:
                            t = cur_tile + next_tile
                            self.game_map.set_tile_by_pos(cur_tile_pos, 0)
                            self.game_map.set_tile_by_pos(next_tile_pos, t)
                    col -= 1

                if copied_map != self.game_map.game_map:
                    self.calculate_number(direction)
                
                ...

            case 's':
                j = 0

                copied_map = copy.deepcopy(self.game_map.game_map)

                while j < row - 1:
                    for i in range(col):
                        cur_tile_pos = (j, i)
                        next_tile_pos = (j + 1, i)

                        cur_tile = self.game_map.get_tile_by_pos(cur_tile_pos)
                        next_tile = self.game_map.get_tile_by_pos(next_tile_pos)
                        if cur_tile == next_tile or next_tile == 0:
                            t = cur_tile + next_tile
                            self.game_map.set_tile_by_pos(cur_tile_pos, 0)
                            self.game_map.set_tile_by_pos(next_tile_pos, t)
                    j += 1

                if copied_map != self.game_map.game_map:
                    self.calculate_number(direction)

            case 'd':
                j = 0

                copied_map = copy.deepcopy(self.game_map.game_map)

                while j < col - 1:
                    for i in range(row):
                        cur_tile_pos = (i, j)
                        next_tile_pos = (i, j + 1)

                        cur_tile = self.game_map.get_tile_by_pos(cur_tile_pos)
                        next_tile = self.game_map.get_tile_by_pos(next_tile_pos)
                        if cur_tile == next_tile or next_tile == 0:
                            t = cur_tile + next_tile
                            self.game_map.set_tile_by_pos(cur_tile_pos, 0)
                            self.game_map.set_tile_by_pos(next_tile_pos, t)
                    j += 1

                if copied_map != self.game_map.game_map:
                    self.calculate_number(direction)


        ...

if __name__ == "__main__":
    ...