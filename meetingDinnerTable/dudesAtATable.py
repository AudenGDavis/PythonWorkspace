'''
Created on Oct 19, 2021

@author: adavis25
'''


forkAB = True 
forkBC = True
forkCD = True
forkDE = True
forkEA = True

guyA = ["hungry", forkEA, forkAB]
guyB = ["hungry", forkAB, forkBC]
guyC = ["full", forkBC, forkCD]
guyD = ["hungry", forkCD, forkDE]
guyE = ["hungry", forkDE, forkEA]



def eat(guy):
    if guy[0] == "hungry":
        guy[1] = False
        guy[2] = False
        timer = input("press enter when the guy is finished eating")
        
eat(guyA)
eat(guyB)
eat(guyC)
eat(guyD)
eat(guyE)

