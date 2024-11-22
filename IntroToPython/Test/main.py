import random
total = 0
iterations = 10000000
for i in range(0,iterations+1):
    sum = 0
    counter = 0 
    while sum < 12:
        num = random.randint(0,9)
        counter+=1
        if num < 3:
            sum += 1 
        elif num == 3:
            sum += 3
    total += counter
    
    if i % 1000000 == 0:
        print(str(int(i / 1000000)) + " million trials done")
    
    
print("Average Number of Throws: " + str(total/iterations))
