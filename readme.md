
---

# Ping-Pong Game

## Overview

This is a simple implementation of the classic Pong game using the `turtle` graphics module in Python. The game involves two paddles controlled by the player to bounce a ball back and forth across the screen. The first player to score 10 points wins the game.

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone this repository or download the source code files to your local machine.

3. Make sure you have the `turtle` module. It comes pre-installed with Python, but you can verify by running:
    ```bash
    pip install PythonTurtle
    ```

## Files

- `main_screen.py`: Contains the `MainScreen` class that sets up the game screen and controls.
- `paddle.py`: Contains the `Paddle` class which represents the paddles used by the players.
- `ball.py`: Contains the `Ball` class which represents the ball in the game.
- `scoreboard.py`: Contains the `ScoreBoard` class which handles displaying the score.
- `controls.py`: Contains the `Controls` class which manages the movement of the paddles.

## Running the Game

1. Navigate to the directory containing the game files.

2. Run the main game script:
    ```bash
    python main_game.py
    ```

## How to Play

- **Left Paddle Controls**:
  - Move Up: `W`
  - Move Down: `S`

- **Right Paddle Controls**:
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`

The game starts with the ball in the center of the screen. Use the paddle controls to move the paddles up and down to bounce the ball back and forth. If the ball passes a paddle and reaches the edge of the screen, the opposing player scores a point. The game continues until one player reaches a score of 10.

## Code Explanation

### Main Components

1. **Ball**:
    - `Ball` class inherits from `Turtle` and represents the ball in the game.
    - It has methods to reset its position, move, and handle collisions with walls and paddles.

2. **Paddle**:
    - `Paddle` class inherits from `Turtle` and represents a paddle.
    - It has methods to reset its position.

3. **ScoreBoard**:
    - `ScoreBoard` class inherits from `Turtle` and handles displaying the scores.

4. **Controls**:
    - `Controls` class manages the movement of the paddles based on the screen height.

5. **MainScreen**:
    - `MainScreen` class sets up the game window, draws the centerline, and handles paddle controls.

### Game Loop

The game loop is controlled by a `while` loop that checks if either paddle has reached a score of 10. The ball continuously moves and bounces off the walls and paddles until it goes out of bounds, at which point the score is updated, and the ball and paddles are reset.

## Customization

You can customize various aspects of the game such as:

- **Ball Speed**: Modify the `self.forward(5)` line in the `move` method of the `Ball` class to change the ball's speed.
- **Paddle Speed**: Modify the values in the `up` and `down` methods of the `Controls` class to change the paddle movement speed.
- **Score Limit**: Change the `10` in the `while` loop condition to set a different score limit for winning the game.

## License

This project is licensed under the MIT License.

---

Feel free to reach out if you have any questions or need further assistance! Enjoy the game!