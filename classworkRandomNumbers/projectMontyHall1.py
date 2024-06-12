from random import randint 
'''
Created on Nov 30, 2021

@author: adavis25
'''

for I in range(1,5):
    car = randint(1,3)
    userpick = input("enter a door to pick (1-3): ")
    print ("car was behind door #" + str(car))
    print ("you picked door #" + str(userpick))
    print ()
    print ()