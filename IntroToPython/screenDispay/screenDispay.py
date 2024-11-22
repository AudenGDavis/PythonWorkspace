'''
Created on Sep 15, 2021

@author: adavis25
'''


def Array (X, Y):
    cal_num = 1
    row_num = 1
    line = ""
    for R in range(1, 11):
        for C in range (1, 31):
            if C == int(X) and R == int(Y):
                line = (line + "x")
            else: 
                line = (line + "_")
                cal_num += 1   
            
        print (line)
        line = ""  
        row_num += 1


print ("the maximum point us (30, 10)")
x_input = input("x?")
y_input = input("y?")
Array(x_input, y_input)
