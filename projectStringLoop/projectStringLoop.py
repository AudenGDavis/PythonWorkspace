'''
Created on Dec 20, 2021

@author: adavis25
'''
while True:
    answer = input("enter a string: ").lower()
    while answer == "":
        answer = input("enter a string stupid, it can't be nothing >:( : ").lower()
    vowels = 0
    knownvowels = ["a", "e", "i", "o", "u"]
    vowelList = []
    for i in range(0,len(answer)):
        if answer[i] in knownvowels:
            vowels += 1
            vowelList.append(i)
    
    if vowels == 0:
        print("there are no vowels")
    elif vowels == 1:
        print("there is 1 vowel")
        print (f"it was found at index {vowelList}")
    else:
        print (f"there are {vowels} vowels")
        print (f"they were found at indexes {vowelList}")
    
    print ("~~~~~~~~~~~~~")