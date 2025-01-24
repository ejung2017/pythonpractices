import random 

HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.

"""
Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.'''
 """

def main(): 
    money = 5000
    print("Money: {}".format(money))
    remaining = getBet(money)
    print(remaining)

def getBet(money): 
    """Ask the player how much they want to bet for this round."""
    print("How much do you bet? (1-5000, or QUIT)")
    betAmount = int(input("> "))
    while True: 
        if betAmount > money: 
            print("You don't have that much monies!")
        else: 
            money -= betAmount
        break
    return money


    pass

def getDeck(): 
    """Return a list of (rank, suit) tuples for all 52 cards."""
    pass

def displayHands(): 
    """Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False."""
    pass

def getHandValue():
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this function picks the most suitable ace value).""" 
    pass

def displayCards(): 
    """Display all the cards in the cards list."""
    pass

def getMove():
    """Asks the player for their move, and returns 'H' for hit, 'S' for stand, and 'D' for double down.""" 
    pass


if __name__ == "__main__": 
    main()