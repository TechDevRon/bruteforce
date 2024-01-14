#length of chars is 93
chars = 'abcdefghijklmnopqrstuvwxyzACDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>/?\'"`~ ' #i know this space is here
import random as r
import time as t
import itertools
import sys
def brutef(pw):
  attempts = 0
  guess = ''
  while True:
    for length in range(1, len(pw) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
#if you don't want to print guess charecters coment "print(guess)" out
            print(guess)
            if guess == pw:
              print('____________________________________')
              print(' ')
              print(f'After {attempts} attemps, password guessed is: {guess}')
              exit()
pw = input('input password> ')
brutef(pw)
