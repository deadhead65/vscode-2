print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(" > ")

if door == "1":
    print("""You enter a dungeon, filled with dragons.
    You are a brave knight wielding a dex sword.
    As you are walking a orc approachs you, he gives you an odd look.
    What do you do?""")
    print("1.Ask him where you are?")
    print("2.Ask him if he speaks the common language of english.")
    print("3.Attack!!!!")

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
    
if orc == "1.":
    print("If you decided to choose option 1 or option 2  congradulations! You aren't dead.")
    print("If you chose the first option continue on with this story line")
    print("""You wake up in a dark cellear, there are a few things around you, A bowl filled with water, a plate for food & a broken brick,
    Which do you choose as a weapon?Do you choose a weapon or talk to the orc?:""")
    words = input (" > ")
    print("a. You call the orc prison guard over and beg for mercy")
    if input == "a.":
        print("""You have decided to talk to the orc, begging him for mercy 'Please Orc, I know not of what i have done or where i am
        this is all a misunderstanding please just let me go'/n
        the orc looks at you and laughs, punches you in the face and walks away""")
    status = input(" > ")
    print("1 you grab the bowl drink the water and hide it behind you're back, calling the orc over you swing the bowl at him")
    print("2. You grab the plate throwing it as a distraction.")
    print("3. You grab the broken brick chucking it at him hoping to knock him out.")
    if status == "1.":
        print("""As the orc comes over to see why you called him over you ask him 'Why am i here?'/nThe orc laughs and starts to walk away./n as he walks away you hit him with the bowl
    the orc looks hurt but he does not get knocked out
    now the orc picks you up and drags you to the king...""")
    if status == "2.":
        print("You throw the plate catching the orc off guard, as he runs away from you're cell he immideatly drops the keys to the prison door...")
    elif status == "3.":
        print("You throw the brick succesfully hitting him in the head killing him,the only problem is he is still halfway across the room/n You cannot grab the key and die of starvation. No one else comes to check on you.")


    


    
