#### Shard Milne
#### 2022-03-02

# Extract interesting information from the cleaned, joined spreadsheet of WA plants and the nurseries which sell them.




import pandas as pd 

df = pd.read_csv('../reference_lists/wa-all-flora-plants-by-nursery-CLEAN-joined-no-fungi.csv', sep="\t")

print(df)

print(df["Taxon Name"]) # To display a column

df.set_index("Taxon Name", inplace = True) # Assign the Taxon Name column as the index for rows

print(df.loc["Abies"]) # Now I can look up a row using the Taxon Name

# 1. Create a spreadsheet with only NATIVE plants
print(df.loc["Abies","Origin"])
for item in df:
	print(item)
	if item["Origin"] == "Native":
		print(item)
# print(df["Origin"] == "Native")
# print((df["Origin"] == ""))

# 2. Create a new sheet showing all the plants which ARE available for purchase

# 3. Create a new sheet with all the plants which are NOT available for purchase

# Categorize plants by family?