#### Shard Milne
#### 2022-03-01
#### This script takes lists of plant species found at nurseries
#### and outputs a spreadsheet of all native plant species and which nursery offers them.

# Make a list of of native plants, listing which nurseries they can be purchased at
# 1. Start with a complete native species list, and a list for each nursery
# 2. For each nursery, for each plant, add to the native species list. Add name of the nursery, and change "available at a nursery?" to Y
# 3. For any plant NOT on the native species list, do nothing
# 4. Write it to a file!

def read_file_to_string(filename):
	# Reads in a file and returns a single text string of the file contents
	contents = open(filename).read()
	#print(contents)
	return contents

def write_list_to_file(clean_list, filename):
	# Takes a list and writes to a file, with each item on a new line
	with open(filename, 'w') as f:
		for item in clean_list:
			f.write(item)
			f.write("\n")

def get_nursery_name(filename):
	# Gets the nursery name from the filename, assuming my standard naming convention
	# PNWNurseryCatalogs-NameofNursery-CLEAN.csv
	return filename.split("-")[1]

# 1. Start with a complete native species list, and a list for each nursery
reference_file = './wa-flora-scinames.csv'
list_of_nursery_lists = [
'./PNWNurseryCatalogs-BurntRidgeNursery-CLEAN.csv',
'./PNWNurseryCatalogs-CottageLakeGardens-CLEAN.csv',
'./PNWNurseryCatalogs-DerbyCanyonNatives-CLEAN.csv',
'./PNWNurseryCatalogs-FiretrailNursery-CLEAN.csv',
'./PNWNurseryCatalogs-FirRunNursery-CLEAN.csv',
'./PNWNurseryCatalogs-FourthCornerNursery-CLEAN.csv',
'./PNWNurseryCatalogs-HimaNursery-CLEAN.csv',
'./PNWNurseryCatalogs-IFANursery-CLEAN.csv',
'./PNWNurseryCatalogs-InsidePassageSeeds-CLEAN.csv',
'./PNWNurseryCatalogs-LandHSeeds-CLEAN.csv',
'./PNWNurseryCatalogs-NorthwestMeadowscapes-CLEAN.csv',
'./PNWNurseryCatalogs-OxbowFarmandConservationCenter-CLEAN.csv']

# Name of output file to write to later
output_file = reference_file[:-4] + "-by-nursery" + reference_file[-4:]

# 2. For each nursery, for each plant, add to the native species list. Add name of the nursery, and change "available at a nursery?" to Y
# 3. For any plant NOT on the native species list, do nothing
# 4. Write it to a file!

def make_plant_list_with_nursery_data(ref, nursery_lists):
	reference_list = read_file_to_string(ref).splitlines()
	reference_dict = {}
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
			reference_dict[taxon][0] = True # Change available at nursery to True
			reference_dict[taxon][1] = reference_dict[taxon][1] + nursery_name + ", " # Add nursery name to entry
			# print("Added", taxon)
		# print(reference_dict)
	return reference_dict

def add_percent_of_nurseries(ref_dict, nursery_lists):
	total_nurseries = float(len(nursery_lists))
	for taxon in ref_dict:
		nurseries = ref_dict[taxon][1].split(', ')
		print(nurseries)
		num_nurseries = float(len(nurseries) - 1)
		print(num_nurseries)
		print(total_nurseries)
		# The ones with no nurseries have a count of 1 because of empty string.
		percent = round(num_nurseries/total_nurseries*100,2)
		print(percent)
		ref_dict[taxon].append(percent)
		print(ref_dict[taxon])
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


reference_dict = make_plant_list_with_nursery_data(reference_file, list_of_nursery_lists)
reference_dict = add_percent_of_nurseries(reference_dict, list_of_nursery_lists)
write_reference_dict_to_file(reference_dict, output_file)

# TODO: Check for logic/make sure the script is accurate
# What to do about genus names?
# What to do about species whose scientific names vary?
# Get more nursery records
# Think about how best to analyze/present these data - what questions to answer.

