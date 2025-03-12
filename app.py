import random

def get_computer_choice():
    return random.choice([1, 2, 3])

def get_user_choice():
    choice = input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors, q to quit): ").lower()
    while choice not in ['1', '2', '3', 'q']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors, q to quit): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == '1' and computer_choice == 3) or \
         (user_choice == '2' and computer_choice == 1) or \
         (user_choice == '3' and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    rounds = 0
    user_wins = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            break
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, str(computer_choice))
        print(result)

        rounds += 1
        if result == "You win!":
            user_wins += 1

    print(f"Game over! You won {user_wins} out of {rounds} rounds.")

if __name__ == "__main__":
    main()
