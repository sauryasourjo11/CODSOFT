import random

# Define choices
choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():
    user_score = 0
    computer_score = 0
    while True:
        # Get user input
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue
        
        # Get computer choice
        computer_choice = get_computer_choice()
        
        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Display result
        display_result(user_choice, computer_choice, winner)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        # Display scores
        print(f"\nScores:\nYou: {user_score}\nComputer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you
