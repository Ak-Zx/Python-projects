import random


def play_game():

    print("Welcome to Number Guessing Game 😎")
    print("Select Difficulty Level")
    print("1. Easy   - 1 to 50   - 10 attempts")
    print("2. Medium - 1 to 100  - 7 attempts")
    print("3. Hard   - 1 to 500  - 5 attempts")

    # Select difficulty
    while True:

        try:
            choice = int(input("Enter your choice (1/2/3): "))

        except ValueError:
            print("❌ Invalid input! Enter 1, 2, or 3.")
            continue

        if choice == 1:
            max_range = 50
            max_attempts = 10
            break

        elif choice == 2:
            max_range = 100
            max_attempts = 7
            break

        elif choice == 3:
            max_range = 500
            max_attempts = 5
            break

        else:
            print("❌ Invalid choice! Enter 1, 2, or 3.")

    # Generate random number
    secret_number = random.randint(1, max_range)

    attempts = 0

    print(f"\nGuess the number between 1 and {max_range}")
    print(f"You have {max_attempts} attempts to guess the number.")

    # Guessing loop
    while attempts < max_attempts:

        try:
            user_input = int(input("Enter your guess: "))

        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        # Check range
        if user_input < 1 or user_input > max_range:
            print(f"❌ Enter a number between 1 and {max_range}.")
            continue

        attempts += 1

        # Check guess
        if user_input == secret_number:
            print(
                f"🎉 Congratulations! You guessed the number "
                f"in {attempts} attempts!"
            )
            return

        elif user_input > secret_number:
            print("📈 Too High!")

        else:
            print("📉 Too Low!")

        print(f"Attempts left: {max_attempts - attempts}")

    print(f"\n💀 Game Over! The correct number was {secret_number}.")


# Play again
while True:

    play_game()

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing! 👋")
        break