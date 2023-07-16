print ("Welcome to the word guessing game!")

import random

secret_words = ['nephi', 'lehi', 'alma', 'moroni', 'helaman', 'mosiah','programmer','byu','pathwayconnect', 'bookofmormon']

secret_word = random.choice(secret_words)

secret_word = secret_word.lower()

word_in_progress = ['_'] * len(secret_word)

num_guesses = 0

while True:
    print(f'\nYour hint is: {" ".join(word_in_progress)}')
    guess = input('What is your guess? ').lower()

    if len(guess) != len(secret_word):
        print('Sorry, the guess must have the same number of letters as the secret word.')
        num_guesses += 1
        continue

    num_guesses += 1

    if guess == secret_word:
        print('Congratulations! You guessed it!')
        print(f'It took you {num_guesses} guesses.')
        break

    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())
        elif guess[i] in secret_word:
            hint.append(guess[i])
        else:
            hint.append('_')
    print(f'Your hint is: {" ".join(hint)}')
    
    
    
    
    
    
   