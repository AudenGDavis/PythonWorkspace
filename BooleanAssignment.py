input1 = int(input("enter a number: "))
if input1 <= 20 and input1 >= 10:
    print ("between 10 and 20")
else:
    print  ("not between 10 and 20")


input2 = input("enter a word: ")
if len(input2) > 3 and len(input2) < 8:
    print ("word is good")
else:
    print ("word is not good")


input3 = input("enter another word: ")
matches = ['yes', 'no']
if not any(m == input3.lower() for m in matches):
    print ("neither one")

input4 = input("enter a word to check for a letter: ")
input5 = input("enter a letter: ")[0]
if input5 in input4:
    print ("your letter is in your word")
else:
    print ("your letter is not in your word")

input6 = input("enter a word: ").lower()
vowelList = ["a", "e", "i", "o", "u"]
if not any(c in vowelList for c in input6.lower()):
    print ("no vowels")
