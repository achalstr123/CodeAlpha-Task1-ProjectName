#=====================Hangman Game=============
import random
words = ["python", "computer", "programming", "hangman", "developer"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
display = ["_"] * len(word)

print(" Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_wrong_guesses - wrong_guesses}")
if "_" not in display:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The word was:", word)
