from sys import argv # import argument argv
from os.path import exists #import another command exists

script, from_file, to_file = argv # defining what argv is/willdo/how many arguments it needs to unpack

print(f"Copying from {from_file}, {to_file}") #using format & print to embed the files i will call in ps.

#we could do these tow on one line, how?
in_file = open(from_file) #defining what in_file will do(open from file called in arg in ps)
indata = in_file.read()  # telling indata to read in_file

print(f"The input file is {len(indata)} bytes long") #using format to read the length of the indata command/reaad the in_file.

print(f"Does the output file exist?{exists(to_file)}") # using boolean values with formatting to ask if the file exists, it comes out true becuase it does i think
print("Ready, hit RETURN to continue,Ctrl-C to abort.") # using input to see if you want to continue?
input() # asking user to enter ctrl c or enter

out_file = open(to_file, 'w') # definign out_file to open the file in write mode
out_file.write(indata) # writing to the file that we are reading

print("Alright, all done.")

out_file.close() # close the file
in_file.close # close the file
