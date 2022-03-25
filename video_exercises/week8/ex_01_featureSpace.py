"""01 Exercise: feature space

    Create a function to generate a set of tuples containing data about babies
        The function takes an argument of how many babies/samples to create
        Each baby has height, weight and age (in months) properties
    Create a function to plot the 3 dimensional feature space of the babies
        Each baby is represented as a scatter dot
    Rewrite the create function to create babies that are getting taller and heavier as they get older
        Rerun the plot function to see if you get an approximately linear visual representation.

"""
import numpy as np


def baby_data(samples):
    data = {'Height':[55, 47, 42, 70, 51, 53], 'Weight':[3.0, 2.8, 3.5, 2.9, 2.7, 3.2], 'Age':[3, 4, 8, 6, 5, 9]}
    baby_list.append((np.random.randint(42, 56), np.random.randint(2.4, 3.8) , np.random.randint(2, 12)))