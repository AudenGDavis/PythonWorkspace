x1 = int(input("enter the x value of the first point "))
y1 = int(input("enter the y value of the first point "))
x2 = int(input("enter the x value of the second point "))
y2 = int(input("enter the y value of the second point "))

xDiff = abs(x1 - x2)
yDiff  = abs(y1 - y2)
print ("the slope of the line that crosses the two points,  " + str(x1) +  ", " + str(y1) + " and, "  + str(x2) + ", " + str(y2) + ", is " + str(yDiff / xDiff))