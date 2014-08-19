global levelTier
levelTier = {1:[10, 20], 2:[20, 30, 40], 3:[30, 40, 50, 70], 4:[40, 50, 60, 80], 5:[50, 60, 70, 90], 6:[60, 70, 80, 100]}

#health = 5440
#attack = 1712

health = 7990
attack = 1930

stats = [health, attack]


class Card:
    def __init__(self, stats, stars, tier):
        self.stats = stats
        self.level = 1
        self.tier = tier
        self.stars = stars
    
    def upgradeLevel(self, maxlevel):
        for level in range(maxlevel):
            if level>=1 and level<10:
                self.stats[0] += self.stats[0]*0.02
                self.stats[1] += self.stats[1]*0.02
                
            if level>=10 and level<30:
                self.stats[0] += self.stats[0]*0.015
                self.stats[1] += self.stats[1]*0.015
                
            if level>=30 and level<=50:
                self.stats[0] += self.stats[0]*0.01
                self.stats[1] += self.stats[1]*0.01
            
            if level>50:
                self.stats[0] += self.stats[0]*0.005
                self.stats[1] += self.stats[1]*0.005
        self.level = maxlevel

    def isMaxLevel(self, tier):
        levels = levelTier.get(self.stars)
        return self.level == levels[tier-1]
            
def upgradeTier (card1, card2):
    if card1.isMaxLevel(card1.tier):

        delta1hp = card1.stats[0]*0.1
        delta1attack = card1.stats[1]*0.1
    else:
        delta1hp = card1.stats[0]*0.05
        print delta1hp
        delta1attack = card1.stats[1]*0.05
        print delta1attack
        
    if card2.isMaxLevel(card2.tier):
        delta2hp = card2.stats[0]*0.1
        delta2attack = card2.stats[1]*0.1
    else:
        delta2hp = card2.stats[0]*0.05
        delta2attack = card2.stats[1]*0.05     
    
    deltaHP = delta1hp + delta2hp
    deltaAttack = delta1attack + delta2attack
    
    newstats = [card1.stats[0]*1.2 + deltaHP, card1.stats[1]*1.2 + delta1attack]
    
    newCard = Card (newstats, card1.stars, card1.tier + 1)
    return newCard
        
card = Card(stats, 4, 2)
#card.upgradeLevel(50)
newcard = upgradeTier(card, card)
print newcard.stats
print card.level



