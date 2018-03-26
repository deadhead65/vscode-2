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

#how are you testing and debuggin these scripts? Are you testing line by line or just writing it all? 


#taking the variables the user input and spitting them back out 
#to answer the questions