from board import GobangBoard

class GobangGame:
    def __init__(self, board_size=15):
        """
        Initialize the Gobang game
        :param board_size: Size of the game board
        """
        self.board = GobangBoard(board_size)
        self.game_over = False
        self.winner = None

    def play_turn(self, x, y):
        """
        Play a turn by placing a stone
        :param x: x-coordinate
        :param y: y-coordinate
        :return: Result of the turn
        """
        if self.game_over:
            return "Game is already over"

        if not self.board.place_stone(x, y):
            return "Invalid move"

        if self.board.check_win(x, y):
            self.game_over = True
            self.winner = self.board.current_player
            return f"Player {self.winner} wins!"

        self.board.switch_player()
        return "Move successful"

    def reset_game(self):
        """
        Reset the game to initial state
        """
        self.board.reset()
        self.game_over = False
        self.winner = None

    def get_board_state(self):
        """
        Get current board state
        :return: String representation of board
        """
        return str(self.board)

    def get_current_player(self):
        """
        Get current player
        :return: Current player number
        """
        return self.board.current_player
