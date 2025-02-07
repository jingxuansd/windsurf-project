class GobangBoard:
    def __init__(self, size=15):
        """
        Initialize the Gobang board
        :param size: Board size (default 15x15)
        """
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.current_player = 1  # 1 for black, 2 for white

    def place_stone(self, x, y):
        """
        Place a stone on the board
        :param x: x-coordinate
        :param y: y-coordinate
        :return: True if placement is valid, False otherwise
        """
        if not (0 <= x < self.size and 0 <= y < self.size):
            return False
        
        if self.board[y][x] != 0:
            return False
        
        self.board[y][x] = self.current_player
        return True

    def check_win(self, x, y):
        """
        Check if the last placed stone results in a win
        :param x: x-coordinate of last stone
        :param y: y-coordinate of last stone
        :return: True if there's a win, False otherwise
        """
        directions = [
            (1, 0),   # horizontal
            (0, 1),   # vertical
            (1, 1),   # diagonal \
            (1, -1)   # diagonal /
        ]
        
        player = self.board[y][x]
        
        for dx, dy in directions:
            count = self.count_consecutive(x, y, dx, dy, player) + \
                    self.count_consecutive(x, y, -dx, -dy, player) - 1
            
            if count >= 5:
                return True
        
        return False

    def count_consecutive(self, x, y, dx, dy, player):
        """
        Count consecutive stones in a given direction
        :param x: starting x-coordinate
        :param y: starting y-coordinate
        :param dx: x-direction to check
        :param dy: y-direction to check
        :param player: player to check for
        :return: number of consecutive stones
        """
        count = 0
        current_x, current_y = x, y
        
        while (0 <= current_x < self.size and 
               0 <= current_y < self.size and 
               self.board[current_y][current_x] == player):
            count += 1
            current_x += dx
            current_y += dy
        
        return count

    def switch_player(self):
        """
        Switch current player
        """
        self.current_player = 3 - self.current_player  # Toggle between 1 and 2

    def reset(self):
        """
        Reset the board to initial state
        """
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 1

    def __str__(self):
        """
        String representation of the board
        """
        board_str = ""
        for row in self.board:
            board_row = []
            for cell in row:
                if cell == 0:
                    board_row.append('.')
                elif cell == 1:
                    board_row.append('●')  # Black stone
                else:
                    board_row.append('○')  # White stone
            board_str += ' '.join(board_row) + '\n'
        return board_str
