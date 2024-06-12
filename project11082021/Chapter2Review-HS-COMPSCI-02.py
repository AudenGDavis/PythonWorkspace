'''
Created on Oct 4, 2019

@author: mellis
'''


'''
Be able to define each of the following terms and give examples:
Secondary storage
output device
CPU  (what does it do)
Main Memory
know what valid variable names are
be able to use the input function
'''
 
#what is the output of the type function for each of the following? 
#store your answer as a string in the given variable
type(1)
type1 = "<class int>"

type(1.0)
type2 = "<class float>"

type("1.0")
type3 = "<class str>"


#write a line of code which assigns the variable i its current value
#incremented by 5
i = 3


#increment i here

i = i + 5

#Given these variables, what is the result of each format function?
#store your answer as a string in the given variables
num = 12345.6789
my_str = "1234"
my_int = 17

format(num, '10.1f')
format1 = "   12345.7"

format(num, '<12.2f')
format2 = "12345.68    "

format(my_str, '10s')
format3 = "1234      "

format(num, '.4f')
format4 = "12345.6789"

format(my_str, '>10s')
format5 = "      1234"

format(my_int, '05d')
format6 = "017"

format(my_int, '<8d')
format7 = "170000"

format(num, '3.1f')
format8 = "12345.6"

#store the returned value in the string variable given
#11.0/2.0
ans1 = "4.5"

#11.0/2
ans2 = "5.5"

#11//2
ans3 = "5"

#11.0 // 2
ans4 = "5.0"

#11%2
ans5 = "1"

#11.0 % 2
ans6 = "1.0"

#11/2
ans7 = "5.5"


#Given the variable slice, write the returned value as a string 
#in each variable

slice = "Welcome to Great Valley"

slice[1:7]
slice1 = "elcome "

slice[10:]
slice2 = "Great Valley"

slice[:10] + "room 100"
slice3 = "Welcome to room 100"

slice[-4]
slice4= "l"

slice.upper()
slice5 = "WELCOME TO GREAT VALLEY"

#write a statement which would return the string "to Great" from slice
#write your statement in the "" in the following line
slice_statement = "slice[8:15]"


'''
Given the following variables and assignmenst write a statement
which will produce the following output

Account: 0001234 Name: Jimmy John      Balance:  37.50
Account: 0045678 Name: Sarah Joe Lee   Balance: 222.25
Account: 0000444 Name: Bob             Balance:   1.00
'''

#The given variables:
acc_num1 = 1234
acc_num2 = 45678
acc_num3 = 444

name1 = "Jimmy John"
name2 = "Sarah Joe Lee" 
name3 = "Bob"

balance1 = 37.5
balance2 = 222.25
balance3 = 1

#write your code here below this line.
print (f"account: {acc_num1} name: {name1} balance: ")
print ()
print ()




#write your code above this line.

if type1 != "<class int>":
    print("type1 incorrect")

if type2 != "<class float>":
    print("type2 incorrect")
if type3 != "<class str>":
    print("type3 incorrect")
if format1 != format(num, '10.1f'):
    print("format 1 incorrect")


if format2 != format(num, '<12.2f'):
    print("format2 incorrect")


if format3 != format(my_str, '10s'):
    print("format3 incorrect")


if format4 != format(num, '.4f'):
    print("format4 incorrect")
    
    


if format5 != format(my_str, '>10s'):
    print("format5 incorrect")


if format6 != format(my_int, '05d'):
    print("format6 incorrect")


if format7 != format(my_int, '<8d'):
    print("format7 incorrect")


if format8 != format(num, '3.1f'):
    print("format8 incorrect")
    


#store the returned value in the string variable given
#11.0/2.0
if ans1 != "5.5":
    print("ans1 incorrect")

#11.0/2
if ans2 != "5.5":
    print("ans2 incorrect")

#11//2
if ans3 != "5":
    print("ans3 incorrect")
#11.0 // 2
if ans4 != "5.0":
    print("ans4 incorrect")
#11%2
if ans5 != "1":
    print("ans5 incorrect")

#11.0 % 2
if ans6 != "1.0":
    print("ans6 incorrect")

#11/2
if ans7 != "5.5":
    print("ans7 incorrect")


#Given the variable slice, write the returned value as a string 
#in each variable

slice = "Welcome to Great Valley"

if slice1 != slice[1:7]:
    print("slice 1 incorrect")


if slice2 != slice[10:]:
    print("slice2 incorrect")

slice[:10] + "room 100"
if slice3 != slice[:10] + "room 100":
    print("slice 3 incorrect")

if slice4 != slice[-4]:
    print("slice 4 incorrect")

if slice5 != slice.upper():
    print("slice 5 incorrect")
#write a statement which would return the string "to Great" from slice
#write your statement in the "" in the following line
if slice_statement != "slice[8:16]":
    print("slice statement incorrect")


if i != 8:
    print("incremented i improperly")
    
print("check complete")




 
 
 