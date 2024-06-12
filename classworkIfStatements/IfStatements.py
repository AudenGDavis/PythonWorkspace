'''
Created on Nov 16, 2021

@author: adavis25
'''
pwd = "marigold"


finish = False
while finish == False:
    guess = input("enter password: ")
    if pwd == guess:
        print ("Good Guess")
        finish = True
    else:
        print ("Nice Try")