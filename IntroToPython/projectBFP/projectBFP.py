from random import randint
'''
Created on Dec 10, 2021

@author: adavis25
'''

print ("let's print every number 0 + 20:") 
first_problem = 0
while first_problem <= 20:
    print (first_problem)
    first_problem += 1
    
    
print ("~~~~~~~~~~~~~~~~~")  
    
    
second_problem = input("enter a string: ")
while first_problem < len(second_problem):
    print (second_problem[first_problem])
    first_problem += 1
    
    
print ("~~~~~~~~~~~~~~~~~")


third_problem = input("enter another string: ").lower()
counter = 0
first_problem = 0
for i in third_problem:
    if third_problem[first_problem] == "a":
        counter += 1
        
if counter == 1:
    print("we found 1 a!")
elif counter > 1:
    print (f"we found {counter} a's!")
else:
    print ("we found no a's")

    
print ("~~~~~~~~~~~~~~~~~")

loop_count = 0
counter = 0
print ("doin' random stuff")
for i in range(0,20):
    random = randint(1,10)
    if random == 2:
        counter += 1
        
if counter == 1:
    print("there is a single 1!")
elif counter > 1:
    print (f"there is {counter} 1's!")
else:
    print ("there are no 1's")

    
print ("~~~~~~~~~~~~~~~~~")


fifth_problem = input("enter an integer: ")

while not fifth_problem.isdigit():
    print ("i said enter a digit you idiot! >:(")
    fifth_problem = input("try again: ")
    
fifth_problem = int(fifth_problem)
sum_varible = 0

for i in range(1, fifth_problem + 1):
    sum += i 
    
print (f"the sum of all numbers to {fifth_problem} is {sum}")
    
'''
https://www.youtube.com/watch?v=dQw4w9WgXcQ
'''