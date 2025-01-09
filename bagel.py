import random
"""
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
Guess #1:
> 123
Pico
Guess #2:
> 456
Bagels
Guess #3:
> 178
Pico Pico
--snip--
Guess #7:
> 791
Fermi Fermi
Guess #8:
> 701
You got it!
Do you want to play again? (yes or no)
> no
Thanks for playing!
"""

"""
Bagels, a deductive logic game.
 16. By Al Sweigart al@inventwithpython.com
 17. 
 18. I am thinking of a {}-digit number with no repeated digits.
 19. Try to guess what it is. Here are some clues:
 20. When I say:    That means:
 21.   Pico         One digit is correct but in the wrong position.
 22.   Fermi        One digit is correct and in the right position.
 23.   Bagels       No digit is correct.
 24. 
 25. For example, if the secret number was 248 and your guess was 843, the
 26. clues would be Fermi Pico.

"""

maxNumberOfGuesses = 3
numberOfDigits = 2

def bagel_game(): 
    print('''
          Bagels, a deductive logic game.
          I am thinking of a {}-digit number with no repeated digits. 
          Try to guess what it is. Here are some clues:
          When I say:    That means:
            Pico         One digit is correct but in the wrong position.
            Fermi        One digit is correct and in the right position.
            Bagels       No digit is correct.
          For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.

          I have thought up a number.
          You have {} guesses to get it.
          '''.format(numberOfDigits, maxNumberOfGuesses))

    secretNumber = getSecretNumber()
    print(secretNumber)
    guessNumber = 1
    while True: 
        guess = ''
        guess = input("Guess #{}: \n".format(guessNumber))
        if guessNumber <= maxNumberOfGuesses:
            if guess == secretNumber:
                print("You got it!")
                break
            else: 
                clues = getClues(guess, secretNumber)
                print(clues)
                guessNumber += 1 
            

        elif guessNumber > maxNumberOfGuesses:
            print("You ran out of guesses. The answer was {}".format(secretNumber))
            break

def getClues(guess, secretNumber):
    """
            Pico         One digit is correct but in the wrong position.
            Fermi        One digit is correct and in the right position.
            Bagels       No digit is correct.
          For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
    """
    clue = []
    for i in range(0,numberOfDigits):
        if guess[i] == secretNumber[i]:
            clue.append("Fermi")
        elif guess[i] in secretNumber:
            clue.append("Pico")
    clue.sort()
    return ' '.join(clue) if len(clue) != 0 else 'Bagels'

def getSecretNumber():
    secretNumber = ''
    randomNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(randomNumbers)
    secretNumber = ''.join(randomNumbers[0:numberOfDigits])
    return secretNumber

if __name__ == '__main__':
    bagel_game()