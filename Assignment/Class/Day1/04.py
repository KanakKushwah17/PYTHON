'''Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage	Grade
90 and above	A
75 to 89	B
60 to 74	C
Below 60	D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B'''


class calculator():
    def __init__(self,rollno,stuname,m1,m2,m3):
        self.rollno=rollno
        self.stuname=stuname
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def total(self):
        self.total_marks=self.m1+self.m2+self.m3
    
    def percentage(self):
        self.per=self.total_marks/3

    def grade(self):
      if self.per >= 90:
           self.grade_stu = 'A'
      elif self.per >= 75:
           self.grade_stu = 'B'
      elif self.per >= 60:
           self.grade_stu = 'C'
      else:
           self.grade_stu = 'D'
        
    def display(self):
        print("------ Student Result ------")
        print("Roll Number      : ",self.rollno)
        print("Student Name     : ",self.stuname)
        print("Total Marks      : ",self.total_marks)
        print("Percentage       : ",self.per)
        print("Grade            : ",self.grade_stu)
        
rollno=int(input("Enter Roll number : "))
stuname=input("Enter Student name : ")
m1=int(input("enter marks"))      
m2=int(input("enter marks"))      
m3=int(input("enter marks"))      


C=calculator(rollno,stuname,m1,m2,m3)
C.total()
C.percentage()
C.grade()
C.display()