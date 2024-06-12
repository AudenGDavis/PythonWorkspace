from random import randint
'''
Created on Dec 14, 2021

@author: adavis25
'''
print ("welcome to the guess game!!!")
print ("~~~~~~~~~~")
while True:
    isbad = True
    thenum = randint(1, 20)
    userInput = 0
    guessnum = 0
    while thenum != userInput:
        guessnum += 1
        userInput = input("enter a number between 1 and 20 to guess: ")
        if userInput.isdigit():
            if int(userInput) <= 20 and int(userInput) >= 1:
                isbad = False
        while isbad: 
            print ("¥0U IDI0T, INVAL1D 1NPUT!!!!!!!!")    
            userInput = input("enter another number BETWEEN 1 and 20 >:( ")
            if userInput.isdigit():
                if int(userInput) <= 20 and int(userInput) >= 1:
                    isbad = False
        userInput = int(userInput)
        
        if userInput == thenum:
            if guessnum == 1:
                print ("you got it in 1 guess!")
            else:
                print (f"you got it, it took you {guessnum} guesses")
            print("lets do it again")
            print ("~~~~~~~~~~")
        elif userInput >= thenum:
            print ("that's too high")
        else:
            print ("that's to low")
            
    