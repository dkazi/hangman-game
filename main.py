import random

words = (
    "apple", "banana", "orange", "grape", "mango", "peach", "cherry", "lemon", "lime", "kiwi",
    "watermelon", "strawberry", "blueberry", "raspberry", "pineapple", "coconut", "apricot", "plum", "pear", "fig",
    "dog", "cat", "rabbit", "elephant", "tiger", "lion", "giraffe", "zebra", "monkey", "panda",
    "whale", "dolphin", "shark", "octopus", "penguin", "kangaroo", "fox", "wolf", "bear", "deer",
    "car", "train", "plane", "bicycle", "motorbike", "boat", "ship", "submarine", "helicopter", "scooter",
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white",
    "table", "chair", "sofa", "bed", "desk", "lamp", "shelf", "mirror", "door", "window",
    "guitar", "piano", "violin", "drum", "flute", "trumpet", "saxophone", "cello", "harp", "keyboard",
    "soccer", "basketball", "tennis", "cricket", "baseball", "volleyball", "hockey", "swimming", "running", "cycling",
    "castle", "dragon", "wizard", "knight", "princess", "forest", "mountain", "river", "ocean", "island",
    "python", "java", "ruby", "javascript", "html", "css", "react", "angular", "swift", "kotlin"
)


def print_hint(hint):
    print(" ".join(hint))

def print_answer(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guesses_letters = set()

    is_running = True


    while is_running:
        print(f"You have {6-wrong_guesses} lives remaining.")
        print_hint(hint)

        guess = input("Enter a letter: ").lower()
        if len(guess) > 1 or not guess.isalpha():
            print("Wrong input.")
            continue
        elif guess in guesses_letters:
            print("You have already guessed this letter.")
            continue



        if guess in answer:
            for i, ch in enumerate(answer):
                if ch == guess:
                    hint[i] = guess

        else:
            print(f"There is not {guess} in the answer.")
            if guess not in guesses_letters:
                wrong_guesses += 1

        guesses_letters.add(guess)

        if "_" not in hint:
            print_answer(answer)
            print("You Won!")
            is_running = False
        elif wrong_guesses == 6:
            print("You lost. The answer is: ")
            print_answer(answer)
            is_running = False



if __name__ == "__main__":
    main()