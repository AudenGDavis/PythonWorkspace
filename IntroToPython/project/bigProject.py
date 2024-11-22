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
    return [assignment, point_given, point_total, str(point_given // point_total)]

def PrintNum (score_list):
    print (score_list[0] + " : " + score_list[3])
    
def PrintInfo (info_list):
    print (info_list[0] + " " + info_list[1] + ", " + info_list[2])
    print ("grade " + info_list[4] + "  contact: " + info_list[3])
    
    
    
grade1 = EnterGrade()
grade2 = EnterGrade()
grade3 = EnterGrade()

PrintInfo(student_data)
PrintNum(grade1)
PrintNum(grade2)
PrintNum(grade3)