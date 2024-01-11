import random

def get_user_choice():
    user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
    return user_choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(player1_choice, player2_choice=None):
    if player2_choice:
        if player1_choice == player2_choice:
            return "It's a tie!"
        elif (player1_choice == "Rock" and player2_choice == "Scissors") or \
             (player1_choice == "Paper" and player2_choice == "Rock") or \
             (player1_choice == "Scissors" and player2_choice == "Paper"):
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    else:
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

def play_single_player():
    print("Welcome to Rock, Paper, Scissors (Single Player)!")
    user_choice = get_user_choice()
    result = determine_winner(user_choice)
    print(result)

def play_double_player():
    print("Welcome to Rock, Paper, Scissors (Double Player)!")
    print("Player 1's turn:")
    player1_choice = get_user_choice()
    print("Player 2's turn:")
    player2_choice = get_user_choice()
    result = determine_winner(player1_choice, player2_choice)
    print(result)

if __name__ == "__main__":
    mode = input("Choose game mode (1 for Single Player, 2 for Double Player): ")
    if mode == "1":
        play_single_player()
    elif mode == "2":
        play_double_player()
    else:
        print("Invalid choice. Please enter 1 or 2.")
