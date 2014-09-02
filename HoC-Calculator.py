import console

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

	def isMaxLevel(self):
		#levels = levelTier.get(self.stars)
		return self.level == levelTier[self.stars][self.tier-1]

def upgradeTier (card1, card2):
	defaultHealth = cards[card1.id][1]
	defaultAttack = cards[card1.id][2]
	if card1.isMaxLevel():
		delta1hp = card1.stats[0]*0.1
		delta1attack = card1.stats[1]*0.1
	else:
		delta1hp = card1.stats[0]*0.05
		delta1attack = card1.stats[1]*0.05

	if card2.isMaxLevel():
		delta2hp = card2.stats[0]*0.1
		delta2attack = card2.stats[1]*0.1
	else:
		delta2hp = card2.stats[0]*0.05
		delta2attack = card2.stats[1]*0.05     

	deltaHP = delta1hp + delta2hp
	print 
	deltaAttack = delta1attack + delta2attack
	
	if max(card1.tier,card2.tier)==1:
		koeff = 1.2
	elif max(card1.tier,card2.tier)==2:
		koeff = 1.5
	elif max(card1.tier,card2.tier)==3:
		koeff = 2
	newstats = [defaultHealth*koeff + deltaHP, defaultAttack*koeff + deltaAttack]
	newCard = Card (card1.id)
	newCard.stars = newstats
	newCard.tier = max(card1.tier,card2.tier)+1
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

console.clear()
print 'Choose a card:'
for card in cards:
	print str(card) + ': ' + cards[card][0]

cardnumber = input_number('Which card do you want to see: ', 1, len(cards))

Tier1card = Card(cardnumber)
maxlvl = levelTier[Tier1card.stars][Tier1card.tier-1]
Tier1card.upgradeLevel(maxlvl)
print Tier1card.stats
#perfectTier(Tier1card, 1)
Tier2card = upgradeTier(Tier1card, Tier1card)
#perfectTier(Tier2card, 2)
Tier3card = upgradeTier(Tier2card, Tier2card)
#perfectTier(Tier3card, 3)
Tier4card = upgradeTier(Tier3card, Tier3card)
#perfectTier(Tier4card, 4)
print Tier4card




#health = input_number('Health: ', 1, 20000)
#attack = input_number('Attack: ', 1, 10000)
#stars = input_number('Stars: ', 1, 6)
#tier = input_number('Tier: ', 1, 4)

#stats = [health, attack]
#card = Card(3, stats, stars, tier)

#card.upgradeLevel(90)
#card.level = 60
#print card.stats
#newcard = upgradeTier(card, card)
#print newcard.stats
#print newcard.level
#newcard.upgradeLevel(80)
#print newcard.stats
#print newcard.level
