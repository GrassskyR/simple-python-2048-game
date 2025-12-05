from game import GameManager

def main():
    game = GameManager()
    while True:
        print("Chose a option (1) (2)")
        print("1. Start Game")
        print("2. Exit")
        try:
            user_input = int(input())
            match user_input:
                case 1:
                    game.run()
                case 2:
                    break

        except ValueError:
            print("InValid Option. Exiting...")
            break
        

if __name__ == "__main__":
    main()
    pass