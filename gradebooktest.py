#Author: Rahul Mohan
#Program: gradebooktest.py

import StudentGradeBook #Assumes StudentGradeBook.py is in your working directory

studentlist = []

#Student #1:

Jim = StudentGradeBook.GradeBook('Jim','AP Biology')

print '\n'

Jim.course_weight(.4,.2,.2,.2) #Tests have 40% weight, the rest each have 20% weight on the final grade

Jim.gradetopass(.8) #Needs a 80% to pass the class

Jim.test(.97)
Jim.test(.92)
Jim.test(.84)
Jim.test(.89)
Jim.test(.91)

Jim.homework(.95)
Jim.homework(.97)
Jim.homework(.93)
Jim.homework(1)
Jim.homework(.88)
Jim.homework(.87)

Jim.classwork(.82)
Jim.classwork(.85)
Jim.classwork(.94)
Jim.classwork(.92)

Jim.finalexam(.85)

Jim.calculate_final_grade()

studentlist.append(Jim);

#Student #2:
    
print '\n'

Sally = StudentGradeBook.GradeBook('Sally','AP Biology')

Sally.course_weight(.4,.2,.2,.2) #Tests have 40% weight, the rest each have 20% weight on the final grade

Sally.gradetopass(.8) #Needs a 80% to pass the class

Sally.test(.97)
Sally.test(.92)
Sally.test(.91)
Sally.test(.98)
Sally.test(.91)

Sally.homework(.95)
Sally.homework(.97)
Sally.homework(.93)
Sally.homework(1)
Sally.homework(1)
Sally.homework(1)

Sally.classwork(.92)
Sally.classwork(.94)
Sally.classwork(.96)
Sally.classwork(.92)

Sally.finalexam(.95)

Sally.calculate_final_grade()

studentlist.append(Sally);

#Student #3:
    
print '\n'

Joe = StudentGradeBook.GradeBook('Joe','AP Biology')

Joe.course_weight(.4,.2,.2,.2) #Tests have 40% weight, the rest each have 20% weight on the final grade

Joe.gradetopass(.8) #Needs a 80% to pass the class

Joe.test(.76)
Joe.test(.82)
Joe.test(.81)
Joe.test(.75)
Joe.test(.83)

Joe.homework(.7)
Joe.homework(.7)
Joe.homework(.8)
Joe.homework(.74)
Joe.homework(.92)
Joe.homework(.85)

Joe.classwork(.8)
Joe.classwork(.75)
Joe.classwork(.81)
Joe.classwork(.86)

Joe.finalexam(.79)

Joe.calculate_final_grade()

studentlist.append(Joe);

print '\n'

#Create lookup dictionary of the students and their finalgrades

students = {}

for i in studentlist:
    students[i.name + ': ' + i.coursename] = i.finalgrade
    
print "Student-Course-Grade Hash Table:\n"
print students


