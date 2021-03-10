from random import shuffle

def createDeck():
	Deck = []
	faceValues = ["A", "J", "Q", "K"]

	for i in range(4): #4 type of cards
		for card in range(2,11): #adding number 2-10
			Deck.append(str(card))
		for card in faceValues:
			Deck.append(card)
	shuffle(Deck)
	return Deck

class Player:
	def __init__(self, hand = [], money = 100):
		self.Hand = hand
		self.score = self.setScore()
		self.money = money
		self.bet = 0

	def __str__(self): #print(Player)
		currHand = ""
		for card in self.Hand:
			currHand += str(card) + " "

		finalStatus = currHand + "score: " + str(self.score)
		# A 10 score: 21
		return finalStatus

	def setScore(self):
		self.score = 0
		faceCardsDict = {"A":11, "J": 10, "Q":10, "K":10, "2":2, "3":3, "4":4,
						"5":5, "6":6, "7":7,"8":8, "9":9,"10":10}

		aceCounter = 0
		for card in self.Hand:
			self.score += faceCardsDict[card]
			if card == "A":
				aceCounter += 1
			if self.score > 21 and aceCounter != 0:
				self.score -= 10
				aceCounter -= 1
		return self.score

	def hit(self, card):
		self.Hand.append(card)
		self.score = self.setScore()

	def play(self, newHand):
		self.Hand = newHand
		self.score = self.setScore()

	def betMoney(self, amonut):
		self.money -= amonut
		self.bet += amonut

	def win(self, result):
		if result == True:
			if self.score == 21 and len(self.Hand) == 2:
				self.money += 2.5*self.bet
			else:
				self.money += 2 * self.bet
			self.bet = 0
		else:
			self.bet = 0

	def draw(self):
		self.money += self.bet
		self.bet = 0

	def hasBlackJack(self):
		if self.score == 21 and len(self.Hand) == 2:
			return True
		else:
			return False


def printHouse(House):
	for card in range(len(House.Hand)):
		if card == 0:
			print("X")
			print("\n")
		elif card -- len(House.Hand) - 1:
			print(House.Hand[card])
		else:
			print(House.Hand[card])
			print("\n")

cardDeck = createDeck()
firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]
Player1 = Player(firstHand)
House = Player(secondHand)
cardDeck = createDeck()

while(True):
	if len(cardDeck) < 20:
		cardDeck = createDeck()
	firstHand = [cardDeck.pop(), cardDeck.pop()]
	secondHand = [cardDeck.pop(), cardDeck.pop()]
	Player1.play(firstHand)
	House.play(secondHand)
	Bet = int(input("Enter your bet:" ))
	Player1.betMoney(Bet)

	print(cardDeck)
	printHouse(House)
	print(Player1)

	if Player1.hasBlackJack():
		if House.hasBlackJack():
			Player1.draw()
		else:
			Player1.win(True)
	else:
		while(Player1.score < 21):
			action = int(input("Do you want another card?(1/0): "))
			if action == 1:
				Player1.hit(cardDeck.pop())
				print(Player1)
				printHouse(House)
			else:
				break
		while(House.score < 16):
			print(House)
			House.hit(cardDeck.pop())
		if Player1.score > 21:
			if House.score > 21:
				Player1.draw()
			else:
				Player1.win(False)
		elif Player1.score > House.score:
			Player1.win(True)
		elif Player1.score == House.score:
			Player1.draw()
		else:
			if House.score > 21:
				Player1.win(True)
			else: 
				Player1.win(False)

print(Player1.money)
print(House)


