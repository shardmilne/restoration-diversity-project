import sys, os

def remove_spaces_from_filename(filename):
	new_filename=filename.replace(" ","")
	print(new_filename)
	new_filename=new_filename.replace("&","and")
	print(new_filename)
	contents = open(filename).read()
	with open(new_filename, "w") as f:
		f.write(contents)
	print("Contents moved to ",new_filename)
	os.remove(filename)
	print(filename," deleted")

# remove_spaces_from_filename(sys.argv[1])

for item in sys.argv[1:]:
	remove_spaces_from_filename(item)