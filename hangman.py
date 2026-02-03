import random

print("WELCOME TO HANGMAN GAME")

# Level data (simple and readable)
easy_words = [
    ("mouse", "Computer input device"),
    ("file", "Stores data"),
    ("code", "Set of instructions")
]

medium_words = [
    ("python", "Programming language"),
    ("network", "Connected computers"),
    ("database", "Structured data storage")
]

hard_words = [
    ("algorithm", "Step by step solution"),
    ("encryption", "Securing information"),
    ("virtualization", "Creating virtual systems")
]


print("\nSelect Level")
print("1 - Easy")
print("2 - Medium")
print("3 - Hard")

level = input("Enter your choice: ")

# Choose word based on level
if level == "1":
    word, hint = random.choice(easy_words)
    print("\nEasy level selected")
elif level == "2":
    word, hint = random.choice(medium_words)
    print("\nMedium level selected")
else:
    word, hint = random.choice(hard_words)
    print("\nHard level selected")

attempts = 6
score = 0
used_hint = False
guessed = []

print("\nWord:")
print("_ " * len(word))

# Main game loop
while attempts > 0:
    print("\n1 - Guess letter")
    print("2 - Get hint")

    option = input("Choose option: ")

    if option == "2":
        if used_hint == False:
            print("Hint:", hint)
            used_hint = True
            score = score - 2
        else:
            print("Hint already used")
        continue

    letter = input("Enter a letter: ").lower()

    if letter in guessed:
        print("You already guessed this letter")
        continue

    guessed.append(letter)

    if letter in word:
        print("Correct letter")
        score = score + 5
    else:
        print("Wrong letter")
        attempts = attempts - 1
        score = score - 1

    # Show current word status
    current_word = ""
    for ch in word:
        if ch in guessed:
            current_word = current_word + ch + " "
        else:
            current_word = current_word + "_ "

    print("\n", current_word)
    print("Attempts left:", attempts)

    # Check win
    if "_" not in current_word:
        print("\nYou guessed the word correctly!")
        score = score + 10
        break

# Lose condition
if attempts == 0:
    print("\nGame Over")
    print("Correct word was:", word)

print("\nFinal Score:", score)
