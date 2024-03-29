import random

# Function to get the user's choice for a given player
def get_user_choice(player):
    user_choice = input(f"Player {player}, enter Rock, Paper, or Scissors: ").capitalize()
    
    # Validate user input
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input(f"Player {player}, enter Rock, Paper, or Scissors: ").capitalize()
    
    return user_choice

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to determine the winner between two players or a player and the computer
def determine_winner(player1_choice, player2_choice=None):
    if player2_choice:
        # For two players
        if player1_choice == player2_choice:
            return "It's a tie!"
        elif (player1_choice == "Rock" and player2_choice == "Scissors") or \
             (player1_choice == "Paper" and player2_choice == "Rock") or \
             (player1_choice == "Scissors" and player2_choice == "Paper"):
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    else:
        # For single player against the computer
        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}.")
        if player1_choice == computer_choice:
            return "It's a tie!"
        elif (player1_choice == "Rock" and computer_choice == "Scissors") or \
             (player1_choice == "Paper" and computer_choice == "Rock") or \
             (player1_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        else:
            return "Computer wins!"

# Function to play the single-player version of the game
def play_single_player():
    while True:
        print("\nWelcome to Rock, Paper, Scissors (Single Player)!\n")
        user_choice = get_user_choice(1)
        result = determine_winner(user_choice)
        print(result)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

# Function to play the double-player version of the game
def play_double_player():
    while True:
        print("\nWelcome to Rock, Paper, Scissors (Double Player)!\n")
        print("Player 1's turn:")
        player1_choice = get_user_choice(1)
        print("Player 2's turn:")
        player2_choice = get_user_choice(2)
        result = determine_winner(player1_choice, player2_choice)
        print(result)

        # Ask if the players want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

# Main section to choose the game mode and initiate the game
if __name__ == "__main__":
    mode = input("\nChoose game mode (1 for Single Player, 2 for Double Player): ")
    if mode == "1":
        play_single_player()
    elif mode == "2":
        play_double_player()
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
