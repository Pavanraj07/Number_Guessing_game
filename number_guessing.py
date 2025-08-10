import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        number_guessing_game()
    else:
        print("Thanks for playing! 👋")

if __name__ == "__main__":
    number_guessing_game()
