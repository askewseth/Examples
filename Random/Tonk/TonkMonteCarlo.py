import Tonk as t

samples = 10000
hands = []
for x in range(samples):
##    if x %1000 == 0:
##        print x
    deck = t.Deck()
    plr = t.Player(deck)
    summ  = 0
    for card in plr.hand:
        summ += card.val
    hands.append(summ)

##for h in hands:
##    print h

wins = 0
for h in hands:
    if h > 48:
        wins=wins+1

print 'Number of 49 or 50 hands: ', wins
print 'Total number of trials: ', samples
print 'Percentage of winning hands: ', 1.0/wins/samples*100
