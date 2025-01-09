import random 

numberOfDigits = 3

randomNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(randomNumbers)
print(randomNumbers)
secretNumber = ''.join(randomNumbers[0:numberOfDigits])
print(secretNumber)

guessNumber = 1
turn = input("Guess #{}: \n".format(guessNumber))
print(turn)

def getSecretNumber():
    secretNumber = ''
    randomNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(randomNumbers)
    secretNumber = ''.join(randomNumbers[0:numberOfDigits])
    return secretNumber

print(secretNumber)