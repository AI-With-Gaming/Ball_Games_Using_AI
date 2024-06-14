# Physics Ball Simulation

This project is a simple physics ball simulation game using Pygame. The simulation includes a ball that moves and bounces off the boundaries of the window and a central circle, grows in size, changes color upon collisions, and is influenced by gravity.

## Features

- **Ball Movement:** The ball moves with a random initial velocity and is affected by gravity.
- **Collisions:** The ball bounces off the bottom of the window and the boundary of a central circle.
- **Growth and Color Change:** The ball grows and changes color upon each collision with the central circle.
- **Game Over:** The game ends when the ball's radius fills the central circle.
- **Background Animation:** The background consists of a smooth transition between frames of an animated GIF.
- **Trail Effect:** The ball leaves a fading trail as it moves.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install Pygame by running:
    ```sh
    pip install pygame
    ```

## Usage

1. Clone the repository or download the source code.
2. Ensure you have 5 frames of the background animation saved as `hacker_background_frame1.png.gif`, `hacker_background_frame2.png.gif`, ..., `hacker_background_frame5.png.gif` in the same directory as the script.
3. Run the script:
    ```sh
    python Bounce.py
    ```

## Code Overview

### Constants

- `WIDTH, HEIGHT`: Dimensions of the window.
- `FPS`: Frames per second.
- `GROWTH_RATE`: Rate at which the ball grows.
- `BALL_INITIAL_RADIUS`: Initial radius of the ball.
- `CIRCLE_RADIUS`: Radius of the central circle.
- `SPEED_INCREASE`: Speed increase upon collision.
- `GRAVITY`: Gravity constant.
- `ELASTICITY`: Elasticity for bounce.
- `COLORS`: List of colors for the ball.

### Classes

- `Ball`: Represents the ball with methods to move, handle collisions, and draw itself.

### Main Game Loop

- Initializes Pygame and sets up the display.
- Loads background frames and scales them.
- Creates a ball instance.
- Runs the game loop to handle events, update ball movement, check for game over, draw elements, and manage background transitions.

### Game Over

- Displays a "Game Over" message when the ball's radius fills the central circle.
- The message has a sinusoidal scaling animation.

Enjoy the simulation and have fun experimenting with the physics!
