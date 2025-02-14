# FlappyBird
This project is a Flappy Bird Clone built using Python and Pygame. It replicates the core mechanics of the famous mobile game where the player controls a bird that must navigate through pipes without hitting them. The bird continuously falls due to gravity, and the player must click to make the bird "flap" and stay afloat while avoiding obstacles.

Features:
Gravity Mechanics: The bird falls due to gravity and flaps upward when the player clicks the mouse or presses a key.
Obstacle Pipes: Pipes move horizontally across the screen, and the player must navigate the bird through gaps in the pipes.
Score Tracking: Every time the bird successfully passes through a set of pipes, the score increases.
Game Over: If the bird hits a pipe or the ground, the game ends.
High Score: Track and display the highest score achieved in the game.
Sound Effects: Add sounds for flapping, collisions, and game over.

How to Play:
Click the mouse or press any key to make the bird flap and stay afloat.
Avoid hitting the pipes or the ground.
Try to survive as long as possible and aim to beat your high score!

Technologies Used in the Flappy Bird Clone:
Python 3.x:

The primary programming language used to create the game logic, mechanics, and flow.
Python is great for rapid prototyping and simplicity, making it a solid choice for game development.
Pygame:

A set of Python modules used for writing video games.
Provides functionalities for handling game graphics, user input (keyboard, mouse), sound, and animations.
In this project, Pygame is used for:
Drawing objects like the bird, pipes, and background.
Managing game events (e.g., key presses).
Handling the game loop (updating the screen and logic).
Implementing collision detection between the bird and pipes.
Game Design Concepts:

Gravity & Physics: The game uses basic physics principles for gravity and the bird's flapping motion.
Collision Detection: Simple bounding box collision detection is used to check if the bird collides with the pipes or the ground.
Graphics:

Basic 2D shapes (using pygame.Surface() and pygame.draw.rect()) are used to represent the bird, pipes, and background.
Simple, retro-style graphics for quick development and easy customization.
User Input Handling:

Keyboard events (pygame.KEYDOWN) are used to make the bird "flap" when the spacebar is pressed.
The player interacts with the game by pressing a key or restarting the game using the keyboard.
Score Tracking:

The score is tracked by counting how many pipes the bird successfully passes. The score is displayed in real-time using Pygame’s text rendering (pygame.font.SysFont()).


