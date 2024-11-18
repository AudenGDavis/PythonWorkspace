import random
import statistics as stats
import matplotlib.pyplot as plt


testResults = []
max = 10000
for s in range(1,max,10):
    # Series
    total = 0
    for t in range(s):
        
        total += count/100
    testResults.append(total/s)



    

plt.plot(range(1,max),testResults, label='Example Line')
plt.xlabel('Number of Trials')
plt.ylabel("Averge Result")
plt.title('Rule of Large Numbers')
# plt.legend()
plt.show()