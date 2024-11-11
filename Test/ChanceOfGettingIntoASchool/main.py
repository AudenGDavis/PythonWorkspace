import random

sum = 0
iterations = 1000000000

for i in range(1, iterations + 1):
    
    if i % 1000000 == 0:
        print(str(i/1000000) + " Million Iterations")
    
    
    if random.randint(0,9) == 0 or random.randint(0,9) == 0 or random.randint(0,9) == 0 or random.randint(0,9) == 0:
        sum += 1
        
print("Average chance of getting into at least one school school: " + str(sum/iterations * 100) + "%")
