import random

# Function to get the user's choice
def get_user_choice():
    user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()

    # Validate user input
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()

    return user_choice

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to determine the winner between the user and the computer
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    while True:
        print("\nWelcome to Rock, Paper, Scissors!\n")

        # Get choices from user and computer
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}.")
        print(f"Computer chose {computer_choice}.\n")

        # Determine and print the result
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

# Main section to initiate the game
if __name__ == "__main__":
    play_game()
