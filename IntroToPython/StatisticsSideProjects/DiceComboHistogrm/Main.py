
import random as rand


iterations = 10000000
x=[0,0,0,0,0,0,0,0,0,0,0]#index 0 = 2
for i in range(iterations):
    num = rand.randrange(1,7)+rand.randrange(1,7)
    x[num-2] += 1
    
print(x)
for i in range(len(x)):
    print(str(i+2)+ ": " + str(x[i] / iterations * 100)+ "%")
