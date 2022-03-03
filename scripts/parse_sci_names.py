#### Shard Milne
#### 2022-03-02
#### A script to parse out the scientific names of plants from the USDA PLANTS database

# Needs to keep genus, species, "var"/variation names, "ssp"/subspecies names,
# Needs to remove author names and/or initials, remove "ex"

# First word is always the genus
# Second word, if lowercase, is species

def parse_sci_name(text):
	words = text.split(" ") # Generate a list of words in the text
	sci_name = '' # Empty string to receive sci name
	# print(words)
	i = 0
	while i < len(words):
		# print(words)
		# print(words[i])
		if i == 0: # The first word is ALWAYS the genus
			sci_name += words[i]
		elif words[i] == "ex" or words[i] == '': # This is the only lowercase word we want to exclude
			pass 
		elif words[i][0].islower() == True: # Every other lowercase word we want to keep
			sci_name += " " + words[i]
		i += 1
	# Thus we've excluded all the author names and kept only the sci name
	# print(words)
	# print(sci_name)
	return sci_name


### Examples! ###
# ex1 = "Abronia umbellata Lam. ssp. breviflora (Standl.) Munz"
# ex2 = "Acinos Mill."
# ex3 = "Achnatherum hendersonii (Vasey) Barkworth"
# ex4 = "Achillea millefolium L. ssp. occidentalis (DC.) Hyl."
# ex5 = "Stipa nelsonii Scribn. ssp. dorei Barkworth & Maze"
# ex6 = "Acer negundo L. ssp. interius (Britton) Á. Löve & D. Löve"
# ex7 = "Centaurea picris Pall. ex Willd."
# ex8 = "Allium geyeri S. Watson var. geyeri"

# parse_sci_name(ex1)
# parse_sci_name(ex2)
# parse_sci_name(ex3)
# parse_sci_name(ex4)
# parse_sci_name(ex5)
# parse_sci_name(ex6)
# parse_sci_name(ex7)
# parse_sci_name(ex8)


# Now we apply parse_sci_name to the whole USDA PLANTS database file, and output a new file that is the same with the addition of a column for clean scientific name

def get_sci_names(database_file, new_file):
	# Accepts the USDA plants database file (CSV), finds the sci name and adds it to a new column
	db = open(database_file, "r").read()
	db = db.replace('\"','') # Remove the quotation marks in the string
	db_lines = db.splitlines() # Get the database as a list of strings
	sci_names = ["Scientific Name"] # a list to put our sci names into
	i = 1 # Skip the header row
	while i < len(db_lines):
		# Get the scientific name from each line/row of the database
		line = db_lines[i].split(",")
		if len(line) > 1:
			sci_name = parse_sci_name(line[2])
			sci_names.append(sci_name)
		else:
			sci_names.append("")
		i += 1
	## Now write to a new file!
	with open(new_file, "w") as f:
		i = 0
		while i < len(db_lines):
			# Write the contents of db first
			f.write(db_lines[i])
			f.write(",")
			f.write(sci_names[i])
			f.write("\n")
			i += 1
	return sci_names

# def write_sci_names(database_file, sci_names, new_file):
# 	db = open(database_file, "r").readlines()
# 	# print(db[0:10])
# 	with open(new_file, "w") as f:
# 		i = 0
# 		while i < len(db):
# 			f.write(db[i].replace("\n",""))
# 			f.write(sci_names[i])
# 			f.write("\n")
# 			i += 1



wa_db = '../reference_lists/usda-plants-wa.csv'
new_wa_db = '../reference_lists/usda-plants-wa-CLEAN.csv'

national_db = "../reference_lists/usda-plants-completeChecklist.csv"
new_national_db = "../reference_lists/usda-plants-completeChecklist-CLEAN.csv"
get_sci_names(wa_db, new_wa_db)
get_sci_names(national_db, new_national_db)
