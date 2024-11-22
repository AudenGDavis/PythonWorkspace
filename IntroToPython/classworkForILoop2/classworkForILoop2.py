'''
Created on Dec 16, 2021

@author: adavis25
'''

theNum = float(input("enter a positive number: "))
while theNum != int(theNum) or theNum <= 0:
    theNum = float(input("enter a positive number: "))
product = 1
theNum = int(theNum)
for i in range(1, theNum + 1):
    product = product * i
    
print (f"{theNum}! = {product}")