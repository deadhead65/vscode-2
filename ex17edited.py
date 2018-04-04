from sys import argv
from os.path import exists # import argument argv

script, from_file, to_file = argv # defining what argv is/willdo/how many arguments it needs to unpack

in_file = open(from_file).read() # i believe if i eliminate indata i can just use in_file to open & read from_file in one line.

print(f"{len(in_file)}")

print(f"Does the output file exist? {exists(to_file)}") # using boolean values with formatting to ask if the file exists, it comes out true becuase it does i think

out_file = open(to_file, 'w')
out_file.write(in_file)

out_file.truncate()
out_file.close()
