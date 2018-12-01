'''
@Title of program: Math - Method 1 - 30-1 IA
@Author: Chinmay Patil
@Date of last edit: <2018-11-14 21:38:14>
@Amount of saves: <16>
'''

### HOW TO RUN: open cmd/terminal and type in python3 then drag this file into the terminal... or just double click this file ###

dict = {} # Create a dictionary (basicly a list)

for x in range(40): # Populate dictionary
	dict[x] = 0


distance = 0 # start at go
for x in range(75): # repeat following code 75 times

	distance += 7 # Add 7
	dict[distance%40] += 1 # Add 1 to the space that is the modulus of the distance and 40 (the number of spaces)



for x in range(40): # repeat following code 40 times

	if dict[x] == 1: # if a space has not been landed on 2 times, print it
		print(f"{x} : {dict[x]}")