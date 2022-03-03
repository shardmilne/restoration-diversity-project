### Shard Milne
### 2022-03-01
### A script which recieves a "messy" nursery plant catalog and
### outputs a "clean" list containing all scientific names

import sys





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
		if species.lower() in messy_text.lower():
			if species not in clean_list:
				clean_list.append(species)
				# print(species)
	return clean_list

def write_list_to_file(clean_list, filename):
	# Takes a list and writes to a file, with each item on a new line
	with open(filename, 'w') as f:
		for item in clean_list:
			f.write(item)
			f.write("\n")

def get_column(filename, colname):
	# Given a QUOTE delimited file and a column header, outputs a list with the column contents
	f = open(filename, "r").read()
	f_lines = f.splitlines() # Get the database as a list of strings
	i = 0
	while i < len(f_lines):
		f_lines[i] = f_lines[i].split('"')[1::2] # separate by capturing things BETWEEN quotation marks
		i += 1
	# Now we have a nice table (list of lists) to work with
	i = 0
	while i < len(f_lines[0]):
		if f_lines[0][i] == colname:
			# print("Found!")
			break
		else:
			# print("Not found, searching...")
			i += 1
	# print(f_lines)
	# print(len(f_lines))
	# print(len(f_lines[0]))
	# print(i)
	col = []
	for line in f_lines:
		if len(line) >= i:
			col.append(line[i])
		else:
			col.append("")
		# Add the ith element of each line to col
	return col
######
# Manually enter arguments
# input_db = "../reference_lists/usda-plants-completeChecklist-CLEAN.csv"
# desired_colname = "Scientific Name"
# messy_file = "../nursery_catalogs/PNWNurseryCatalogs-BurntRidgeNursery.csv"
# clean_filename = messy_file[:-4] + "-" + input_db.split("/")[-1][:-4] + "-CLEAN.csv"


### Take command-line arguments
input_db = sys.argv[1]
desired_colname = sys.argv[2]
messy_files = sys.argv[3:]
# messy_files = open('./nurseries_to_process.txt',"r").read()
# messy_files = messy_files.splitlines()

for messy_file in messy_files:
	clean_filename = messy_file[:-4] + "-" + input_db.split("/")[-1][:-4] + "-CLEAN.csv"
	# print(clean_file)


	print(clean_filename)
	# Run it!!
	# use get_column to extract the scientific names
	complete_species_list = get_column(input_db, desired_colname)
	# use read file to string to get messy nursery list
	messy_catalog = read_file_to_string(messy_file)
	# use compare and clean to get the CLEAN nursery plant list
	clean_catalog = compare_and_clean(complete_species_list, messy_catalog)
	# write list to file
	write_list_to_file(clean_catalog, clean_filename)