 # importing argv from sys
from sys import argv 

 # definig arguments?
script, user_name = argv
prompt = '> ' # defining prompt hmm

#using script arg
print("Hi {}, I'm the {} script.".format(user_name, script))
print("I'd like to ask you a few questions.") 
# you are printing the literal 
# string which is why the variable never gets
#  passed to the string. 

#here's another way
print("Do you like me "+user_name+" ?") 
likes = input(prompt) # setting the input

print("Where do you live {}?".format(user_name)) 
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("Alright, so you said {} about liking me. You live in {}. Not sure where that is. And you have a {} computer. Nice.".format(likes, lives, computer))

# I usually write it all and then head over to the debug console in vscode. 
#If something is not right i will look at the line it's bugging out at and start searching from there.
#sometimes its a problem on line 1 & it affects line 13 etc


#taking the variables the user input and spitting them back out 
#to answer the questions