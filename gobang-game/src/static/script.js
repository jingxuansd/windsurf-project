class GobangGame {
    constructor() {
        this.board = document.querySelector('.board');
        this.statusElement = document.querySelector('.status');
        this.resetButton = document.querySelector('.reset-button');
        this.gameOverOverlay = document.querySelector('.game-over-overlay');
        this.winnerText = document.querySelector('.winner-text');
        this.playAgainButton = document.querySelector('.play-again-button');
        
        this.currentPlayer = 'black';
        this.gameOver = false;
        this.cells = [];
        this.BOARD_SIZE = 15;
        this.CELL_SIZE = 35;
        this.BOARD_PADDING = 20;
        this.winningCells = [];
        
        this.initializeBoard();
        this.bindEvents();
    }

    initializeBoard() {
        this.board.innerHTML = '';
        this.cells = Array(this.BOARD_SIZE).fill().map(() => Array(this.BOARD_SIZE).fill(null));
        this.winningCells = [];
        
        for (let i = 0; i < this.BOARD_SIZE; i++) {
            for (let j = 0; j < this.BOARD_SIZE; j++) {
                const cell = document.createElement('div');
                cell.className = 'cell';
                cell.dataset.row = i;
                cell.dataset.col = j;
                cell.style.left = `${this.BOARD_PADDING + j * this.CELL_SIZE}px`;
                cell.style.top = `${this.BOARD_PADDING + i * this.CELL_SIZE}px`;
                this.board.appendChild(cell);
                this.cells[i][j] = cell;
            }
        }

        this.currentPlayer = 'black';
        this.gameOver = false;
        this.hideGameOverModal();
        this.updateStatus();
    }

    bindEvents() {
        this.board.addEventListener('click', (e) => {
            if (this.gameOver) return;
            
            const cell = e.target;
            if (!cell.classList.contains('cell') || 
                cell.classList.contains('black') || 
                cell.classList.contains('white')) {
                return;
            }

            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);
            
            this.makeMove(row, col);
        });

        this.resetButton.addEventListener('click', () => this.initializeBoard());
        this.playAgainButton.addEventListener('click', () => this.initializeBoard());
    }

    makeMove(row, col) {
        const cell = this.cells[row][col];
        cell.classList.add(this.currentPlayer);

        if (this.checkWin(row, col)) {
            this.gameOver = true;
            this.showWinner();
            return;
        }

        this.currentPlayer = this.currentPlayer === 'black' ? 'white' : 'black';
        this.updateStatus();
    }

    checkWin(row, col) {
        const directions = [
            [0, 1],   // horizontal
            [1, 0],   // vertical
            [1, 1],   // diagonal \
            [1, -1]   // diagonal /
        ];

        for (const [dx, dy] of directions) {
            let count = 1;
            this.winningCells = [[row, col]];
            
            // Check in positive direction
            count += this.countDirection(row, col, dx, dy, true);
            // Check in negative direction
            count += this.countDirection(row, col, -dx, -dy, true);

            if (count >= 5) {
                this.highlightWinningCells();
                return true;
            }
            
            this.winningCells = [];
        }

        return false;
    }

    countDirection(row, col, dx, dy, collectCells = false) {
        const player = this.currentPlayer;
        let count = 0;
        let x = row + dx;
        let y = col + dy;

        while (x >= 0 && x < this.BOARD_SIZE && y >= 0 && y < this.BOARD_SIZE) {
            if (!this.cells[x][y].classList.contains(player)) break;
            count++;
            if (collectCells) {
                this.winningCells.push([x, y]);
            }
            x += dx;
            y += dy;
        }

        return count;
    }

    highlightWinningCells() {
        for (const [row, col] of this.winningCells) {
            this.cells[row][col].classList.add('winning');
        }
    }

    showWinner() {
        const winner = this.currentPlayer.charAt(0).toUpperCase() + this.currentPlayer.slice(1);
        this.winnerText.innerHTML = `<span>${winner}</span> Wins!`;
        this.gameOverOverlay.classList.add('active');
        this.statusElement.textContent = `Game Over - ${winner} Wins!`;
    }

    hideGameOverModal() {
        this.gameOverOverlay.classList.remove('active');
        // Remove winning highlights
        document.querySelectorAll('.cell.winning').forEach(cell => {
            cell.classList.remove('winning');
        });
    }

    updateStatus() {
        if (!this.gameOver) {
            const player = this.currentPlayer.charAt(0).toUpperCase() + this.currentPlayer.slice(1);
            this.statusElement.textContent = `Current player: ${player}`;
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new GobangGame();
});
