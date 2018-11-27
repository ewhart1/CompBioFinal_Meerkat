#!/usr/bin/env python

# Charis, Eric, Zara Final Project
# Simulation to plot variation in different phenotypes amongst a meerkat population

import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

class user_input(object):

	def inps():
		startPop = int(input("Enter desired starting population size: "))
		smallLight = int(input("Enter number of individuals from the starting population with light-colored coats and small bodies: "))
		normalLight = int(input("Enter number of individuals from the starting population with light-colored coats and normal-sized bodies: "))
		smallDark = int(input("Enter number of individuals from the starting population with dark coats and small bodies: "))
		normalDark = int(input("Enter number of individuals from the starting population with dark coats and normal-sized bodies: "))
		numberOfGen = int(input("Enter number of generations to run: "))

		numOff_smallLight = np.random.randint(2,5,1)
		numOff_normalLight = np.random.randint(2,4,1)
		numOff_smallDark = np.random.randint(0,4,1)
		numOff_normalDark = np.random.randint(0,3,1)
		total_smallLightOff = (numOff_smallLight * smallLight)
		total_normalLightOff = (numOff_normalLight * normalLight)
		total_smallDarkOff = (numOff_smallDark * smallDark)
		total_normalDarkOff = (numOff_normalDark * normalDark)

		pheno = [total_smallLightOff, total_normalLightOff, total_smallDarkOff, total_normalDarkOff]
		adult_gen = [smallLight, normalLight, smallDark, normalDark]
		total_gen = [smallLight, normalLight, smallDark, normalDark]
		per_gen = [pheno, adult_gen]
		a = 0
		
# insert an empty list		
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

				total_gen[a] = ((pheno[a] + adult_gen[a]) + total_gen[a])

			a += 1

#		for z in numberOfGen:
#			per_gen = (pheno + adult_gen)
#			per_gen[z+1] = per_gen[z] 


		num_1 = [smallLight]*(numberOfGen+1)
		num_2 = [normalLight]*(numberOfGen+1)
		num_3 = [smallDark]*(numberOfGen+1)
		num_4 = [normalDark]*(numberOfGen+1)

		print("Total number of small size, light coat Meerkats: " + str(total_gen[0]))
		print("Total number of normal size, light coat Meerkats: " + str(total_gen[1]))
		print("Total number of small size, dark coat Meerkats: " + str(total_gen[2]))
		print("Total number of normal size, dark coat Meerkats: " + str(total_gen[3]))
		print("Generations run: " +str(numberOfGen))
		print(total_gen[0])
#		print(per_gen[a])


		plt.plot(range(numberOfGen+1), num_1,  color='red')
#		plt.plot(range(numberOfGen+1), num_2, color='blue')
#		plt.plot(range(numberOfGen+1), num_3, color='green')
#		plt.plot(range(numberOfGen+1), num_4, color='purple')


# Labeling x and y axis and formatting plot.
		plt.xlabel("Number of Generations")
		plt.ylabel("Population Size")
		plt.title("Change in Population Size Over Generations of Different Phenotypes of MeerKats")
		abc = "Time"
		plt.figtext(0.5, 0.005, abc, wrap=True, horizontalalignment='center', fontsize=10, color='red')
		plt.show()


user_input.inps()


