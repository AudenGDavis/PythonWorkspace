while True:
    grade = float(input("enter grade percent (no % sign): "))
    print ()
    if grade >= 90.0:
        print ("you get a A! :)")
    elif grade >= 80.0:
        print ("you get a B :)")
    elif grade >= 70: 
        print ("you get a C :|") 
    elif grade >= 60:
        print ("that's pretty bad, you get a D :|")
    else:
        print ("wow you're stupid, you get a F :(")
    print ()