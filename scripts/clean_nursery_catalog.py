### Shard Milne
### 2022-03-01
### A script which recieves a "messy" nursery plant catalog and
### outputs a "clean" list containing all scientific names

import sys

### Take command-line arguments
reference_file = sys.argv[1]
messy_file = sys.argv[2]
# reference_file = './wa-flora-scinames.csv'
# messy_file = './PNW Nursery Catalogs - Burnt Ridge Nursery.csv'
clean_file = messy_file[:-4] + "-CLEAN" + messy_file[-4:] # Add 'CLEAN' suffix before file type
# print(clean_file)



# Clean nursery catalogs by scientific name
# 1. Start with a complete native species list, and a messy list for a nursery
# 2. For each native plant species name, search the messy list for the scientific name. Add to clean list.
# 3. Export clean list.

def read_file_to_string(filename):
	# Reads in a file and returns a single text string of the file contents
	contents = open(filename).read()
	#print(contents)
	return contents

def compare_and_clean(reference_list, messy_text):
	# Takes a reference list of plant names and a "messy" string,
	# and outputs a list containing the taxa which appeared in the string and the list
	clean_list = []
	for species in reference_list:
		if species in messy_text:
			clean_list.append(species)
			# print(species)
	return clean_list

def write_list_to_file(clean_list, filename):
	# Takes a list and writes to a file, with each item on a new line
	with open(filename, 'w') as f:
		for item in clean_list:
			f.write(item)
			f.write("\n")


######

######
# Get a string for all species in WA, split into a list
wa_species_list = read_file_to_string(reference_file).splitlines()
# print(wa_species_list)

# Get a single string containing the nursery catalog
messy_catalog = read_file_to_string(messy_file)


clean_catalog = compare_and_clean(wa_species_list, messy_catalog)
# print("***")
# print(clean_catalog)


write_list_to_file(clean_catalog, clean_file)

print("Output saved to ", clean_file)
