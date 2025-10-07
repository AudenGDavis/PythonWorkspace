from typing import Set

done: bool = False
while not done:
    monthStr: str = input("Please enter the month of your birthday as a integer (press return to escape)\n Your Birthday Month: ")
    
    while not monthStr.isdigit() or monthStr == "":
        print("Please enter a valid date")
        monthStr = input("Please enter the month of your birthday as a integer (press return to escape)\n Your Birthday Month: ")

    if monthStr == "":
        done = True
        continue

    dayStr: str = input("Please enter the month of your birthday as a integer (press return to escape)\n Your Birthday Month: ")
    
    while not monthStr.isdigit() or monthStr == "":
        print("Please enter a valid date")
        monthStr = input("Please enter the month of your birthday as a integer (press return to escape)\n Your Birthday Month: ")

    if monthStr == "":
        done = True
        continue

