from random import randint 
'''
Created on Nov 30, 2021

@author: adavis25
'''
unpickedDoors = [1,2,3]

car = randint(1,3)


unpickedDoors.remove(car)


userpick = int(input("enter a door to pick: "))

if userpick in unpickedDoors:
    unpickedDoors.remove(userpick)


print ("a goat is behind door #" + str(unpickedDoors[randint(0,len(unpickedDoors)-1)]))

switchChoice = (input(f"say 'yes' to switch doors, say 'no' to stay: ")).lower()

if (switchChoice == "no" and car == userpick) or (switchChoice == "yes" and not car == userpick):
    print (f"the car has behind door #{car}")
    print ("you got the car!!!!!!!!!!!!!!!!!!!!!!")
elif (switchChoice == "yes" and car == userpick) or (switchChoice == "no" and not car == userpick):
    print (f"you got the goat, the car was in door #{car} :^(")
else:
    print ("Y0U 3R0KE TH3 PR0GR4M!!!1!!!")