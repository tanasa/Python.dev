#!/usr/bin/env python
# coding: utf-8

import random
import sys

def generateSecretNumber():
    """
    Generates a secret number as a 3-digit string with unique digits.
    """
    return ''.join(random.sample('123456789', 3))

def playerGuess():
    """
    Prompts and validates the player's guess ensuring it is a 3-digit number 
    with unique digits and does not start with '0'.
    """
    
    while True:
        guess = input("What is my 3-digit number? ")

        if not guess.isdigit() or len(guess) != 3:
            print("Invalid guess. Try again.")
            continue

        if len(set(guess)) != 3:
            print("Invalid guess. Try again.")
            continue
        
        if guess[0] == '0':
            print("Invalid guess. Try again.")
            continue

        return guess

def compareSecretGuess(secret, guess):
    """
    Compares the guess with the secret number and returns a hint.
    
    - "Fermi": A digit is correct and in the correct position.
    - "Pico": A digit is correct but in the wrong position.
    - "Bagels": No digit is correct.
    """
    
    result = []
   
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result.append("Fermi")
        elif guess[i] in secret:
            result.append("Pico")
            
    if not result:
        return "Bagels"
    else:
        return " ".join(result)

if __name__ == "__main__":
    
    print("Instructions:")
    print("Bagels: no digit is correct.")
    print("Pico: one digit is correct but in the wrong position.")
    print("Fermi: one digit is correct and in the correct position.")

    secret = generateSecretNumber()
    # For testing with a fixed secret, use :
    # secret = "410"  
    
    attempts = 10

    while attempts > 0:

        print(f"\nYou have {attempts} attempts to guess my 3-digit number.")
        guess = playerGuess()
        
        if guess == secret:
            print(f"Congratulations! You have guessed the secret number {secret}.")
            sys.exit()
        else:
            comparison = compareSecretGuess(secret, guess)
            print(comparison)
            
        attempts -= 1

    print(f"Unfortunately, You lost this game. The secret number was {secret}.")
    print("Please play again. Next time, you will be the winner.")


