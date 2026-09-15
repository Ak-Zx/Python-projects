import random
def play_game():
    print("Welcome to Number Guessing Game😎")
    print("Select Difficulty Level")
    print("1.Easy , 1-50 , 10 attempts")
    print("2.Medium , 1-100, 7 attempts")
    print("3.Hard , 1-500 , 5 attempts")
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
        except ValueError:
            print("❌ Invalid input! Enter 1, 2, or 3.")
            continue
        if choice == 1:
            max_attempts = 10
            max_range = 50
            break
        if choice == 2:
            max_attempts = 7
            max_range = 100
            break
        if choice == 3:
            max_attempts = 5
            max_range = 500
            break
        else:
            print("Invalid choice Enter the valid choice 1/2/3!!")
    secret_number = random.randint(1,max_range)
    attempts = 0
    print(f"Guess the Number Between 1 and {max_range}")
    print(f"You have {max_attempts} attemptsko to guess the Number")
    while attempts < max_attempts:
        try:
            user_input = int(input("Enter your guess: "))
        except ValueError:
            print("**Invalid input !!,Please enter valid Number**")
            continue
        if user_input < 1 or user_input > max_range:
            print(f"*** Enter the Number Between 1 - {max_range} ***")
            continue
        attempts += 1
        if user_input == secret_number:
            print(f"Congratulations, You have Guessed the number in {attempts} attempts")
            return
        elif user_input > secret_number:
            print("Too High !!")
        else:
            print("Too Low !!")
        print(f"Attempts Left: {max_attempts - attempts}")
    print(f"Game Over, The Correct Number was {secret_number}")
while True:
    play_game()
    again = input("Play again? (yes/no): ").lower()
    if again != 'yes':
        break