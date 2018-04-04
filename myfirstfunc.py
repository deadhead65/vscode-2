from os.path import exists
def object(music , lamp):
    print(f'You have  {lamp},  lava{lamp} & i have {music} on')
    print("Does it work?")
    print(f"Is the music on? {exists(music)}")
    print(f"Boy i sure like you\'re {music}\n")

print("First Free string let's see what we can do here.")

music = ('Google Play')
lamp = ("Electricity/Light")
bills = int(10 + 20)
music_lamp = bills
print(f"This is roughly how much {music} & {lamp} cost me per month.\n{music_lamp}.00")


print("Where is that light coming from?", end = ' ')
lamp = input()

print(f"Ooh {lamp} sorry didn't know you were home haha.\nThank's for turning it on for me.")
print("Close it all down now. Thanks for visitng, much work to do.\nbye bye now.")
