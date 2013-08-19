#Author: Rahul Mohan
#Program: StudentGradeBook.py

class GradeBook:
    
    def __init__(self, name, coursename):
        
        self.name = name
        self.coursename = coursename
        
        self.testgrade = []
        self.testweight = 0
        self.homeworkweight = 0
        self.classworkweight = 0
        self.finalexamweight = 0
        self.homeworkgrade = []
        self.classworkgrade = []
        
        self.testavg = 0
        self.hwavg = 0
        self.classworkavg = 0
        self.finalexamgrade = 0
        self.finalgrade = 0
        self.gradeneeded = 0
        
    def course_weight(self, test_weight, hw_weight, classwork_weight, finalexam_weight):
        
        self.testweight = test_weight
        self.homeworkweight = hw_weight
        self.classworkweight = classwork_weight
        self.finalexamweight = finalexam_weight
        
        
        if ((hw_weight + classwork_weight + test_weight + finalexam_weight) != 1):
            raise Exception("The weights need to add up to 1!")
        else:
            print "Weight of Tests on Final Grade: " + str(test_weight)
            print "Weight of Homework on Final Grade: " + str(hw_weight)
            print "Weight of classworks on Final Grade: " + str(classwork_weight)
            print "Weight of final exam on Final Grade: " + str(finalexam_weight)
    
    def gradetopass(self, gradeneeded):
        if (gradeneeded > 1) or (gradeneeded < 0):
            raise Exception("The grade needs to be in the range 0 - 1")
        else:
            self.gradeneeded = gradeneeded
            print "The following grade is needed to pass the course: " + str((gradeneeded)*100) + "%" 
        
    def test(self,testscore): #input something like .85 (85 percent) 
        
        if (testscore > 1) or (testscore < 0):
            raise Exception("The score needs to be in the range 0 - 1")
        else:
            self.testgrade.append(testscore)
        
        self.testavg = (sum(self.testgrade) / len(self.testgrade))
        
        print "Current Test Average: " + str(self.testavg)
        
    def homework(self,hwscore): #input something like .85
    
        if (hwscore > 1) or (hwscore < 0):
            raise Exception("The score needs to be in the range 0 - 1")
        else:
            self.homeworkgrade.append(hwscore)
        
        self.hwavg = (sum(self.homeworkgrade) / len(self.homeworkgrade))
        print "Current Homework Average: " + str(self.hwavg)
        
    def classwork(self,classworkscore): #input something like .85
    
        if (classworkscore > 1) or (classworkscore < 0):
            raise Exception("The score needs to be in the range 0 - 1")
        else:
            self.classworkgrade.append(classworkscore)
        
        self.classworkavg = (sum(self.classworkgrade) / len(self.classworkgrade))
        print "Current Classwork Average: " + str(self.classworkavg)
    
    def finalexam(self,finalexamscore):
        
        if (finalexamscore > 1) or (finalexamscore < 0):
            raise Exception("The score needs to be in the range 0 - 1")
        else:
            self.finalexamgrade = finalexamscore
        
        print "Final Exam Score: " + str(self.finalexamgrade)
        
    def calculate_final_grade(self):
        
        self.finalgrade = (self.testweight * self.testavg) + (self.homeworkweight * self.hwavg) + (self.classworkweight * self.classworkavg) + (self.finalexamweight * self.finalexamgrade)
        
        
        if self.finalgrade > self.gradeneeded:
            print self.name + " has passed the course."
        else:
            print self.name + " has failed the course."

        print "Final Grade in " + self.coursename + ": " + str(self.finalgrade*100) + "%"
    
    
        
        
