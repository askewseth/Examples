import random

class Card():
    suit_names = ["Spades", "Clubs", "Diamonds", "Hearts"]
    rank_names = ["Ace", "2", "3","4","5","6","7","8",
                  "9", "10", "Jack", "Queen", "King"]
    def __init__(self, val, suit):    
        self.val = val
        self.suit = suit
        self.valStr = self.rank_names[val]
        self.suitStr = self.suit_names[suit]
    def disp(self):
        print self.valStr, " of ",self.suitStr
    def getVal(self):
        return self.val
    def getSuit(self):
        return self.suit
        
class Deck():
    def __init__(self):
        deck = []
        for x in range(0,13):
            for y in range(4):
                deck.append(Card(x,y))
        random.shuffle(deck)
        self.deck = deck
    def printDeck(self):
        for x in range(len(self.deck)):
            self.deck[x].disp()
    def takeCard(self):
        return self.deck.pop(0)
    def shuffle(self):
        random.shuffle(self.deck)

class Pile(Deck):
    def __init__(self):
        pile = [None]
        self.pile = pile
    def add(self, card):
        """Add to the beginning of the deck, index 0"""
        self.pile.insert(0, card)
    def takeCard(self, card):
        """Draw card from pile"""
        return self.pile.pop(0)
    def showTop(self):
        if len(self.pile) == 1:
            print "\n Top of Pile: NONE"
        else:
            print "\n Top of Pile: ", self.pile[0].disp()
        
class Player():
    playersList = []
    def __init__(self, deck, name="No Name"):
        self.name = name
        hand = []
        deck.shuffle()
        for x in range(5):
            hand.append(deck.takeCard())
##        self.deck = deck
        self.hand = hand
    def showHand(self):
        self.sortHand()
        for y, x in enumerate(range(len(self.hand))):
            suit = self.hand[x].suitStr
            val = self.hand[x].valStr
            show = ": " + val + " of " + suit
            print y+1, show
    def sortHand(self):
        self.hand.sort(key= lambda x: x.val, reverse=True)
    def newHand(self):
        hand = []
        for x in range(5):
            hand.append(deck.takeCard())
        self.hand = hand
    def dropCard(self, pile, iCard):
        """Throws one card down to pile"""
        pile.add(self.hand.pop(iCard))
    def dropLowestTurn(self, deck, pile):
        printSmSpacer()
        #Take card from deck
        print "\n {}'s TURN: \n".format(self.name)
        print "Before: "
        self.showHand()
        #Take card from deck
        self.hand.append(deck.takeCard())
        #Sort Hand
        self.sortHand()
        #Drop the highest card in your hand
        self.dropCard(pile, 0)
        print "\n After: "
        self.showHand()
        print "\n I {} am done. \n".format(self.name)
    def takeTurn(self, deck, pile):
        printSmSpacer()
        print "\n It's {}'s Turn. \n".format(self.name)
        self.showHand()
        self.checkSpreadSame()
        self.checkSpreadSeq()
        #Get new card
        inp = input("Press 1 to draw from deck, 2 to pick from pile:\n")
        if inp == 2:
            pile.takeCard()
        if inp == 1:
            self.hand.append(deck.takeCard())
        self.sortHand()
        self.showHand()
        self.checkSpreadSame()
        inp = input("Which card would you like to toss?\n")
        self.dropCard(pile, inp-1)
        print "\n{}'s Turn is done\n".format(self.name)
    def check(self):
        """All the check methods put together"""
        checks = []
        checks.append(self.checkSpreadSame())

        for check in checks:
            if checks[check] == True:
                print "You have a spread"
    def checkSpreadSame(self):
        """Checks if 3 of a kind are present in hand"""
        self.sortHand()
        vals = []
        for x in range(len(self.hand)):
            vals.append(self.hand[x].val)
        for x in range(len(vals)):
            if vals.count(vals[x]) > 2:
                print "You can spread with {}'s".format(self.hand[x].valStr)
                return True
        return False
    def checkSpreadSeq(self):
        """Checks if 3 in a sequence are present in hand"""
        spade = []
        club = []
        diamond = []
        heart = []
        suits = [spade, club, diamond, heart]
        for card in self.hand:
            if card.val == 0:
                spade.append(card)
            elif card.val == 1:
                club.append(card)
            elif card.val == 2:
                diamond.append(card)
            elif card.val == 3:
                heart.append(card)
##        print "After adding to lists"
##        print ""
##        for x, suit in enumerate(suits):
##            print ''
##            print x, ": "
##            for card in suit:
##                card.disp()
        for suit in suits:
            suit.sort()
            for x in range(len(suit)-2):
                if card[x].val == card[x+1].val-1 == card[x+2].val-2:
                    seq = [card[x], card[x+1], card[x+2]]
                    print "You can spread with: "
                    for card in seq:
                           card.disp()
                    return seq
        dum = Card(-1,-1)
        return [dum, dum, dum]

                
class Bot(Player):
    def __init__(self, deck, name = "Bot" ):
        hand = []
        deck.shuffle()
        for x in range(5):
            hand.append(deck.takeCard())
        self.hand = hand
        self.name = name
    def takeTurn(self, deck, pile):
        self.dropLowestTurn(deck, pile)

def printSpacer():
    dots = ["." for x in range(50)]
    print "".join(dots)

def printSmSpacer():
    dots = ["." for x in range(25)]
    print ''.join(dots)
    
def PlayGame():
    numPlayers = 2
    deck = Deck()
    deck.shuffle()
    pile = Pile()
    
    player = Player(deck, "Player 1")
    bot = Bot(deck)
    liPlayers = [bot, player]

    player.sortHand()
    bot.sortHand()
    
    printSpacer()
    print "\n{}'s hand: ".format(player.name)
    player.showHand()
    print "\n{}'s hand: ".format(bot.name)
    bot.showHand()

##    printSpacer()
##    player.dropLowestTurn(deck, pile)
##    bot.dropLowestTurn(deck, pile)

    printSpacer()

    play = True
    while play == True: 
        for plr in liPlayers:
            pile.showTop()
            plr.takeTurn(deck, pile)
            if len(plr.hand) == 0:
                print "WINNER"
                play = False



    

def test():
    deck = Deck()
    deck.printDeck()
    for x in range(5):
        print ""
    deck.shuffle()
    deck.printDeck()
    seth = Player(deck, "Seth")
    for x in range(5):
        print ""
    print seth.name
    seth.showHand()

def testSort():
    deck = Deck()
    seth = Player(deck,"Seth")

##deck = Deck()
##bot = Bot(deck)
##player = Player(deck, "Player")
##pile = Pile()
##ace = Card(1,1)
##
##win = Player(deck)
##w = Card(1,0)
##o = Card(0,0)
##n = Card(2,0)
##win.hand = [w,o,n]
##win.checkSpreadSame()
##win.checkSpreadSeq()

