import random
from hangmanart import *
from hangmanwords import *


def startgame():
    # Begin game
    chosen_word = random.choice(word_list).upper()
    display = []
    letters_chosen = []
    guesses = 7
    game = True
    print(f"\nWelcome to {hangword}\n")

    # Display word blanks
    for letter in chosen_word:
        display += "_"
    print(f"Your word: {' '.join(display)}")

    while game is True:

        guess = input("\nGuess a letter: ").upper()
        print("------------------------------------------------------")
        # Wrong guess
        if guess not in chosen_word:
            guesses -= 1
            letters_chosen += guess
            # No more lives - GAME OVER
            if guesses == 0 and "_" in display:
                print(f"\nYour word: {' '.join(display)}\n{hang[6]}\n\nYou lose.\n\nThe solution is: {chosen_word}.")
                playagain()
            # Still has lives
            else:
                print(f"\nYour word: {' '.join(display)}\n{hang[7 - guesses]}\n\nIncorrect letter! {guess} is not in this word - try again!")
                print(f"\nGuesses left: {guesses}\t\tIncorrect Letters: {' '.join(letters_chosen)}")
        # Correct guess
        else:
            # Already guessed that letter
            if guess in display:
                print(f"\nYour word: {' '.join(display)}\n{hang[7 - guesses]}\n\nYou already guessed {guess} - try again!")
                print(f"\nGuesses left: {guesses}\t\tIncorrect Letters: {' '.join(letters_chosen)}")
            # New correct guess
            else:
                for x in range(0, len(chosen_word)):
                    if guess == chosen_word[x] and display[x] == "_":
                        display[x] = f"{guess}"
                print(f"\nYour word: {' '.join(display)}\n{hang[7 - guesses]}\n\nCorrect!")
                print(f"\nGuesses left: {guesses}\t\tIncorrect Letters: {' '.join(letters_chosen)}")
                # All letters filled in now - YOU WIN
                if "_" not in display:
                    print(f"\nYour word: {' '.join(display)}\n{hang[7 - guesses]}\n\nYou win!\n\nThe solution is: {chosen_word}.")
                    playagain()


def playagain():
	question = input("\nPlay again? ").lower()

	questionyes = ["yes", "y"]
	questionno = ["no", "n"]
	
	if any(match in question for match in questionyes):
		startgame()
	elif any(match in question for match in questionno):
		exit()
	else:
		print("\nIncorrect response - try again!")
		playagain()


startgame()