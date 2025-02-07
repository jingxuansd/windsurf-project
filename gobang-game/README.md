# Gobang (Five in a Row) Game

## Overview
This is a classic Gobang game implemented in Python. Players take turns placing stones on a 15x15 grid, with the goal of getting five stones in a row.

## Features
- Console-based gameplay
- Supports two players (Black and White)
- Win condition detection
- Game reset functionality

## Requirements
- Python 3.7+
- Optional: Pygame (for future GUI implementation)

## Installation
1. Clone the repository
2. Create a virtual environment (optional but recommended)
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Play
Run the console game:
```
python src/console_game.py
```

Game Rules:
- Black (●) plays first
- Players take turns placing stones
- Enter coordinates as 'x y' (e.g., '7 7')
- First player to get 5 stones in a row (horizontal, vertical, or diagonal) wins

## Future Improvements
- Graphical User Interface (GUI)
- AI opponent
- Online multiplayer

## Contributions
Feel free to open issues or submit pull requests!
