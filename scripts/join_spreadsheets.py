
def read_file_as_table(filename, sep):
	f = open(filename, "r").read()
	f_lines = f.splitlines() # Get the database as a list of strings
	i = 0
	while i < len(f_lines):
		if sep == '\"':
			f_lines[i] = f_lines[i].split('"')[1::2] # separate by capturing things BETWEEN quotation marks
		elif sep == ",":
			f_lines[i] = f_lines[i].split(",")
		elif sep == "\t":
			f_lines[i] = f_lines[i].split("\t")
		i += 1
	# Now we have a nice table (list of lists) to work with
	return f_lines

def join_tables(table1, colname1, table2, colname2):
	# Matches the values in colname1 and colname2 and combines all the data into a new table
	colnum1 = find_column(table1, colname1)
	colnum2 = find_column(table2, colname2)
	joined = []
	joined.append(table1[0] + table2[0]) # add the headers as the first joined row
	# print(joined)
	i = 1
	while i < len(table1):
		# print(table1[i][colnum1])
		j = 1
		while j < len(table2):
			if table1[i][colnum1] == table2[j][colnum2]:
				newrow = table1[i] + table2[j]
				joined.append(newrow)
				# print(newrow)
			j += 1
		i += 1
	return joined

	# for each item in col1
	# if it matches an item in col2
	# then add that entire row from table1, and that entire row from table2


def find_column(table, colname):
	# Output the index with the desired colname
	i = 0
	while i < len(table[0]):
		# print(table[0])
		if table[0][i] == colname:
			return i
		else:
			i += 1
	print("Could not find", colname)
	return None


def write_table_to_file(table, filename):
	with open(filename, "w") as f:
		for row in table:
			for item in row:
				f.write(str(item))
				f.write("\t")

			f.write("\n")
	print("Written to", filename)


# ex1 = [["Col1","Col2","Col3"],[1,2,3],[4,5,6]]
# col1 = "Col1"
# ex2 = [["Col2", "Col1", "BLAH","TEST"],[1,2,3,4],["1","2","3","4"],[4,5,6,7]]
# col2 = "Col2"
# table12 = join_tables(ex1, col1, ex2, col2)
# print(table12)
# print(find_column(ex1,col1))

file1 = '../reference_lists/usda-plants-completeChecklist-CLEAN-by-nursery.csv'
colname1 = "Taxon Name"
file2 = '../reference_lists/wa-all-flora.txt'
colname2 = 'TaxonName'
outputfile = "../reference_lists/wa-all-flora-plants-by-nursery-CLEAN-joined-no-fungi.csv"

table1 = read_file_as_table(file1,"\t")
table2 = read_file_as_table(file2, "\t")
print(table2[0])
table1_2 = join_tables(table1, colname1, table2, colname2)
write_table_to_file(table1_2, outputfile)

# outputfile = "./test.csv"
# write_table_to_file(table12, outputfile)