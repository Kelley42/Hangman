import random
from hangmanart import *
from hangmanwords import *

# Randomly choose word
chosen_word = random.choice(word_list)
display = []
letters_chosen = []
blank = "_"
guesses = 7

# Defs
def game():
    global chosen_word, display, guesses, blank, letters_chosen
    # Begin game
    chosen_word = random.choice(word_list)
    display = []
    letters_chosen = []
    blank = "_"
    guesses = 7
    print(f"\nWelcome to {hangword}\n")

    # Display word blanks
    for letter in chosen_word:
        display += blank
    print(f"Your word: {' '.join(display)}")

    guessgame()

    
def guessgame():
    global display, chosen_word, blank, guesses
    # If user lost all turns
    if guesses == 0 and blank in display:
        print(f"\nYour word: {' '.join(display)}")
        print(f"\n{hang[6]}")
        print("\nYou lose.")
        print(f"\nThe solution is {chosen_word}.")
        playagain()
        
    # User guesses letter
    while guesses > 0:
        # If there are still blanks
        if blank in display:
            repeat_guess()
        # If all letters were guessed correctly
        else:
            print(f"\nYour word: {' '.join(display)}")
            print(f"\n{hang[7 - guesses]}")
            print("\nYou win!")
            print(f"\nThe solution is {chosen_word}.")
            playagain()


def repeat_guess():
    global chosen_word, guesses, printdisplay, letters_chosen
    guess = input("\nGuess a letter: ").lower()
    
    if guess not in chosen_word:
        guesses -= 1
        if guesses == 0 and blank in display:
            guessgame()
        else:
            letters_chosen += guess
            print(f"\nYour word: {' '.join(display)}")
            print(f"\n{hang[7 - guesses]}")
            print(f"\nIncorrect letter! {guess} is not in this word - try again!")
            print(f"\nGuesses left: {guesses}")
            print(f"\nIncorrect Letters: {' '.join(letters_chosen)}")
            guessgame()
    else:
        if guess in display:
            print(f"\nYour word: {' '.join(display)}")
            print(f"\n{hang[7 - guesses]}")
            print(f"\nYou already guessed {guess} - try again!")
        else:
            for x in range(0, len(chosen_word)):
                if guess == chosen_word[x] and display[x] == "_":
                    display[x] = f"{guess}"
            print(f"\n{' '.join(display)}")
            print(f"\n{hang[7 - guesses]}")
            print("\nCorrect!")
    guessgame()


def playagain():
	question = input("\nPlay again? ").lower()

	questionyes = ["yes", "y"]
	questionno = ["no", "n"]
	
	if any(match in question for match in questionyes):
		game()
	elif any(match in question for match in questionno):
		exit()
	else:
		print("\nIncorrect response - try again!")
		playagain()


game()