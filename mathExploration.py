from random import *
from colorama import Fore, Style
from copy import deepcopy
totals = []
spaces = [
	"go","brown1","chest","brown2","incTax","rail1","lightBlue1","chance","lightBlue2","lightBlue3", # First Row
	"visitJail","purple1","electric","purple2","purple3","rail2","orange1","chest","orange2","orange3", # Second Row
	"parking","red1","chance","red2","red3","rail3","yellow1","yellow2","water","yellow3", # Third Row
	"toJail","green1","green2","chest","green3","rail4","chance","blue1","luxTax","blue2" # Final Row
]

chestcards = [
	"gotoGo","gotoJail",
	"N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A"
]
chancecards = [
	"back3","gotoGo","gotoJail","gotoR3","gotoP1","gotoB2","gotoRail","gotoRail","gotoUtil","gotoRail1",
	"exitJail","money","money","money","money","money"
]

for x in range(len(spaces)):
	totals.append(0)


	
class player(object):
	space=0
	money=0




	def roll(self):

		rolled = getroll()
		self.space += rolled
		if self.space > (len(spaces)-1):
			self.space -= (len(spaces))

		

		

		if spaces[self.space] == "chance":
			self.chance()
			#pass

		if spaces[self.space] == "chest":
			self.chest()
			#pass

		spacesout[self.space] += 1


		if self.space == 30: # The to jail space
			self.space = 10
		





	def chance(self):
		#"back3","gotoGo","gotoJail","gotoR3","gotoP1","gotoB2","gotoRail","gotoRail","gotoUtil","gotoRail1"
		rcard = chancecurrent.pop(0)
		chancecurrent.append(rcard)
		#rcard = randint(1,16)
		if rcard == "gotoGo":
			self.space = 0

		elif rcard == "gotoR3":
			self.space = spaces.index("red3")

		elif rcard == "gotoP1":
			self.space = spaces.index("purple1")

		elif rcard == "gotoUtil":
			space1 = spaces.index("water")
			space2 = spaces.index("electric")
			d1 = abs(self.space-space1)
			d2 = abs(self.space-space2)
			if d1 > d2:
				self.space = space1
			else:
				self.space = space2

		elif rcard == "gotoRail":
			space1 = spaces.index("rail1")
			space2 = spaces.index("rail2")
			space3 = spaces.index("rail3")
			space4 = spaces.index("rail4") 
			d1 = abs(self.space-space1)
			d2 = abs(self.space-space2)
			d3 = abs(self.space-space3)
			d4 = abs(self.space-space4)
			trains = [d1,d2,d3,d4]
			goto = min(trains)
			self.space = abs(self.space-goto)

		elif rcard == "back3":
			self.space = self.space - 3
			if self.space < 0:
				self.space += (len(spaces))

		elif rcard == "gotoJail":
			self.space = 10

		elif rcard == "gotoRail1":
			self.space = spaces.index("rail1")

		elif rcard == "gotoB2":
			self.space = spaces.index("blue2")


	def chest(self):
		cCard = chestcards.pop(0)
		if cCard == "gotoGo":
			self.space = 0
		if cCard == "gotoJail":
			self.space = 10
		chestcards.append(cCard)
		#cCard = randint(1,16)
		#if cCard == 1:
		#	self.space = 0
		#elif cCard == 2:
		#	self.space = 10

		#print(self.space)
		#print(spaces[self.space])







def getroll():
	#droll = randint(1,6)
	#droll2 = randint(1,6)
	#froll = droll+droll2
	dice1 = [1,2,3,4,5,6]
	dice2 = [1,2,3,4,5,6]
	shuffle(dice1)
	shuffle(dice2)
	randindex = randint(0,5)
	randindex2 = randint(0,5)
	froll = dice1[randindex] + dice2[randindex2]
	return froll

p1 = player()
p2 = player()
p3 = player()
p4 = player()























for g in range(50): # Run 10 games

	#print(spaces)

	spacesout = []

	for x in range(len(spaces)):
		spacesout.append(0)


	chestcurrent = deepcopy(chestcards)
	shuffle(chestcurrent)
	chancecurrent = deepcopy(chancecards)
	shuffle(chancecurrent)
	#print(chancecurrent)
	#print(chestcurrent)

	p1.space = 0
	p2.space = 0
	p3.space = 0
	p4.space = 0
	

	for x in range(75):
		p1.roll()
		p2.roll()
		p3.roll()
		p4.roll()

	output = f"Spaces of game {g+1}: "
	for x in range(len(spaces)):
		output += f"{Fore.GREEN}{spaces[x]}{Style.RESET_ALL}:{Fore.RED}{spacesout[x]}{Style.RESET_ALL}, "


	print(output)


	for x in range(len(spacesout)):
		totals[x] += spacesout[x]















spacesN = deepcopy(spaces)
totalsN = deepcopy(totals)

output = "Final Spaces: "
for x in range(len(spaces)):
	output += f"{Fore.GREEN}{spaces[x]}{Style.RESET_ALL}:{Fore.RED}{totals[x]}{Style.RESET_ALL}, "

print("\n\n\n")
print(output)
print("\n")
highest = max(totals)
index = totals.index(highest)
print(f"Highest Value is: {highest} on {spaces[index]}")
totals.pop(index)
spaces.pop(index)

highest = max(totals)
index = totals.index(highest)
print(f"Second Greatest Value is: {highest} on {spaces[index]}")
totals.pop(index)
spaces.pop(index)

highest = max(totals)
index = totals.index(highest)
print(f"Third Greatest Value is: {highest} on {spaces[index]}")
totals.pop(index)
spaces.pop(index)

'''
spaces = [
	"go","brown1","chest","brown2","incTax","rail1","lightBlue1","chance","lightBlue2","lightBlue3", # First Row
	"visitJail","purple1","electric","purple2","purple3","rail2","orange1","chest","orange2","orange3", # Second Row
	"parking","red1","chance","red2","red3","rail3","yellow1","yellow2","water","yellow3", # Third Row
	"toJail","green1","green2","chest","green3","rail4","chance","blue1","luxTax","blue2" # Final Row
]
'''
brown = 0
rail = 0
lightBlue = 0
purple = 0
util = 0
orange = 0
red = 0
yellow = 0
green = 0
blue = 0
for x in spacesN:
	if "brown" in x:
		brown += totalsN[spacesN.index(x)]
	elif "rail" in x:
		rail += totalsN[spacesN.index(x)]
	elif "lightBlue" in x:
		lightBlue += totalsN[spacesN.index(x)]
	elif "purple" in x:
		purple += totalsN[spacesN.index(x)]
	elif "electric" == x or "water" == x:
		util += totalsN[spacesN.index(x)]
	elif "orange" in x:
		orange += totalsN[spacesN.index(x)]
	elif "red" in x:
		red += totalsN[spacesN.index(x)]
	elif "yellow" in x:
		yellow += totalsN[spacesN.index(x)]
	elif "green" in x:
		green += totalsN[spacesN.index(x)]
	elif "blue" in x:
		blue += totalsN[spacesN.index(x)]

output = "\n\n\nTOTALS: "

output += f"Brown:{Fore.BLACK}{brown}{Style.RESET_ALL}, "
output += f"Rail:{Fore.CYAN}{rail}{Style.RESET_ALL}, "
output += f"Light Blue:{Fore.BLUE}{lightBlue}{Style.RESET_ALL}, "
output += f"Purple:{Fore.MAGENTA}{purple}{Style.RESET_ALL}, "
output += f"Util:{Fore.CYAN}{util}{Style.RESET_ALL}, "
output += f"Orange:{Fore.YELLOW}{orange}{Style.RESET_ALL}, "
output += f"Red:{Fore.RED}{red}{Style.RESET_ALL}, "
output += f"Yellow:{Fore.YELLOW}{yellow}{Style.RESET_ALL}, "
output += f"Green:{Fore.GREEN}{green}{Style.RESET_ALL}, "
output += f"Blue:{Fore.BLUE}{blue}{Style.RESET_ALL}"

print(output)

finalresults = [brown,rail,lightBlue,purple,util,orange,red,yellow,green,blue]
finalresultscolors = ["brown","rail","lightBlue","purple","util","orange","red","yellow","green","blue"]


print("\n")
highest = max(finalresults)
index = finalresults.index(highest)
print(f"Highest Value is: {highest} on {finalresultscolors[index]}")
finalresults.pop(index)
finalresultscolors.pop(index)

highest = max(finalresults)
index = finalresults.index(highest)
print(f"Second Greatest Value is: {highest} on {finalresultscolors[index]}")
finalresults.pop(index)
finalresultscolors.pop(index)

highest = max(finalresults)
index = finalresults.index(highest)
print(f"Third Greatest Value is: {highest} on {finalresultscolors[index]}")
finalresults.pop(index)
finalresultscolors.pop(index)


highest = max(finalresults)
index = finalresults.index(highest)
print(f"Fourth Greatest Value is: {highest} on {finalresultscolors[index]}")
finalresults.pop(index)
finalresultscolors.pop(index)