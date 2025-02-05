import tkinter
import random
import time
from tkinter import messagebox  # To use message boxes

rows = 30  
colums = 30
tile_size = 25
width = tile_size * rows
height = tile_size * colums
speed = 90  # Initial speed for the snake

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Game window
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=width, height=height, borderwidth=0)
canvas.pack()
window.update()

# Center the window
window_height = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
windowX = int((screen_width / 2) - (window_width / 2))
windowY = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{windowX}+{windowY}")

# Initialize snake and food
snake = Tile(5 * tile_size, 5 * tile_size)
food = Tile(10 * tile_size, 10 * tile_size)
velocityX = 0
velocityY = 0
snake_body = []  # Multiple snake tiles
GameOver = False
score = 0
start_time = time.time()  # Start timer

# Change direction on key press
def changeDirection(e):
    global velocityX, velocityY, GameOver, score
    if GameOver:
        return
    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0

# Move the snake
def move():
    global snake, food, snake_body, GameOver, score, speed
    if GameOver:
        return
    if (snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height):
        GameOver = True
        gameOver()  # Call the game over function
        return
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            GameOver = True
            gameOver()  # Call the game over function
            return

    # Collision with food
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, colums - 1) * tile_size
        food.y = random.randint(0, rows - 1) * tile_size
        score += 1

    # Update snake body
    for i in range(len(snake_body) - 1, -1, -1):
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            prevTile = snake_body[i-1]
            tile.x = prevTile.x
            tile.y = prevTile.y

    snake.x += velocityX * tile_size
    snake.y += velocityY * tile_size

    # Increase speed every 5 points
    if score % 5 == 0:
        speed = 100 - (score // 5)  # Reduce the speed (increase the game difficulty)

# Game Over function with "Try Again" option
def gameOver():
    global snake, food, snake_body, velocityX, velocityY, score, GameOver
    # Ask the player if they want to try again or not
    response = messagebox.askyesno("Game Over", f"Game Over! Your Score: {score}\nDo you want to try again?")
    if response: 
         # "Yes" clicked
        # Reset the game
        snake = Tile(5 * tile_size, 5 * tile_size)
        food = Tile(10 * tile_size, 10 * tile_size)
        velocityX = 0
        velocityY = 0
        snake_body = []
        score = 0
        GameOver = False
        start_time = time.time()  # Restart the timer
        draw()  # Restart the drawing loop
    else:  # "No" clicked
        # Show the Game Over message and wait for a few seconds before closing
        canvas.create_text(width / 2, height / 2, font="Arial 40", text=f"GAME OVER   {score}", fill="lime green")
        window.after(2000, window.quit)  # Wait 2 seconds before closing the game

# Draw the game elements
def draw():
    global snake, food, snake_body, GameOver, score, start_time
    canvas.delete("all")
    move()

    # Draw the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + tile_size, snake.y + tile_size, fill='lime green')

    # Draw the food
    canvas.create_rectangle(food.x, food.y, food.x + tile_size, food.y + tile_size, fill='red')

    # Draw the snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + tile_size, tile.y + tile_size, fill="lime green")

   
    elapsed_time = int(time.time() - start_time)
    canvas.create_text(200, 30, font="Arial 20", text=f"Time: {elapsed_time}s", fill="white")

    # Show score
    if GameOver:
        canvas.create_text(width / 2, height / 2, font="Arial 40", text=f"GAME OVER   {score}", fill="lime green")
    else:
        canvas.create_text(55, 30, font="Arial 20", text=f"Score: {score}", fill="white")

    window.after(speed, draw)

# Bind key press event
window.bind("<KeyPress>", changeDirection)
draw()
window.mainloop()
