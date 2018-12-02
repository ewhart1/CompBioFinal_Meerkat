#!/usr/bin/env python

# Charis, Eric, Zara Final Project
# Simulation to plot variation in different phenotypes amongst a meerkat population

import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

class user_input(object):
#Identifying the starting population for each individual phenotype that a meerkat is capable of having.
#Identifying the amount of generations that will run along with the starting population amounts already given to each phenotype.
	def inps():
		startPop = int(input("Enter desired starting population size: "))
		smallLight = int(input("Enter number of individuals from the starting population with light-colored coats and small bodies: "))
		normalLight = int(input("Enter number of individuals from the starting population with light-colored coats and normal-sized bodies: "))
		smallDark = int(input("Enter number of individuals from the starting population with dark coats and small bodies: "))
		normalDark = int(input("Enter number of individuals from the starting population with dark coats and normal-sized bodies: "))
		numberOfGen = int(input("Enter number of generations to run: "))
#Calling on Numpy to run random array.
#Now we are allowing the simulation to randomly select integers that represent the amount of each phenotype present in the range we have provided.
		numOff_smallLight = np.random.randint(2,5,1)
		numOff_normalLight = np.random.randint(2,4,1)
		numOff_smallDark = np.random.randint(0,4,1)
		numOff_normalDark = np.random.randint(0,3,1)
#Calculating the total number of offspring per phenotype after running the random offspring generator for each generation in a particular simulation.
		total_smallLightOff = (numOff_smallLight * smallLight)
		total_normalLightOff = (numOff_normalLight * normalLight)
		total_smallDarkOff = (numOff_smallDark * smallDark)
		total_normalDarkOff = (numOff_normalDark * normalDark)
#Creating variables for later use.
		pheno = [total_smallLightOff, total_normalLightOff, total_smallDarkOff, total_normalDarkOff]
		adult_gen = [smallLight, normalLight, smallDark, normalDark]
		total_gen = [smallLight, normalLight, smallDark, normalDark]
		a = 0
#Creating empty list.
		perGen = []
		perGen2 = []
		perGen3 = []
		perGen4 = []
#While loop is calculating the total number of the populations in one generation, and the for loop is looping it for the number of generations that the user selected.
		while a < len(pheno):
			for i in range(numberOfGen):
				numOff_smallLight = np.random.randint(2,5,1)
				numOff_normalLight = np.random.randint(2,4,1)
				numOff_smallDark = np.random.randint(0,4,1)
				numOff_normalDark = np.random.randint(0,3,1)
				total_smallLightOff = (numOff_smallLight * smallLight)
				total_normalLightOff = (numOff_normalLight * normalLight)
				total_smallDarkOff = (numOff_smallDark * smallDark)
				total_normalDarkOff = (numOff_normalDark * normalDark)

#This calculates the entire population number at a specific time.
				total_gen[a] = ((pheno[a] + adult_gen[a]) + total_gen[a])
				c = total_gen[a]
#The if/elif statements calculate the products from each factor in the for loop above. It then adds each respective answer to the empty list created earlier
#Essentially, each 'perGen' empty list compounds on itself
				if a == 0:
					perGen.extend(c)
				elif a == 1:
					perGen2.extend(c)
				elif a == 2:
					perGen3.extend(c)
				else:
					perGen4.extend(c)
			a += 1

#Assigning line colors for the graph that will represent each possible phenotype. Aside from the line color, the line itself will reflect the total number of each phenotype.
		print("Total number of small size, light coat Meerkats, indicated by red line: " + str(total_gen[0]))
		print("Total number of normal size, light coat Meerkats, indicated by blue line: " + str(total_gen[1]))
		print("Total number of small size, dark coat Meerkats, indicated by green line: " + str(total_gen[2]))
		print("Total number of normal size, dark coat Meerkats, indicated by purple line: " + str(total_gen[3]))
		print("Generations run: " +str(numberOfGen))
		print(total_gen[0])
		print(perGen)
		print(perGen2)
		print(perGen3)
		print(perGen4)

#Calling on matplotlib to establish the x/y axis for each phenotype per generation.
		plt.plot(range(numberOfGen), perGen,  color='red')
		plt.plot(range(numberOfGen), perGen2, color='blue')
		plt.plot(range(numberOfGen), perGen3, color='green')
		plt.plot(range(numberOfGen), perGen4, color='purple')

#Labeling x/y axis, legend and formatting plot
		plt.xlabel("Number of Generations")
		plt.ylabel("Population Size")
		plt.title("Change in Population Size Over Generations of Different Phenotypes of MeerKats")
		abc = "Time"
		plt.figtext(0.5, 0.005, abc, wrap=True, horizontalalignment='center', fontsize=10, color='red')
#Creating a Legend to help easily identify what line represents what phenotype in the simulation.
		plt.legend(('Small light', 'Normal light', 'Small dark', 'Normal dark'), loc='upper left')
		plt.show()

user_input.inps()
