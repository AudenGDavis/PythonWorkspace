'''
Created on Nov 5, 2020

@author: mellis
'''

'''
 * For each of the following questions, determine
 * what value is stored in the given variables when
 * the code snippet is done running.  Given a variable
 * called num, you will write its value in the String
 * variable called numAns.
 * 
 * Example:
 * 
 * var = 5;
 * var = var + 2;
 * 
 * 
 * varAns = "7";
 * 
''' 


#1

num1 = 17
num1 = num1 -5

num1Ans = ""


#2

doub1 = 4.5;
myInt1 = 5;

doub1 = doub1 + 2.0 * myInt1;
myInt1 = myInt1 -1;

doub1Ans = "";
myInt1Ans = "";

#3

doub2 = 6;

doub2 = doub2 *3;

doub2Ans = "";

#4

myInt2 = 5;
myInt3 = myInt2;

myInt2 = myInt3 + 6;

myInt2Ans = "";
myInt3Ans = "";


#5

myInt4 = 17;
myInt5 = 4;

myInt6 = myInt4 / myInt5;

myInt4Ans = "";
myInt5Ans = "";
myInt6Ans = "";

#6

first = "Computer";
second = "Science";

str1 = first + second;

str1Ans = "";

#7

doub3 = 21;
doub4 = doub3/2;

doub3 -=2;

doub3Ans = "";
doub4Ans = "";

#8

myInt7 = 4;
myInt8 = myInt7;

myInt7 *= 3;
myInt8 /= 2;

myInt7 = myInt8;

myInt7Ans = "";
myInt8Ans = "";


if num1Ans != str(num1):
    print("num1Ans incorrect")
if myInt1Ans != str(myInt1):
    print("myInt1 incorrect")
if myInt2Ans != str(myInt2):
    print("myInt2 incorrect")
if myInt3Ans != str(myInt3):
    print("myInt3 incorrect")
if myInt4Ans != str(myInt4):
    print("myInt4 incorrect")
if myInt5Ans != str(myInt5):
    print("myInt5 incorrect")
if myInt6Ans != str(myInt6):
    print("myInt6 incorrect")
if myInt7Ans != str(myInt7):
    print("myInt7 incorrect")
if doub1Ans != str(doub1):
    print("doub1 incorrect")
if doub2Ans != str(doub2):
    print("doub2 incorrect")
if doub3Ans != str(doub3):
    print("doub3 incorrect")
if doub4Ans != str(doub4):
    print("doub4 incorrect")
if str1Ans != str1:
    print("str1 incorrect")