import pandas as pd
import json
import csv
import re
from itertools import dropwhile
import os
import shutil
import zipfile
from multidict import MultiDict
from collections import defaultdict
import randomizer


# inputfile is converted to a csv file
# inputfile appears to be an excel file.
# output_file appears to be replaceable with csv_file_path.
inputfile='Basic_File.xlsx'
output_file = 'output.csv'
csv_file_path = 'output.csv'

# These store everything needed to create the config file.
# Will be generated based on the input file.
json_file_path = 'config/reactions.json'
json_file_path_2 = 'config/species.json'
json_file_path_3='config/config.json'
json_file_path_4='config/tolerance.json'

# These seem important for other parts of the reactions.
configfile='config/my_config_{num}.json'
max_config = 10
photofile='jan.photo'
CompletePhotolysis = 'config/CompletePhotolysis.csv'
photolysisfile = 'config/Photolysis.csv'

# Where the output config file will be stored.
base_dir = "config"
base_dir_1 = "config"


#Conversion of excel file to csv
input_file = pd.read_excel(inputfile)
input_file.to_csv(output_file, index=False)

#Conversion of csv file into json files
#Read csv file
with open(csv_file_path, newline='') as csvfile:
    data = list(csv.reader(csvfile))
    

    
# Initialize the base JSON structure
MEC_NAME = data[0][0]




json_data = {
    "camp-data": [
        {
            "name": MEC_NAME,
            "type": 'MECHANISM',
            "reactions": []
        }
    ]
}
musica=[]
reaction={}


# Parse the csv data
for row in data:
    if row and row[0].lower() == 'begin':
        if row[1] == "ARRHENIUS":
            print(row)
            A = float(row[row.index('!') + 1])
            Ea =float(row[-1])
            reaction = {
                "type": row[1],
                "A": A,
                "Ea": Ea,
                "reactants": {},
                "products": {},
                }
           
            reactants = row[2:5]
            products = row[5:row.index('!')]
            for r in reactants:
                if r:
                    if r in reaction['reactants']:
                        reaction['reactants'][r] = {'qty': 2}# checks if the string is not empty
                    elif r[0].isdigit():
                        if '.' in r:
                            if not r[3].isdigit():
                                qty = float(r[0:3])
                                reactant_name = r[3:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[4].isdigit():
                                qty = float(r[0:4])
                                reactant_name = r[4:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[5].isdigit():
                                qty = float(r[0:5])
                                reactant_name = r[5:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[6].isdigit():
                                qty = float(r[0:6])
                                reactant_name = r[6:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[7].isdigit():
                                qty = float(r[0:7])
                                reactant_name = r[7:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                        else:
                            if not r[1].isdigit():
                                qty = int(r[0:1])
                                reactant_name = r[1:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[2].isdigit():
                                qty = int(r[0:2])
                                reactant_name = r[2:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[3].isdigit():
                                qty = int(r[0:3])
                                reactant_name = r[3:]
                                reaction['reactants'][reactant_name] = {'qty': qty}   
                    else:
                        reaction['reactants'][r] = {}
                    
            for p in products:
                if p:
                    if p in reaction['products']:
                        reaction['products'][p] = {'yield': 2}# checks if the string is not empty
                    elif p[0].isdigit():
                        if '.' in p:
                            if not p[3].isdigit():
                                qty = float(p[0:3])
                                pro_name = p[3:]
                                reaction['products'][pro_name] = {'yield': qty}
                            elif not p[4].isdigit():
                                qty = float(p[0:4])
                                pro_name = p[4:]
                                reaction['products'][pro_name] = {'yield': qty}
                            elif not p[5].isdigit():
                                qty = float(p[0:5])
                                pro_name = p[5:]
                                reaction['products'][pro_name] = {'yield': qty}
                            elif not p[6].isdigit():
                                qty = float(p[0:6])
                                pro_name = p[6:]
                                reaction['products'][pro_name] = {'yield': qty}
                            elif not p[7].isdigit():
                                qty = float(p[0:7])
                                pro_name = p[7:]
                                reaction['products'][pro_name] = {'yield': qty}
                        else:
                            qty = int(p[0])
                            pro_name = p[1:]
                            reaction['products'][pro_name] = {'yield': qty}
   
                    else:
                        reaction['products'][p] = {}
                        products = [p for p in products if p != '']
                                        # checks if the string is not empty
                    
            json_data["camp-data"][0]["reactions"].append(reaction)
        
        
        elif row[1] == "PHOTOLYSIS":
            reaction = {
                "type": row[1],
                "reactants": {},
                "products": {},
                "MUSICA name": row[-1],
                }
            print(row)

            reactants = row[2:4]
            products = row[5:row.index('!')]
            for r in reactants:
                if r:
                    if r in reaction['reactants']:
                        reaction['reactants'][r] = {'qty': 2}# checks if the string is not empty
                    elif r[0].isdigit():
                        if '.' in r:
                            if not r[3].isdigit():
                                
                                qty = float(r[0:3])
                                
                                reactant_name = r[3:]
                               
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[4].isdigit():
                                
                                qty = float(r[0:4])
                                reactant_name = r[4:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[5].isdigit():
                               
                                qty = float(r[0:5])
                                reactant_name = r[5:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[6].isdigit():
                               
                                qty = float(r[0:6])
                                reactant_name = r[6:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[7].isdigit():
                               
                                qty = float(r[0:7])
                                reactant_name = r[7:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            

                                
                        else:
                            if not r[1].isdigit():
                                qty = int(r[0:1])
                                reactant_name = r[1:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[2].isdigit():
                                qty = int(r[0:2])
                                reactant_name = r[2:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
                            elif not r[3].isdigit():
                                qty = int(r[0:3])
                                reactant_name = r[3:]
                                reaction['reactants'][reactant_name] = {'qty': qty}
       
                    else:
                        reaction['reactants'][r] = {}
            for p in products:
                if p:
                    if p in reaction['products']:
                        reaction['products'][p] = {'yield': 2}# checks if the string is not empty
                    elif p[0].isdigit():
                        if '.' in p:
                            if not p[3].isdigit():
                                qty = float(p[0:3])
                                pro_name = p[3:]
                                reaction['products'][pro_name] = {'yield': qty}
                            elif not p[4].isdigit():
                                qty = float(p[0:4])
                                pro_name = p[4:]
                                reaction['products'][pro_name] = {'yield': qty}
                            elif not p[5].isdigit():
                                qty = float(p[0:5])
                                pro_name = p[5:]
                                reaction['products'][pro_name] = {'yield': qty}
                            elif not p[6].isdigit():
                                qty = float(p[0:6])
                                pro_name = p[6:]
                                reaction['products'][pro_name] = {'yield': qty}
                            elif not p[7].isdigit():
                                qty = float(p[0:7])
                                pro_name = p[7:]
                                reaction['products'][pro_name] = {'yield': qty}          
                        else:
                            qty = int(p[0])
                            pro_name = p[1:]
                            reaction['products'][pro_name] = {'yield': qty}         
                    else:
                        reaction['products'][p] = {}
                        products = [p for p in products if p != '']
                                        # checks if the string is not empty
                    
            json_data["camp-data"][0]["reactions"].append(reaction)
            print("its a photolysis reaction")
            
            musica.append(reaction["MUSICA name"])
        elif row[1] == "EMISSION":
            spec=[]
            for i in range(2,7):
                spec.append(row[i])
            spec = [r for r in spec if r != '']
            sc = float(row[-1])
            for item in spec:
                reaction = {
                    "type": row[1],
                    "species": item,
                    "scaling factor": sc,}
                json_data["camp-data"][0]["reactions"].append(reaction)
            
               
            
                
        elif row[1] == "FIRST_ORDER_LOSS":
            spec=[]
            for i in range(2,7):
                spec.append(row[i])
            spec = [r for r in spec if r != '']
            sc = float(row[-1])
            for item in spec:
                reaction = {
                    "type": row[1],
                    "species": item,
                    "scaling factor": sc,}
                json_data["camp-data"][0]["reactions"].append(reaction)
               
              
        elif row[1] == "WET_DEPOSITION":
            sc=float(row[-1])
            reaction = {
                "type": row[1],
                "aerosol phase" : "my aero phase",
                "scaling factor" : sc,
                }
            json_data["camp-data"][0]["reactions"].append(reaction)

        elif row[1] == "CMAQ_H2O2":
            k1_A= float(row[2])
            k1_B = float(row[3])
            k1_C=float(row[4])
            k2_A=float(row[5])
            k2_B=float(row[6])
            k2_C=float(row[7])
            time=row[8]
            reaction = {
                "type": row[1],
                "k1_A" :k1_A,
                "k1_B" :  k1_B,
                "k1_C" :  k1_C,
                "k2_A" :  k2_A,
                "k2_B" :  k2_B,
                "k2_C" :  k2_C,
                "time unit" : time,
                "reactants": {},
                "products":{}
                }
            reactants = row[9:12]
            products = row[12:row.index('!')]
            for r in reactants:
                if r:  # checks if the string is not empty
                    reaction['reactants'][r] = {}
                    reactants = [r for r in reactants if r != '']
          
            for p in products:
                if p:  # checks if the string is not empty
                    reaction['products'][p] = {}
                    products = [p for p in products if p != '']
            
            json_data["camp-data"][0]["reactions"].append(reaction) 

        elif row[1] == "CMAQ_OH_HNO3":
            k1_A = float(row[2])
            k1_B = float(row[3])
            k1_C=float(row[4])
            k2_A=float(row[5])
            k2_B=float(row[6])
            k2_C=float(row[7])
            k3_A=float(row[8])
            k3_B=float(row[9])
            k3_C=float(row[10])
            time=row[11]
            reaction = {
                "type": row[1],
                "k1_A" :  k1_A,
                "k1_B" :  k1_B,
                "k1_C" :  k1_C,
                "k2_A" :  k2_A,
                "k2_B" :  k2_B,
                "k2_C" :  k2_C,
                "k3_A" :  k3_A,
                "k3_B" :  k3_B,
                "k3_C" :  k3_C,
                "time unit" : time,
                "reactants": {},
                "products": {}
                }
            reactants = row[12:15]
            products = row[15:row.index('!')]
            for r in reactants:
                if r:  # checks if the string is not empty
                    reaction['reactants'][r] = {}
                    reactants = [r for r in reactants if r != '']
         
            for p in products:
                if p:  # checks if the string is not empty
                    reaction['products'][p] = {}
                    products = [p for p in products if p != '']
            
            json_data["camp-data"][0]["reactions"].append(reaction) 


        elif row[1] == "TROE":
            k0_A = float(row[2])
            k0_B = float(row[3])
            k0_C=float(row[4])
            kinf_A=float(row[5])
            kinf_B=float(row[6])
            kinf_C=float(row[7])
            Fc=float(row[8])
            N=float(row[9])
            time=row[10]
            reaction = {
                "type": row[1],
                "k0_A" :  k0_A,
                "k0_B" :  k0_B,
                "k0_C" :  k0_C,
                "kinf_A" :  kinf_A,
                "kinf_B" :  kinf_B,
                "kinf_C" :  kinf_C,
                "Fc" :  Fc,
                "N" :  N,
                "time unit" : time,
                "reactants": {},
                "products": {}
                }
            reactants = row[11:13]
            products = row[14:row.index('!')]
            for r in reactants:
                if r:  # checks if the string is not empty
                    reaction['reactants'][r] = {}
                    reactants = [r for r in reactants if r != '']
            for p in products:
                if p:  # checks if the string is not empty
                    reaction['products'][p] = {}
                    products = [p for p in products if p != '']
            json_data["camp-data"][0]["reactions"].append(reaction) 
 

# Write to JSON file
with open(json_file_path, 'w') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)
    print("Reaction.json File is Created Successfully")



# Read CSV file for creating species.json
with open(csv_file_path, newline='') as csvfile:
    data = list(csv.reader(csvfile))



# Initialize the base JSON structure
json_data = {
    "camp-data": [
        {
            "name": "M",
            "type": "CHEM_SPEC",
            "tracer type": "CONSTANT",
            "description": "Third-body molecule. This is any molecule present in the system."
        }
    ]
}

# List to keep track of already added species
added_species = []

# Parse the csv data
for row in data:
    if row and row[0].lower() == 'begin':
        if row[1] == "CMAQ_H2O2":
            species = row[9:row.index('!')]
            for s in species:
                if s != '' and s not in added_species and s != '%' and s != '$':
                    if s[0].isdigit():
                        added_species.append(s[1:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[1:]})
                    else:
                        added_species.append(s)
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s})

             
        elif row[1] == "CMAQ_OH_HNO3":
            species = row[12:row.index('!')]
            for s in species:
                if s != '' and s not in added_species and s != '%' and s != '$':
                    if s[0].isdigit():
                        added_species.append(s[1:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[1:]})
                    else:
                        added_species.append(s)
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s})

        elif row[1] == "TROE":
            species = row[11:row.index('!')]
            for s in species:
                if s != '' and s not in added_species and s != '%' and s != '$':
                    if s[0].isdigit():
                        added_species.append(s[1:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[1:]})
                    else:
                        added_species.append(s)
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s})
                   
        else:
            species = row[2:row.index('!')]
            local=[]
            for s in species:
                if s != '' and s not in added_species and s != '%' and s != '$':
                    if not s[0].isdigit() and s[0:] not in added_species:
                        local.append(s[0:])
                        added_species.append(s[0:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[0:]})
                    elif len(s) >= 3 and s[0].isdigit() and not s[1].isdigit() and s[1]!='.' and s[1:] not in added_species:
                      
                        local.append(s[1:])
                        added_species.append(s[1:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[1:]})                                 
                    elif len(s) >= 3 and s[0].isdigit() and s[1].isdigit() and s[1]!='.' and s[2:] not in added_species:
                     
                        local.append(s[2:])
                        added_species.append(s[2:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[2:]})                                            
                    elif len(s) >= 4 and s[2].isdigit() and s[1]!='.' and s[3:] not in added_species:
                       
                        local.append(s[3:])
                        added_species.append(s[3:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[3:]})
#floating condition
                    elif len(s) >= 4 and s[2].isdigit() and not s[3].isdigit()  and s[1]=='.' and s[3:] not in added_species:
                        local.append(s[3:])
                        added_species.append(s[3:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[3:]})
                    elif len(s) >=5 and not s[4].isdigit() and s[3].isdigit() and s[2].isdigit() and s[1]=='.' and s[4:] not in added_species:
                        
                        local.append(s[4:])
                        added_species.append(s[4:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[4:]})
                    elif len(s) >= 6 and not s[5].isdigit() and s[4].isdigit() and s[3].isdigit() and s[2].isdigit()  and s[1]=='.'  and s[5:] not in added_species:
                        local.append(s[5:])
                        added_species.append(s[5:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[5:]})
                    elif len(s) >= 7 and s[5].isdigit() and s[4].isdigit() and s[3].isdigit() and s[2].isdigit() and s[1]=='.' and s[6:] not in added_species:
                        local.append(s[6:])
                        added_species.append(s[6:])
                        json_data["camp-data"].append({"type": "CHEM_SPEC", "name": s[6:]})
                    


# Write to JSON file
with open(json_file_path_2, 'w') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)
    print("Species.json File is Created Successfully")





#MECHANISM FOR CREATING MY CONFIG FILE:
   
data = {
    "box model options": {
        "grid": "box",
        "chemistry time step [min]": 0.1,
        "output time step [min]": 6,
        "simulation length [hr]": 24
    },
    "chemical species": {},
    "environmental conditions": {
        "temperature": {
            "initial value [K]": 298.15
        },
        "pressure": {
            "initial value [Pa]": 101325.0
        }
    },
    "evolving conditions": {
        "Photolysis.csv": {
            "linear combinations": {}
        },
    },
    "initial conditions": {},
    "model components": [
        {
            "type": "CAMP",
            "configuration file": "camp_data/config.json",
            "override species": {
                "M": {
                    "mixing ratio mol mol-1": 1.0
                }
            },
            "suppress output": {
                "M": {}
            }
        }
    ]
}

for species in added_species:
    data['chemical species'][species] = {
        "initial value [molecule cm-3]": "0"
    }
    if species == 'O2':
        data['chemical species'][species]['initial value [molecule cm-3]'] = "5.25E+18"
    elif species == 'H2O':
        data['chemical species'][species]['initial value [molecule cm-3]'] = "2.5E+16"
    elif species == 'NO2':
        data['chemical species'][species]['initial value [molecule cm-3]'] = "250000000000"
    elif species == 'CO':
        data['chemical species'][species]['initial value [molecule cm-3]'] = "12500000000000"
    elif species == 'CH4':
        data['chemical species'][species]['initial value [molecule cm-3]'] = "37500000000000"
        

####
####

# Writing to file & Randomizing concentrations some number of times.
for i in range(0, max_config):
    with open(configfile.format(num=i), 'w') as f:
        randomizer.randomize_concentrations(data['chemical species'])
        json.dump(data, f, indent=4)





#MECHANISM FOR CONVERTING .PHOTO FILE TO CSV

# Open the data file
with open(photofile, 'r') as file:
    data = file.read()

# Find the start of the 'PHOTOLYSIS-DATA' block
start = data.find('PHOTOLYSIS-DATA')

# If 'PHOTOLYSIS-DATA' is not found, start from the beginning
if start == -1:
    start = 0

# Extract the data from 'PHOTOLYSIS-DATA' onward
data = data[start:]


# Split the data into blocks using '!' as the delimiter
blocks = data.split('!')

# Initialize a dictionary to hold the data
data_dict = {}

# Helper function to check if a string can be converted to a float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Iterate over the blocks
for block in blocks:
    # Split the block into lines
    lines = block.strip().split('\n')
    # The name of the measurement is on the first line
    name = lines[0].strip()
    # The data points are on the remaining lines
    data_points = []
    for line in lines[1:]:
        split_line = line.strip().split()
        # Check if all elements in split_line can be converted to floats
        if all(is_float(s) for s in split_line):
            data_points.extend([float(point) for point in split_line])
    # Add the data points to the dictionary
    data_dict[name] = data_points


#Removing extra keys
keys_to_remove = list(data_dict.keys())[:2]
for key in keys_to_remove:
    del data_dict[key]





# Create a new dictionary to store the updated key-value pairs
updated_data_dict = {}

# Get the keys from data_dict

keys = list(data_dict.keys())

for i in range(0, len(keys)):
    
    updated_key = "PHOT.j" + keys[i]  # Add a prefix "PHOT.jb" to the existing key
    value = data_dict[keys[i]]
    updated_data_dict[updated_key] = value

# FINDING MUSICA NAME IN KEYS'
newfile_keys = []
keys = list(updated_data_dict.keys())

for i in range(1, len(musica)):
    search_key = "PHOT." + musica[i]
    search_key_parts = search_key.split("->")
    search_key_parts = [part.strip() for part in search_key_parts]

    for key in keys:
        key_parts = key.split("->")
        key_parts = [part.strip() for part in key_parts]

        if search_key_parts == key_parts:
            newfile_keys.append(key)
            print("found: " + key)


data_dict = updated_data_dict


#Adding time,pressure,temperature values
items = list(data_dict.items())
time_values = [0] + [1800 * i for i in range(1, len(next(iter(data_dict.values()))))]
items.insert(0, ('time', time_values))
rep = len(next(iter(data_dict.values())))
items.insert(1, ('ENV.pressure', [101325]*rep))
items.insert(2, ('ENV.temperature', [298.15]*rep))
key_to_start = 'time'
data_dict = dict(dropwhile(lambda item: item[0] != key_to_start, data_dict.items()))
data_dict= dict(items)


#Writitng data to csv file

def write_dict_to_csv(dictionary, filename):
    headers = dictionary.keys()
    # Extract the values from the dictionary
    values = [[val / 60 for val in sublist] for sublist in dictionary.values()]
  
    # Find the maximum number of values for any key
    max_length = max(len(v) for v in values)
    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(headers)
        # Write each row individually
        for i in range(max_length):
            row = [v[i] if i < len(v) else "" for v in values]
            writer.writerow(row)



write_dict_to_csv(data_dict, CompletePhotolysis)


def write_dict_to_newcsv(dictionary, filename, keys_list):
    # Add 'time', 'ENV.pressure', and 'ENV.temperature' to keys_list if missing
    if 'time' not in keys_list:
        keys_list.insert(0, 'time')
    if 'ENV.pressure' not in keys_list:
        keys_list.insert(1, 'ENV.pressure')
    if 'ENV.temperature' not in keys_list:
        keys_list.insert(2, 'ENV.temperature')

    headers = keys_list
    # Extract the values from the dictionary based on the keys_list
    values = []
    rep=2
    for key in keys_list:
        if key == 'time':
            values.append([val / 60 for val in dictionary.get(key, [])])
        elif key == 'ENV.pressure':
            values.append([val / 60 for val in dictionary.get('ENV.pressure')])
           
        elif key == 'ENV.temperature':
            values.append([val / 60 for val in dictionary.get('ENV.temperature')])
        else:
            values.append([val / 60 for val in dictionary.get(key, [])])

   
    # Find the maximum number of values for any key
    max_length = max(len(v) for v in values)
    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(headers)
        # Write each row individually
        for i in range(max_length):
            row = [v[i] if i < len(v) else "" for v in values]
            writer.writerow(row)


write_dict_to_newcsv(data_dict, photolysisfile, newfile_keys)





#MECHANISM FOR CREATING A 2 OTHER FILES:

json_data = {
  "camp-files": [
    "camp_data/tolerance.json",
    "camp_data/species.json",
    "camp_data/reactions.json"
  ]
}

with open(json_file_path_3, 'w') as f:
    json.dump(json_data, f, indent=4)



json_data = {
  "camp-data": [
    {
      "type": "RELATIVE_TOLERANCE",
      "value": 0.0001
    }
  ]
}

# Writing to file
with open(json_file_path_4, 'w') as f:
    json.dump(json_data, f, indent=4)


dir_nam = os.path.join(base_dir, MEC_NAME )  # Assuming MEC_NAME is the name of the folder you want to create

# create directory
try:
    os.mkdir(dir_nam)
    dir_nam += '/config'
    os.mkdir(dir_nam)
except FileExistsError:
    print(f"The directory {dir_nam} already exists")

# List of files to be copied
json_files = [
    (configfile.format(num=i)) for i in range(0, max_config)
]
json_files.append(photolysisfile)

# Copy each file into the new directory
for file_path in json_files:
    # check if file exists
    if os.path.isfile(file_path):
        # copy file to new directory
        shutil.copy(file_path, dir_nam)
    else:
        print(f"The file {file_path} does not exist")



base_dir = dir_nam
name = 'camp_data'
dir_name = os.path.join(base_dir, name)

# create directory
try:
    os.mkdir(dir_name)
    os.mkdir(dir_nam)
except FileExistsError:
    print(f"The directory {dir_name} already exists")

# List of files to be copied
json_files = [
    json_file_path,
    json_file_path_2,
    json_file_path_3,
    json_file_path_4
]

# Copy each file into the new directory
for file_path in json_files:
    # check if file exists
    if os.path.isfile(file_path):
        # copy file to new directory
        shutil.copy(file_path, dir_name)
    else:
        print(f"The file {file_path} does not exist")


#MECHANISM FOR zipping

# dir_nam = os.path.join(base_dir_1, f"{MEC_NAME}") 

# # Specify the output ZIP file path
# output_zip_path = os.path.join(base_dir_1, f"{MEC_NAME}")  # Added '.zip' to the name
# print(dir_nam)
# shutil.make_archive(output_zip_path, format='zip', root_dir=dir_nam, base_dir='config')

'''
Below is outdated, use above if zipping is needed.
'''
# # Create a ZIP file and add the contents of the folder
# with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
#     # Walk through the directory and add all files and subdirectories to the ZIP file
#     for root, _, files in os.walk(dir_nam):
#         for file in files:
#             print(file)
#             print(dir_nam)
#             # Construct the file_path
#             file_path = os.path.join(root, file)
#             print(file_path)
#             # Construct the arcname, adjusting it to not duplicate MEC_NAME
#             arcname = os.path.relpath(file_path, base_dir)
#             print(arcname)
#             zipf.write(file_path, arcname)

# print(f"Folder '{dir_nam}' successfully zipped to '{output_zip_path}'.")