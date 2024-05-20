# Gomoku AI Project

## Author
Zhihang Cheng

## Overview
This Gomoku AI project implements a basic AI opponent for the traditional board game Gomoku, where the objective is to align five stones in a row. The AI is designed to play with a "regular" level of intelligence, making it capable of challenging beginners but not professional players.

## Features
- **AI Intelligence**: The AI can effectively block simple threats like four consecutive stones (e.g., BBBB) but struggles with more complex setups (e.g., BB_B).
- **Evaluation System**: The AI evaluates potential moves based on the immediate threat or opportunity, prioritizing blocking or extending sequences of black stones.
- **Dynamic Interaction**: Players interact with the AI in real-time, with the AI responding to the player's moves based on a set evaluation system.

## Technologies Used
- **Python**: Main programming language used for the AI logic and game mechanics.
- **Processing**: Used for rendering the game board and handling user interaction within a graphical interface.

## AI Strategy
The AI follows a simple yet effective strategy to decide its next move:
1. **Move Evaluation**: Scans the board for the best move by temporarily placing a stone in each possible position and evaluating the move's impact based on a predefined scoring system.
2. **Scoring System**: Scores are assigned based on potential threats or opportunities (e.g., blocking or completing a row of stones).
3. **Decision Making**: After evaluating all possible moves, the AI places a stone in the position with the highest score.

## How to Run the Project
To run this project, you will need to have Python and Processing installed on your machine. Once installed, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the Processing sketch to start the game interface.

## Future Improvements
- **Enhanced AI Intelligence**: Incorporating more complex strategies and recognition of patterns beyond simple linear threats.
- **Adjustable Difficulty Levels**: Allowing users to set the difficulty level of the AI to match their skill level.
- **GUI Enhancements**: Improving the graphical user interface for a better user experience.

## Conclusion
This project serves as a foundation for a simple yet interactive Gomoku game. It demonstrates basic AI implementation and provides a platform for further enhancement and integration of more sophisticated AI algorithms.
