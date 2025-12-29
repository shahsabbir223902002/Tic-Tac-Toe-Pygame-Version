# Tic-Tac-Toe-Pygame-Version
This project is a Tic-Tac-Toe game developed using Python and Pygame. It features a graphical interface, player name input, turn-based gameplay, win detection with animation, and control buttons for restarting, starting a new game, or exiting. The game demonstrates event handling, game logic, and UI design.

---

## Overview

This is a **Tic-Tac-Toe game built using Pygame**. It allows two players to:

* Enter their names directly in the game window
* Play Tic-Tac-Toe on a **3x3 board**
* See a **win animation** when someone wins
* Restart the game with the same players or start a **new game** with different players
* Exit the game at any time

This project is suitable for learning **Python GUI programming**, **event handling**, and **game logic design**.

---

## Features

* **Player Name Input:** Players can type their names in the start screen.
* **Dynamic Player Info:** Names appear on the screen with their respective symbols (X and O).
* **Game Board:** Centered 3x3 board with clear grid lines.
* **Interactive Gameplay:** Players click on the board to place X or O.
* **Win Detection:** Checks rows, columns, and diagonals for a win.
* **Win Animation:** Blue line highlights the winning row, column, or diagonal.
* **Winning Celebration:** Confetti animation and flashing winner text.
* **Buttons:**

  * **Restart:** Clears the board, same players.
  * **New Game:** Returns to name input screen for new players.
  * **Exit:** Closes the game.

---

## How to Play

1. Run the Python script:

   ```bash
   python tic_tac_toe.py
   ```
2. Enter **Player X** and **Player O** names using the start screen.
3. Press **Enter** to start the game.
4. Click on empty squares to place your symbol.
5. Win by filling a row, column, or diagonal with your symbol.
6. Use the buttons at the bottom to restart, start a new game, or exit.

---

## Installation

1. Make sure Python 3.x is installed.
2. Install Pygame:

   ```bash
   pip install pygame
   ```
3. Run the script:

   ```bash
   python tic_tac_toe.py
   ```

---

## Code Structure

* **Main Script:** Handles game loop, event management, and drawing.
* **Functions:**

  * `draw_start_screen()` – displays the start screen with input boxes.
  * `draw_board()` – draws the Tic-Tac-Toe grid.
  * `draw_player_info()` – displays player names and symbols.
  * `draw_marks()` – draws X and O marks.
  * `draw_buttons()` – displays Restart, New Game, and Exit buttons.
  * `check_win()` – checks winning conditions.
  * `animate_win()` – shows winning line animation.
  * `reset_board()` – resets the board for the same players.
  * `new_game()` – resets board and player names.

---

## Future Improvements

* Add **AI opponent** for single-player mode.
* Implement **scoreboard** to track wins.
* Add **sound effects** for moves and winning.
* Enhance **confetti animation** with particles and colors.

---

## Author

**Md. Shah Emran Hossain Sabbir**.
Green University of Bangladesh.
Department of CSE.

---

