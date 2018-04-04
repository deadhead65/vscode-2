#ch = cheese, cr = cracker
def cheese_and_crackers(cheese_count, boxes_of_crackers): #def is defining a function, what's inside () is the arguments being passed to the new function
    print(f"You have {cheese_count} cheeses!") # print, format, embedded inside is cheese_count argument
    print(f"You have {boxes_of_crackers} boxs of crackers!") #print,format,embedded inside boxes_of_crackers argument

    print("Man that's enough for a party!")# print this everytime cheese or cracker arguemnt is ran
    print("Get a blanket.\n") # print this in a new line everytime cheese or cracker argument is ran 


print("We can just give the function numbers directly") # techincally the first (free) string without any arguments,formatting,definitons or input. 
cheese_and_crackers(20,30) # cheese_ crackers is a function and converts to int ch-20 , cr - 30 


print("OR, we can use variables from our script:") #taking values from previous code block?
amount_of_cheese = 10 # setting the variable to 10 
amount_of_crackers = 50 #setting the variable to 50/defining the arg

cheese_and_crackers(amount_of_cheese,amount_of_crackers) # using variables and arguments together. 


print("We can even do m ath inside too:") # print
cheese_and_crackers(10 + 20, 5 + 6) # defining the function cheese_and_crackers(10+ 20, 5 + 6)


print("And we combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #remember amount_of cheese = 10, amount_of_crackers = 50 cheese _and_crackers = whatever cheeese & crackers are defined


