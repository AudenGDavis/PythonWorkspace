'''
Created on Sep 3, 2021

@author: adavis25
'''
name = input("what's you name")
ave = float(input("what's the average number of hours you work per week"))
weeks = float(input("how many weeks to you work per year"))
rate = int(input("what's your hourly rate"))
salary = ave * weeks * rate
print ("your annual salary is " + str(salary))