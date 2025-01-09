import random 

numberOfDigits = 3
maxNumberOfGuesses = 3 

def main(): 
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
        if guessNumber <= maxNumberOfGuesses: 
            guess = ''
            guess = input("Guess #{}: \n".format(guessNumber))

            if guess == secretNumber: 
                print("You got it!")
                break
            else: 
                clue = getClues(guess, secretNumber)
                ans = ' '.join(clue)
                print(ans)
                guessNumber += 1 
        else: 
            print("You don't have any more chances. The secret number was {}".format(secretNumber))
            break 
    
def getClues(guess, secretNumber): 
    clue = []
    for digit in range(numberOfDigits): 
        if guess[digit] == secretNumber[digit]: 
            clue.append("Fermi")
        elif guess[digit] in secretNumber: 
            clue.append("Pico")
    clue.sort()
    if clue == []: 
        clue.append("Bagel")
    return clue 

def getSecretNumber(): 
    secretNumber = ''
    randomNumber = ['1', '2', '4', '5', '6', '7', '8', '9', '0']
    random.shuffle(randomNumber) 
    secretNumber = ''.join(randomNumber[0:numberOfDigits]) 
    return secretNumber  
    

if __name__ == '__main__': 
    main() 