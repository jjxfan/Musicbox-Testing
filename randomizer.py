import pandas as pd
import random
import math

# For the file to specify ranges.
FILE_NAME = 'concentration_ranges/concentration_ranges.csv'
RANDOM_FILE_NAME = 'concentration_ranges/random_concentration_ranges.csv'

GENERAL_NAME_COL = 'general_name'
CHEMICAL_NAME_COL = 'chemical_name'
TYPE_COL = 'type'
CONCENTRATION_COL = 'concentration'
MINIMUM_COL = 'min'
MAXIMUM_COL = 'max'
POW_10_COL = 'pow10' 

rand_species = pd.read_csv(RANDOM_FILE_NAME, index_col=False)
set_species = pd.read_csv(FILE_NAME, index_col=False)


# To store final concentrations

# For the main configuration file
CONCENTRATION_KEY = 'initial value [molecule cm-3]'

CONVERSION_RATE = '?'

# Lines 590 - 592
def randomize_concentrations(species_data):
    totals_of_randomized_species = {}
    for type in rand_species[TYPE_COL].unique():
        totals_of_randomized_species[type] = 0.0

    for index, row in rand_species.iterrows():
        species = row.loc[CHEMICAL_NAME_COL]
        pow10 = row.loc[POW_10_COL]
        init_conc = random.uniform(row.loc[MINIMUM_COL], row.loc[MAXIMUM_COL])
        # print(species)
        # print(init_conc)
        # print(pow10)
        while (init_conc >= 10):
            init_conc /= 10
            pow10 += 1
        while (init_conc < 1):
            init_conc *= 10
            pow10 -= 1
        # print(pow10)
        # print(init_conc)
        # print(species)

        totals_of_randomized_species[row.loc[TYPE_COL]] += init_conc * math.pow(10, pow10)
        if (species not in species_data.keys()):
            species_data[species] = {CONCENTRATION_KEY: ''}
        species_data[species][CONCENTRATION_KEY] = '{conc:.2f}E{plus}{power}'.format(
                conc=init_conc, 
                plus= "+" if (pow10 > 0) else "",
                power=pow10)

    return totals_of_randomized_species

    

def set_concentrations(species_data):
    totals_of_randomized_species = {}
    for type in set_species[TYPE_COL].unique():
        totals_of_randomized_species[type] = 0.0

    for index, row in set_species.iterrows():
        species = row.loc[CHEMICAL_NAME_COL]
        pow10 = row.loc[POW_10_COL]
        init_conc = row.loc[CONCENTRATION_COL]
        while (init_conc >= 10):
            init_conc /= 10
            pow10 += 1
        while (init_conc < 1):
            init_conc *= 10
            pow10 -= 1

        totals_of_randomized_species[row.loc[TYPE_COL]] += init_conc * math.pow(10, pow10)
        if (species not in species_data.keys()):
            species_data[species] = {CONCENTRATION_KEY: ''}
        species_data[species][CONCENTRATION_KEY] = '{conc:.2f}E+{power}'.format(conc=init_conc, power=pow10)

    return totals_of_randomized_species

def get_random_compound_cols():
    items = []
    for type in rand_species[TYPE_COL].unique():
        items.append(type)
    return items

def get_compound_cols():
    items = []
    for type in set_species[TYPE_COL].unique():
        items.append(type)
    return items

# sample_species = {
#     "A": {CONCENTRATION_KEY: "0.0"},
#     "NO2": {CONCENTRATION_KEY: "3.1"},
#     "C": {CONCENTRATION_KEY: "5.2"}
# }
# print(rand_species)
# print(randomize_concentrations(sample_species))
# print(set_concentrations(sample_species))
# print(sample_species)

# To do:
# * Try to include compatability with powers of 10. (May need additional column)
# * Confirm that a configuration file is created.
# * Start on graphing?
# * Look up String.format
# * Convert between ppm / ppb and molecules / cm^3\
# * Look into CAMP