from models import GameMap
from models import CalculateTile
from view import Renderer
from pynput import keyboard
from copy import deepcopy

class GameManager:

    __CONTROLS = ['w','s','a','d']

    def __init__(self):
        self.map_size = (4, 4)  # default map size 4x4
        self.isRunning = True
        self.listener = None
        self.key_buffer = ""
        self.game_map = None
        self.render = None
        self.calculator = None
        ...
    ...

    def on_press(self, key):
        try:
            self.key_buffer = key.char
            print(self.key_buffer)
        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.is_running = False
            return False

    def setup_game(self):
        try:
            user_input = input("Enter Map Size (row, col) [Default 4,4]: \n")
            if user_input.strip():
                row, col = map(int, user_input.split(","))
                self.map_size = (row, col)
        except ValueError:
            print("Invalid input, using default 4x4")
            ...

        self.game_map = GameMap(self.map_size)
        self.game_map.init_map()

        for _ in range(2):  # spawn two number when game start
            self.game_map.spawn_number()

        self.listener = keyboard.Listener(  # init control
            on_press=self.on_press,
            on_release=self.on_release
        )

        self.render = Renderer(self.game_map)
        self.calculator = CalculateTile(self.game_map)

    def check_is_map_stuck(self) -> bool:
        row, col = self.map_size

        tile_movable_status = []

        for i in range(row):
            for j in range(col):
                if self.game_map.get_tile_by_pos((i, j)):
                    tile_movable_status.append(self.game_map.is_tile_moveable((i, j)))

        is_stuck = not any(tile_movable_status)

        return is_stuck

    def run(self):
        self.setup_game()
        self.listener.start()
        self.render.render_map()
        with keyboard.Events() as events:
            for event in events:
                if isinstance(event, keyboard.Events.Press):
                    if self.key_buffer in self.__CONTROLS:
                        self.calculator.calculate_number(self.key_buffer)

                        self.game_map.spawn_number()
                            
                        self.render.render_map()
                        # print(self.check_is_map_stuck())

                    if self.check_is_map_stuck():
                        self.render.render_map()
                        print("Game Over")
                        break
        ...

if __name__ == "__main__":
    game = GameManager()
    game.run()
    ...