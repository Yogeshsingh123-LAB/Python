import random
print("Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!") 
    else:        
        print("Computer wins!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        else:
            computer_choice = random.choice(choices)
