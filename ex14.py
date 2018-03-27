from sys import argv  # importing argv from sys

script, user_name = argv # definig arguments?
prompt = '> ' # defining prompt hmm

# print(f"Hi {user_name}, I'm the {script} script.") #using script arg
print("Hi %s, I'm the %s script." %(user_name,script)) # %s means it is going ot be a string and %d is used for integers the format is print("something %d" %(yournumber))
print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
print("Do you like me %s" %(user_name))

#you must use raw_input and not input

likes = raw_input(prompt) # setting the raw_input

# print(f"Where do you live{user_name}?")
print("Where do you live %s" %(user_name))
lives = raw_input(prompt)

print("What kind of computer do you have?")
computer = raw_input(prompt)

# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}. Not sure where that is.
# And you have a {computer} computer. Nice.
# """)

print("""
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" %(likes,lives,computer))

#taking the variables the user raw_input and spitting them back out
#to answer the questions

# the arguments are defined by the users!
