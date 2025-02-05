# Snake Game 🐍

 - A simple and interactive Snake Game built using Python's Tkinter library, where the player controls the snake to collect food and avoid colliding with the walls or its own body.

## Features:
- **Movement:** The player can move the snake in four directions (Up, Down, Left, Right).
- **Game Over:** The game ends when the snake collides with the wall or itself.
- **Score:** The score increases every time the snake eats food, and the difficulty increases as the score goes up.
- **Speed Adjustment:** The speed of the snake increases as the score increases.
- **Game Over Popup:** After the game ends, the player can choose to restart the game or quit.

## How to Play:
1. Use the arrow keys (`↑`, `↓`, `←`, `→`) to move the snake.
2. Eat the red food to grow the snake and increase your score.
3. Avoid running into walls or the snake's own body.
4. If you lose, you can choose to restart the game or quit.

## Technologies Used:
- **Python:** The game is implemented in Python.
- **Tkinter:** Tkinter is used for creating the graphical user interface (GUI), which includes drawing the snake, food, and score.
- **Time module:** Used for tracking the elapsed time during the game.

## Game Design:
- **Tile System:** The game grid is divided into 30 rows and 30 columns, each tile having a size of 25x25 pixels.
- **Snake Movement:** The snake's position is updated based on keyboard input. The snake moves one tile at a time in the chosen direction.
- **Food:** Food spawns at random positions on the grid and increases the length of the snake when eaten.
- **Speed:** The snake's speed starts at 90ms and decreases (i.e., the snake moves faster) as the score increases in multiples of 5.
