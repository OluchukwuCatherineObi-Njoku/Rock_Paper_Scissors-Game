# Single Player Rock, Paper, Scissors Game

## Overview
This is a simple console-based Rock, Paper, Scissors game implemented in Python. It allows a single player to play against the computer.

## How to Play
1. Run the Python script.
2. The game will prompt you to enter your choice (Rock, Paper, or Scissors).
3. The computer will randomly choose its option.
4. The game will determine the winner based on the choices made.
5. The result will be displayed on the console.

## Code Structure
- `get_user_choice()`: Takes user input for their choice and validates it.
- `get_computer_choice()`: Generates a random choice for the computer.
- `determine_winner(user_choice, computer_choice)`: Determines the winner based on the user's choice and the computer's choice.
- `play_game()`: Main function to initiate and play the game.

# Double Player Rock, Paper, Scissors Game

## Overview
This is an extended version of the Rock, Paper, Scissors game that allows either a single player to play against the computer or two players to take turns playing against each other.

## How to Play
1. Run the Python script.
2. Choose the game mode (1 for Single Player, 2 for Double Player).
   - In Single Player mode, you play against the computer.
   - In Double Player mode, two players take turns making choices.
3. Follow the prompts to enter choices.
4. The game will determine the winner based on the choices made.
5. The result will be displayed on the console.

## Code Structure
- `get_user_choice()`: Takes user input for their choice and validates it.
- `get_computer_choice()`: Generates a random choice for the computer.
- `determine_winner(player1_choice, player2_choice)`: Determines the winner between two players.
- `play_single_player()`: Initiates the single-player game.
- `play_double_player()`: Initiates the double-player game, allowing two players to take turns.
- `main()`: Allows the user to choose the game mode and initiates the respective game.
