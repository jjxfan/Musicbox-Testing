import pandas as pd
import random
import math

# For the file to specify ranges. FILE_NAME should be used for set concentrations,
# RANDOM_FILE_NAME for randomized concentrations 
FILE_NAME = 'concentration_ranges/concentration_ranges.csv'
RANDOM_FILE_NAME = 'concentration_ranges/random_concentration_ranges.csv' 

GENERAL_NAME_COL = 'general_name' # Name you would give the compound. (Ex. methane). Serves no real purpose.
CHEMICAL_NAME_COL = 'chemical_name' # The general chemical name. (Ex. CH4)
TYPE_COL = 'type' # The type of compound it is. (Ex. Organic Carbon, or RH.)
CONCENTRATION_COL = 'concentration' # The concentration, expressed in a number between 1 and 10. (ex. 2.34,
                                    # but not 0.000314)
MINIMUM_COL = 'min' # (RANDOM_FILE only) the minimum number of the random range the concentration can be.
MAXIMUM_COL = 'max' # (RANDOM_FILE only) the maximum number of the random range the concentration can be.
POW_10_COL = 'pow10' # The base power of 10 to apply to the number (ex. 13, so we get 2.34 * 10^13)

rand_species = pd.read_csv(RANDOM_FILE_NAME, index_col=False)
set_species = pd.read_csv(FILE_NAME, index_col=False)

# To modify apsects of the main configuration file
CONCENTRATION_KEY = 'initial value [molecule cm-3]'

CONVERSION_RATE = '?' # The conversion rate to use. (unfinished.)

# Randomizes the concentrations of the species present within the RANDOM_FILE.
# Species_data must be in a json-format; ideally, pass in the json data linked to 
# 'species'.
# Return a dictionary mapping the types of compounds we want to measure to their initial concentrations.
def randomize_concentrations(species_data):
    totals_of_randomized_species = {}
    for type in rand_species[TYPE_COL].unique():
        totals_of_randomized_species[type] = 0.0

    for index, row in rand_species.iterrows():
        species = row.loc[CHEMICAL_NAME_COL]
        pow10 = row.loc[POW_10_COL]
        init_conc = random.uniform(row.loc[MINIMUM_COL], row.loc[MAXIMUM_COL])
      
        # Adjust the power of 10.
        while (init_conc >= 10):
            init_conc /= 10
            pow10 += 1
        while (init_conc < 1):
            init_conc *= 10
            pow10 -= 1

        totals_of_randomized_species[row.loc[TYPE_COL]] += init_conc * math.pow(10, pow10)
        if (species not in species_data.keys()):
            species_data[species] = {CONCENTRATION_KEY: ''}
        species_data[species][CONCENTRATION_KEY] = '{conc:.2f}E{plus}{power}'.format(
                conc=init_conc, 
                plus= "+" if (pow10 > 0) else "",
                power=pow10)

    return totals_of_randomized_species

    
# Sets the concentrations of the species present within the FILE.
# Species_data must be in a json-format; ideally, pass in the json data linked to 
# 'species'.
# Return a dictionary mapping the types of compounds we want to measure to their initial concentrations.
def set_concentrations(species_data):
    totals_of_randomized_species = {}
    for type in set_species[TYPE_COL].unique():
        totals_of_randomized_species[type] = 0.0

    for index, row in set_species.iterrows():
        species = row.loc[CHEMICAL_NAME_COL]
        pow10 = row.loc[POW_10_COL]
        init_conc = row.loc[CONCENTRATION_COL]

        # Adjust the power of 10.
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

# Get the compounds present in the RANDOM_FILE.
def get_random_compound_cols():
    items = []
    for type in rand_species[TYPE_COL].unique():
        items.append(type)
    return items

# Get the compounds present in the FILE.
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