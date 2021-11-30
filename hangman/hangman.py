import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # memilih secara acak kata di dalam list
    while '-' in word or '' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # huruf di dalam kata
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # yang musti di tebak user

    nyawa = 7

    # input user
    while len(word_letters) > 0 and nyawa > 0:
        # huruf yang di pakai
        # ' '.join(['a', 'b', 'cd']) adalah 'a b cd'
        print('you have', nyawa, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # memberi tahu pengguna kata saat ini (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('kata saat ini: ', ' '.join(word_list))


        user_letter = input('tebak huruf: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                nyawa = nyawa - 1 # take away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word')

        elif user_letter in used_letters:
            print('\nyou have already used that letter. guess another letter')

        else:
            print('\nthat is not a valid letter')

hangman()