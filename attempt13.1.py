from sys import argv
'''

Note: This program can't be executed through input console!

Normally if you don't use an IDE you run python like this:
    'cd Project_directory'
    On mac and linux:
    'python Filename.py'
    On windows:
    'python_version.exe filename.py'

As you may probably now, argv gets arguments from user within a script. To provide 
arguments you are required to run the code through command line. When the code is executed 
that way your first argument is your filename. More arguments can be added as such:
    'python_version.exe filename.py first_arg second_arg third_arg'


'''


'''
    # filename: String, gets file's name from the command line
    # first_arg: String, gets the first argument from user

'''
filename, first_arg, sec_arg, third_arg = argv

print("Your file name", filename)
print("Your first argument", first_arg)
print("Your second argument?", sec_arg)
print("Your third argument", third_arg)
