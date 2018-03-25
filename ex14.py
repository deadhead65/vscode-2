from sys import argv  # importing argv from sys

script, user_name = argv # definig arguments?
prompt = '> ' # defining prompt hmm

print(f"Hi {user_name}, I'm the {script} script.") #using script arg
print("I'd like to ask you a few questions.") 
print(f"Do you like me {user_name}?") 
likes = input(prompt) # setting the input

print(f"Where do you live{user_name}?") 
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
#taking the variables the user input and spitting them back out 
#to answer the questions
