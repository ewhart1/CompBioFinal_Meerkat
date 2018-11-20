#!/usr/bin/env python

# Charis, Eric, Zara Final Project
# Simulation to plot variation in different phenotypes amongst a meerkat population

import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
print("Hello")

class individual(object):
    def __init__(self, smallLight, normalLight, smallDark, normalDark, numOff):
        self.smallLight = smallLight
        self.normalLight = normalLight
        self.smallDark = smallDark
        self.normalDark = normalDark
        self.numOff = numOff

    def reproduce(self):
        self.numOff.smallLight = nr.poisson(2, 4)

# User inputs for the population simulation
totalPop = input("Enter desired starting population size: ")
smallLight = input("Enter number of individuals from the starting population with light-colored coats and small bodies: ")
normalLight = input("Enter number of individuals from the starting population with light-colored coats and normal-sized bodies: ")
smallDark = input("Enter number of individuals from the starting population with dark coats and small bodies: ")
normalDark = input("Enter number of individuals from the starting population with dark coats and normal-sized bodies: ")
numberOfGen = input("Enter number of generations to run: ")
carryingCapacity = input("Enter the carrying capacity of the total population (all phenotypes combined): ")

