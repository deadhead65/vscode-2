print("""You enter a dark room and enter a door.""")
print("Choose a number")
door = input(" > ")

if door == "1":
    print("""You enter a dungeon, filled with dragons.
    You are a brave knight wielding a dex sword.
    As you are walking a orc approachs you, he gives you an odd look.""")

    print("""What do you do?
    1 Ask him where you are?
    2 Ask him if he speaks the common language of english?
    3 Attack!!!!""")

    orc = input(" > ") # when creating a value to input must use = 

    if orc == "1":
        print("The orc pulls out a club & knocks you out!")
    elif orc == "2":
        print("""The orc speaks orc tounge, you know nothing of what he says.
        He now looks angry and is charging at you.""")
    elif orc  == "3":
        print("""You chose to attack.
        you swing you're mighty sword but fail, missing him by inches.
        The orc looks at you with red fury in his eyes and stabs you in the heart.
        You are now dead.""")
    #it's here that the code stops, i don't know how to continue it, its supposed to continue so that if you chose option 1 it would branch into what i have written below, once i figure this out
    # it will continue on if you chose option 2 that will branch out if you chose option 3 it will branch out. But theres something obvious i am missing. 
    
    
    #How would "1."" ever be equal to one of the options above, which are all numbers and do not have a "."
if orc == "1": #Used to be   if orc == "1."  
    print(" ")
    print("You chose the first option continue on with this story line")
    print("")
    print("""You wake up in a dark cellear, there are a few things around you, A bowl filled with water, a plate for food & a broken brick.
    Do you choose a weapon or talk to the orc?:
        a. Choose to Talk.
        b. Choose a Weapon
    """)

    wordsOrWeapon = input (" > ")

    # Why would it be input here, should be wordsOrWeapon...
    if wordsOrWeapon == "a.": #Why the dot?
        print("""You have decided to talk to the orc, begging him for mercy 'Please Orc, I know not of what i have done or where i am
        this is all a misunderstanding please just let me go'/n
        the orc looks at you and laughs, punches you in the face and walks away""")
    else:
        print("""Choose your Weapon wisely.
            1. You grab the bowl drink the water and hide it behind you're back, calling the orc over you swing the bowl at him
            2. You grab the plate throwing it as a distraction.
            3. You grab the broken brick chucking it at him hoping to knock him out.
        """)
        status = input(" > ") #Will have to use a number with a "." in your text input to see == works.

        if status == "1.":
            print("""As the orc comes over to see why you called him over you ask him 'Why am i here?'/nThe orc laughs and starts to walk away./n as he walks away you hit him with the bowl
        the orc looks hurt but he does not get knocked out
        now the orc picks you up and drags you to the king...""")
        if status == "2.":
            print("You throw the plate catching the orc off guard, as he runs away from you're cell he immideatly drops the keys to the prison door...")
        elif status == "3.":
            print("You throw the brick succesfully hitting him in the head killing him,the only problem is he is still halfway across the room/n You cannot grab the key and die of starvation. No one else comes to check on you.")
        else: #You should always have an else to catch all incorrect inputs.
            print("You did not choose a valid option try again remember to use a '.' in this case")

elif orc=="2":     
    print("You selected orc option 2")

else: 
    print("Nothing correct was selected")
    
