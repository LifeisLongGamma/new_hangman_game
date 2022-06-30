import random
from word_list import words
import string

def get_word(words):
    random.shuffle(words)
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed
    lives = 5

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives remaining', '\nYou have used these letters: ', ' '.join(used_letters))
        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print('You have already used this letter. Please try again!')
        else:
            print('Input error. Please try again!')

    if lives == 0:
        print(f'You have died! Hidden word was {word}')
    else:
        print(f'Congratulations! You have guessed word {word}')

hangman()


