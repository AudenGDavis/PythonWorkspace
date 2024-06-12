''' 

Created on Oct 25, 2021 

  

@author: adavis25 

''' 

student_data = [] 

student_data.append(input("enter student first name")) 

student_data.append(input("enter student last name")) 

student_data.append(input("enter student address")) 

student_data.append(input("enter student phone number")) 

student_data.append(input("enter student grade")) 

  

  

def EnterGrade (): 

    assignment = input("enter new assignment name") 

    point_given = float(input("enter points given")) 

    point_total = float(input("enter total number of points")) 
    print (f"points earned {point_given}")
    print (f"total points {point_total}")

    return [assignment, point_given, point_total, str(point_given // point_total  * 100)] 

  

def PrintNum (score_list): 

    print (score_list[0] + " : " + score_list[3]) 

     

def PrintInfo (info_list): 

    print (info_list[0] + " " + info_list[1] + ", " + info_list[2]) 

    print ("grade " + info_list[4] + "  contact: " + info_list[3]) 

 

def PublishGrades (list1, list2, list3): 

    TotalPointsGiven = list1[1] + list2[1] + list3[1] 
    TotalPoints = float(list1[2]) + float(list2[2]) + float(list2[2])

    Average = TotalPointsGiven  // TotalPoints * 100 

    print (f"{list1[0]}: {list1[1]}  / {list1[2] } : {list1[3]}") 
    print (f"{list2[0]}: {list2[1]}  / {list2[2] } : {list2[3]}") 
    print (f"{list3[0]}: {list3[1]}  / {list3[2] } : {list3[3]}")

    # print ("points: " + str(TotalPointsGiven) + "/" + str(TotalPoints) + "average: " + Average) 
    print (f"points: {TotalPointsGiven}  / {TotalPoints} Average:  {Average}")
     

     

     

grade1 = EnterGrade() 

grade2 = EnterGrade() 

grade3 = EnterGrade() 

  

PrintInfo(student_data) 

PrintNum(grade1) 

PrintNum(grade2) 

PrintNum(grade3) 

PublishGrades(grade1, grade2, grade3) 