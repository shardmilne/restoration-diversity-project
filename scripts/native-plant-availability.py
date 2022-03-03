#### Shard Milne
#### 2022-03-01
#### This script takes lists of plant species found at nurseries
#### and outputs a spreadsheet of all native plant species and which nursery offers them.

# Make a list of of native plants, listing which nurseries they can be purchased at
# 1. Start with a complete native species list, and a list for each nursery
# 2. For each nursery, for each plant, add to the native species list. Add name of the nursery, and change "available at a nursery?" to Y
# 3. For any plant NOT on the native species list, do nothing
# 4. Write it to a file!

import sys

def read_file_to_string(filename):
	# Reads in a file and returns a single text string of the file contents
	contents = open(filename).read()
	#print(contents)
	return contents

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

def write_list_to_file(clean_list, filename):
	# Takes a list and writes to a file, with each item on a new line
	with open(filename, 'w') as f:
		for item in clean_list:
			f.write(item)
			f.write("\n")

def get_nursery_name(filename):
	# Gets the nursery name from the filename, assuming my standard naming convention
	# PNWNurseryCatalogs-NameofNursery-NameofDatabase-CLEAN-CLEAN.csv
	return filename.split("-")[1]

# 1. Start with a complete native species list, and a list for each nursery
# 2. For each nursery, for each plant, add to the native species list. Add name of the nursery, and change "available at a nursery?" to Y
# 3. For any plant NOT on the native species list, do nothing
# 4. Write it to a file!

def make_plant_list_with_nursery_data(reference_list, nursery_lists):
	# reference_list = read_file_to_string(ref).splitlines()
	reference_dict = {}
	discard_bin = [] # here is where all of the taxa NOT found in the reference list will go
	# Key will be taxon name, value will be a list of [Available at Nursery?, Nursery Names]
	for taxon in reference_list:
		reference_dict[taxon] = [False, '']
	# print(reference_dict)
	for file in nursery_lists:
		# For each nursery, read in the plant list and get the name of the nursery
		nursery_plants = read_file_to_string(file).splitlines()
		nursery_name = get_nursery_name(file)
		# print(nursery_plants)
		# print(nursery_name)
		for taxon in nursery_plants:
			# For each taxon in the nursery list, find in the reference dictionary and add to it.
			if taxon in reference_dict:
				reference_dict[taxon][0] = True # Change available at nursery to True
				reference_dict[taxon][1] = reference_dict[taxon][1] + nursery_name + ", " # Add nursery name to entry
			else:
				if taxon not in discard_bin:
					discard_bin.append(taxon)
					print("Could not add", taxon)
					print(discard_bin)
			# print("Added", taxon)
		# print(reference_dict)
	return reference_dict, discard_bin

def add_percent_of_nurseries(ref_dict, nursery_lists):
	total_nurseries = float(len(nursery_lists))
	for taxon in ref_dict:
		nurseries = ref_dict[taxon][1].split(', ')
		# print(nurseries)
		num_nurseries = float(len(nurseries) - 1)
		# print(num_nurseries)
		# print(total_nurseries)
		# The ones with no nurseries have a count of 1 because of empty string.
		percent = round(num_nurseries/total_nurseries*100,2)
		# print(percent)
		ref_dict[taxon].append(percent)
		# print(ref_dict[taxon])
	return ref_dict


def write_reference_dict_to_file(ref_dict, filename):
	with open(filename, 'w') as f:
		# write a header
		f.write("Taxon Name\t")
		f.write("Available at Nursery?\t")
		f.write("Nurseries\t")
		f.write("Percent of Nurseries with this Taxon")
		f.write("\n")
		for key in ref_dict:
			f.write(key)
			f.write("\t")
			f.write(str(ref_dict[key][0]))
			f.write("\t")
			f.write(ref_dict[key][1])
			f.write("\t")
			f.write(str(ref_dict[key][2]))
			f.write("\n")
	print("Writing to", filename, "complete!")

def write_discards_to_file(discard_bin, discard_file):
	with open(discard_file, 'w') as f:
		for item in discard_bin:
			f.write(item)
			f.write("\n")
	print("Writing discarded taxa to", discard_file)

reference_file = sys.argv[1]
colname = sys.argv[2]
list_of_nursery_lists = sys.argv[3:]

# Name of output file to write to later
output_file = reference_file[:-4] + "-by-nursery" + reference_file[-4:]
discard_filename = reference_file[:-4] + "-discards" + reference_file[-4:]

reference_list = get_column(reference_file, colname)[1:] # Get the correct column, but remove the header

reference_dict, discards = make_plant_list_with_nursery_data(reference_list, list_of_nursery_lists)
reference_dict = add_percent_of_nurseries(reference_dict, list_of_nursery_lists)
write_reference_dict_to_file(reference_dict, output_file)
write_discards_to_file(discards, discard_filename)

# TODO: Check for logic/make sure the script is accurate
# What to do about genus names?
# What to do about species whose scientific names vary?
# Get more nursery records
# Think about how best to analyze/present these data - what questions to answer.

