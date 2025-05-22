import random

#list of words
words = ["apple", "house", "robot", "plane", "chair"]

# Randomly select a word from the list
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)
guessed_letters = []
max_attempts = 6
attempts = 0

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_attempts, "incorrect guesses allowed.")
print(" ".join(guessed_word))

while attempts < max_attempts and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        attempts += 1
        print("Wrong guess. Attempts left:", max_attempts - attempts)

    print(" ".join(guessed_word))

# Final result
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)
