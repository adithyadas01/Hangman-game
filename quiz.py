
import random

# List of words
words = ["python", "eclipse", "brainhunt", "codenova", "phoenix"]

# Choose a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("\n🎮 Welcome to the Hangman Game! 🎮")
print("I'm thinking of a word...")
print(" ".join(guessed))
print(f"You have {attempts} attempts.\n")

while attempts > 0 and "_" in guessed:
    guess = input("👉 Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}\n")

    print("Word:", " ".join(guessed))
    print("Guessed letters:", ", ".join(guessed_letters), "\n")

if "_" not in guessed:
    print(f"🎉 You win! The word was '{word}'. Great job!")
else:
    print(f"💀 You lose! The word was '{word}'. Better luck next time!")
