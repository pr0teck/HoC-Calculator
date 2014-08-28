#import console

global levelTier
levelTier = {1:[10, 20], 2:[20, 30, 40], 3:[30, 40, 50, 70], 4:[40, 50, 60, 80], 5:[50, 60, 70, 90], 6:[60, 70, 80, 100]}

cards = {1:['Card Name', 5440, 1712, 2], 2:['Card Name 2', 7990, 1930, 3], 3:['Sun Mage', 5546, 1429, 4], 4:['Bourgard', 4320, 1368, 4]}

class Card:
    def __init__(self, id):
        self.id = id
        self.stats = cards[id][1:3]
        self.level = 1
        self.tier = 1
        self.stars = cards[id][3]

    def upgradeLevel(self, maxlevel):
        print 'Upgrade to level ' + str(maxlevel)
        for level in range(maxlevel):
            if level>=1 and level<10:
                self.stats[0] += self.stats[0]*0.02
                self.stats[1] += self.stats[1]*0.02

            if level>=10 and level<30:
                self.stats[0] += self.stats[0]*0.015
                self.stats[1] += self.stats[1]*0.015

            if level>=30 and level<50:
                self.stats[0] += self.stats[0]*0.01
                self.stats[1] += self.stats[1]*0.01

            if level>=50 and level<70:
                self.stats[0] += self.stats[0]*0.005
                self.stats[1] += self.stats[1]*0.005
                
            if level>=70:
                self.stats[0] += self.stats[0]*0.01
                self.stats[1] += self.stats[1]*0.01
        self.level = maxlevel

    def isMaxLevel(self, tier):
        #levels = levelTier.get(self.stars)
        return self.level == levelTier[self.stars][tier-1]

def upgradeTier (card1, card2):
    maxTier = max(card1.tier,card2.tier)
    print 'Evolve tier from ' + str(maxTier) + ' to ' + str(maxTier+1)
    defaultHealth = cards[card1.id][1]
    defaultAttack = cards[card1.id][2]
    if card1.isMaxLevel(card1.tier):
        delta1hp = card1.stats[0]*0.1
        delta1attack = card1.stats[1]*0.1
    else:
        delta1hp = card1.stats[0]*0.05
        delta1attack = card1.stats[1]*0.05

    if card2.isMaxLevel(card2.tier):
        delta2hp = card2.stats[0]*0.1
        delta2attack = card2.stats[1]*0.1
    else:
        delta2hp = card2.stats[0]*0.05
        delta2attack = card2.stats[1]*0.05     

    deltaHP = delta1hp + delta2hp
    print 
    deltaAttack = delta1attack + delta2attack
    
    if maxTier==1:
        koeff = 1.2
    elif maxTier==2:
        koeff = 1.5
    elif maxTier==3:
        koeff = 2
    newstats = [defaultHealth*koeff + deltaHP, defaultAttack*koeff + deltaAttack]
    newCard = Card (card1.id)
    newCard.stats = newstats
    newCard.stars = card1.stars
    newCard.tier = maxTier+1
    print newCard.stats
    print newCard.tier
    return newCard

def input_number(prompt, min_value, max_value):
    value = None
    while value is None:
        try:
            value = int(raw_input(prompt))
        except ValueError:
            print 'Please enter a number!'
        if value < min_value or value > max_value:
            print ('Please enter a number between %i and %i!' % 
                   (min_value, max_value))
            value = None
    return value

def perfectTier(card, tier):
    maxLevel = levelTier[card.stars][tier-1]
    card.upgradeLevel(maxLevel)

#console.clear()
print 'Choose a card:'
for card in cards:
    print str(card) + ': ' + cards[card][0]

cardnumber = input_number('Which card do you want to see: ', 1, len(cards))

Tier1card = Card(cardnumber)
perfectTier(Tier1card, 1)
print 'perfect T1: ' + str(Tier1card.stats)
Tier2card = upgradeTier(Tier1card, Tier1card)
perfectTier(Tier2card, 2)
print 'perfect T2: ' + str(Tier2card.stats)
Tier3card = upgradeTier(Tier2card, Tier2card)
perfectTier(Tier3card, 3)
print 'perfect T3: ' + str(Tier3card.stats)
Tier4card = upgradeTier(Tier3card, Tier3card)
perfectTier(Tier4card, 4)
print Tier4card.stats


