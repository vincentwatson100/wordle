import random


print('welcome to your wordle file.you have 6 guesses to guess a five letter word.')
guess=input('please enter a five letter word: ')

word_list = ['fizzy', 'crazy', 'apple', 'berry', 'black', 'white', 'cozey', 'alone', 'along', 'alert', 'alike', 'allow', 'alter', 'exist', 'extragoing', 'hence', 'globe', 'final', 'first', 'fixed', 'loose', 'logic', 'quiet', 'speak', 'spare', 'grape', 'peach']

chosen_word = random.choice(word_list)
print(chosen_word)
