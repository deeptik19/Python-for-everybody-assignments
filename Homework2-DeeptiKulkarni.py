# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:12:59 2018
@author: Deepti Kulkarni 
"""


"""Chapter 3, Exercise 2
Rewrite your pay program using try and except so that your program handles non-
numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the program. """


try:
    hours= float(input('Enter Hours: '))
    rate=float(input('Enter Rate: '))
    print('Pay: ',hours*rate)
    
except:
    hours=-1
    rate=-1
    print("Error! Please enter numeric values only.")


"""Chapter 3, Exercise 3
Write a program to prompt for a score between 0.0 and 1.0. If the score is out 
of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table: Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F """


try:
    score=float(input("Enter score between 0.0 and 1.0: "))
    if score>1.0 or score<0:
        print("Error! Please enter score between 0.0 and 1.0 only. ")
    elif score>=0.9:
        print("Grade is 'A'")
    elif score>=0.8:
        print("Grade is 'B'")
    elif score>=0.7:
        print("Grade is 'C'")
    elif score>=0.6:
        print("Grade is 'D'")
    else:
        print("Grade is 'F'")

except:
    score= -1
    print("Error! Please enter numeric values only.")   
    
    

"""Chapter 4, Exercise 6
Rewrite your pay computation with time-and-a-half for over-
time and create a function called computepay which takes two parameters
(hours and rate)."""

def computepay(hours,rate):
    
    if hours>40:
        overtime_rate=1.5*rate
        overtime_hours=hours-40
        overtime=overtime_hours*overtime_rate        
        pay=(40*rate)+overtime
    else:
        pay=hours*rate
    return pay

try:
    
    hours= float(input('Enter Hours: '))
    rate=float(input('Enter Rate: '))
    pay=computepay(hours,rate)
    
    print('Pay: ',pay)

except:
    score= -1
    print("Error! Please enter numeric values only.")   
    
    
"""Chapter 4, Exercise 7
Rewrite the grade program from the previous chapter using a function called 
computegrade that takes a score as its parameter and
returns a grade as a string."""

def computegrade(score):
    if score>=0.9:
        grade="A"
    elif score>=0.8:
        grade="B"
    elif score>=0.7:
        grade="C"
    elif score>=0.6:
        grade="D"
    else:
        grade="F"
    return grade
    
try:
    score=float(input("Enter score between 0.0 and 1.0: "))
    if score>1.0 or score<0:
        print("Error! Please enter score between 0.0 and 1.0 only. ")
    else:
        grade=computegrade(score)
        print("Grade is: ",grade)
    
except:
    score= -1
    print("Error! Please enter numeric values only.")   
    



"""
--------Sample Output(Chapter 3, Exercise 2)------------

Enter Hours: 12

Enter Rate: nine
Error! Please enter numeric values only.

Enter Hours: nine
Error! Please enter numeric values only.

--------Sample Output(Chapter 3, Exercise 3)------------

Enter score between 0.0 and 1.0: 2
Error! Please enter score between 0.0 and 1.0 only. 

Enter score between 0.0 and 1.0: nine
Error! Please enter numeric values only.

Enter score between 0.0 and 1.0: 0.99
Grade is 'A'

Enter score between 0.0 and 1.0: 0.77
Grade is 'C'

Enter score between 0.0 and 1.0: 0.66
Grade is 'D'

Enter score between 0.0 and 1.0: 0.5
Grade is 'F'

--------Sample Output(Chapter 4, Exercise 6)------------

Enter Hours: 45

Enter Rate: 10
Pay:  475.0

--------Sample Output(Chapter 4, Exercise 7)------------

Enter score between 0.0 and 1.0: 0.7
Grade is:  C

"""