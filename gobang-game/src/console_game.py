from game import GobangGame

def print_board(game):
    """
    Print the current game board
    """
    print("\nCurrent Board:")
    print(game.get_board_state())
    print(f"Current Player: {'Black (●)' if game.get_current_player() == 1 else 'White (○)'}")

def main():
    """
    Console-based Gobang game
    """
    game = GobangGame()
    
    print("Welcome to Gobang (Five in a Row)!")
    print("Black (●) plays first. Enter coordinates as 'x y'.")
    print("Example: '7 7' places a stone at row 7, column 7.")
    
    while not game.game_over:
        print_board(game)
        
        try:
            move = input("Enter your move (x y): ").split()
            if len(move) != 2:
                print("Invalid input. Please enter two numbers.")
                continue
            
            x, y = map(int, move)
            result = game.play_turn(x, y)
            
            print(result)
            
            if game.game_over:
                print_board(game)
                print(f"Player {game.winner} wins!")
                break
        
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'y':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
