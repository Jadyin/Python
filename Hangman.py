import random
from wordlist import words
import string

print("Yes I work")

def valid_word(wordle):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word




def hangman():
    word = valid_word(words)
    word_set = set(word)
    alphabet = set(string.ascii_lowercase)
    already_used_letters = set()

    lives = 10

    while len(word_set) > 0 and lives != 0:
        print("You've used have these letters:","".join(already_used_letters))
        print("You have", lives, "lives left")

        word_list = [letter if letter in already_used_letters else "-" for letter in word]
        print("Current word:","".join(word_list))

        user_guess = input("Guees a Letter! \n").lower()
        if user_guess in alphabet - already_used_letters:
            already_used_letters.add(user_guess)
            if user_guess in word_set:
                word_set.remove(user_guess)
            else:
                lives -= 1
                print("Letter isn't in word")

        elif user_guess in already_used_letters:
            print("Letter has already been guessed")
        else:
            print("Error: Invalid Guess")
            
    if lives == 0:
        print("Sorry you were hung, Better luck next time \nThe word was:", word)
    else:
        print("Congrats you won the word was:", word,"!!\n")

hangman()



