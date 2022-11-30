from words import words
import random
from visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 

    lives = 7

    
    while len(word_letters) > 0 and lives > 0:
       
        print('Tienes ', lives, 'vidas restantes: ', ' '.join(used_letters))

       
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('palabra actual: ', ' '.join(word_list))

        user_letter = input('Ingresa una letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  
                print('\nLa letra seleccionada,', user_letter, 'no esta dentro de la palabra.')

        elif user_letter in used_letters:
            print('\nYa se menciono esa letra. Intenta con otra letra.')

        else:
            print('\nLa letra no es parte de la palabra.')

    
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Perdiste', word)
    else:
        print('Felicidades, encontraste la palabra', word, '!!')


if __name__ == '__main__':
    hangman()
