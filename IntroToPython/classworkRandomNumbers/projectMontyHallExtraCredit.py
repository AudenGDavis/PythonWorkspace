import random
'''
Created on Dec 2, 2021

@author: adavis25
'''

hello = input("hello, welcome to our  game show, press enter to continue...")
unpickedDoors = [1,2,3]

car = random.randint(1,3)
unpickedDoors.remove(car)

print ('''
+---+ +---+ +---+
| 1 | | 2 | | 3 |
|  •| |  •| |  •|
|   | |   | |   |
+---+ +---+ +---+
''')


userpick = ""

while not userpick == 1 and not userpick == 2 and not userpick == 3:
    userpick = input("enter a door to pick: ")
    userpick = int(userpick) if userpick.isdigit() else ""


if userpick in unpickedDoors:
    unpickedDoors.remove(userpick)

revealedGoat = random.choice(unpickedDoors)
print ("a goat is behind door #" + str(revealedGoat))
unpickedDoors.remove(revealedGoat)

switchChoice = (input(f"say 'yes' to switch doors, say 'no' to stay: ")).lower()
while not switchChoice == "yes" and not switchChoice == "no": 
    switchChoice = (input(f"say 'yes' to switch doors, say 'no' to stay: ")).lower()

if (switchChoice == "no" and car == userpick) or (switchChoice == "yes" and not car == userpick):
    print (f"the car has behind door #{car}")
    print ("you got the car!!!!!!!!!!!!!!!!!!!!!!")
elif (switchChoice == "yes" and car == userpick) or (switchChoice == "no" and not car == userpick):
    print (f"you swapped and got the goat, the car was in door #{car} :^(")
else:
    print ("Y0U 3R0KE TH3 PR0GR4M!!!1!!!")