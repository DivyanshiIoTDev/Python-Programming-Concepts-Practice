# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:49:12 2025

@author: bishe
"""
#WORD GUESSING GAME
import random
name=input("Enter your name")
print(f"Good Luck!{name}")
words=["programming","geeks","happy","good","enjoy","fun"]
word=random.choice(words)
guesses=''
turns=12
while turns>=0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            failed+=1
            print("_",end=" ")
    if failed==0:
        print("You guessed it right")
    print("Enter the next charachter")
    guess=char(input("Enter the next charachter"))
    guesses+=guess
    
    if guesses not in word:
        turns-=1
        print("Number of turns left"+turns)
        if turns==0:
            print("You lost")
            
        