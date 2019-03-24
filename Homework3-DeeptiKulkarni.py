# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 05:59:19 2018
@author: Deepti Kulkarni 
"""

"""Exercise 1: Chapter 5, Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number."""

count=0
total=0

while True:
    try:
        number=input("Enter a number: ")
        
        if number=="done":
            break
        
        number=float(number)
        count=count+1
        total=total+number
            
    except:
         number=-1
         print("Error! Please enter numeric values only.")   
        
     
        
if count==0: 
    #if the first entry is "done", average is invalid, but printing it as zero
    average=0
else:
    average=total/count
    
print("Total is : ",total)
print("Count is: ",count)    
print("Average is: ",average)
    

"""Exercise 2, Chapter 5: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average."""

num_array= list()

while True:
    try:
        number=input("Enter a number: ")
        
        if number=="done":
            break
        
        num_array.append(float(number))
        
    except:
         number=-1
         print("Error! Please enter numeric values only.")   
        
    
print("Total is : ",sum(num_array))
print("Count is: ",len(num_array))

#Maximum and minimum of an empty array is invalid, but here printing max and min as zero if array is empty 

if num_array:
    print("Maximum number is: ",max(num_array))
    print("Minimum number is: ",min(num_array))
    
else:
    print("Maximum number is: ",0)
    print("Minimum number is: ",0)
    

    


""""Exercise 5: Chapter 6, Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number."""

str= 'X-DSPAM-Confidence:0.8475'

#Solution 1 

print("\n Solution 1 \n")
strfind= str.find(':')   # Finding ':' in the string 

DividedString= str[strfind+1:] # Dividing string from ':' till end of the string

print(DividedString,"Type is: ", type(DividedString))

CovertedStr= float(DividedString)       #Converting String to float 
print(CovertedStr, "Type is: ", type(CovertedStr))

#Solution 2 

print("\n Solution 2 \n") #Directly finding value only using 1 function 

DividedString1,DividedString2=str.rsplit(':',1)  #Spliting string directly 

ConvertedString2= float(DividedString2)    #Converting String to float 
print(ConvertedString2,"Type is: ", type(ConvertedString2),"\n")




"""Exercise 6:Chapter 6 Read the documentation of the string methods at
https://docs.python.org/library/stdtypes.html#string-methods You
might want to experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.
The documentation uses a syntax that might be confusing. For example,
in find(sub[, start[, end]]), the brackets indicate optional arguments.
So sub is required, but start is optional, and if you include start, then
end is optional."""

str1='Business Analytics-Python Language'

#Finding string 'ness' in str1 by giving 1 argument which gives index value of starting character in substring 
print("String Operations: ")
print(str1.find('ness'))  

#Finding string 'ness' in str1 by giving 3 arguments, which passes -1 value if substring not found in string within given argument

strfind2= str1.find('ness', 0, 6)  
print(strfind2)

#Finding string 'ness' in str1 by giving 2 arguments
strfind3= str1.find('ness',5)      
print(strfind3)

#Finding string 'ness' in str1 by giving 3 arguments, where last argument is length of string
strfind4= str1.find('ness',0,len(str))  
print(strfind4)

#Striping 'e' from string, strip() function can remove first and last space if no argument given 
#and can remove char if argument is passed, only from first and last index
print(str1.strip("e"))
print(str1.strip("e,B")) # Removing 2 characters which is passed in as 1 argument 

#Making first character capital and rest lower
str3='python business analytics'
print(str3.capitalize())

#Counting number of times particular character/word is repeated in the string
print(str1.count('s'))
print(str1.count('Business'))

#Making string upper case
print(str1.upper())

#Replacing character in the string with other character
print(str1.replace("e","o"))



"""
-----------SAMPLE OUTPUT------------------

-------Exercise 1: Chapter 5------

Enter a number: 1

Enter a number: 2

Enter a number: 7

Enter a number: ds
Error! Please enter numeric values only.

Enter a number: done
Total is :  10.0
Count is:  3
Average is:  3.3333333333333335

--------Exercise 2, Chapter 5-----

Enter a number: 1

Enter a number: 3

Enter a number: 7

Enter a number: done
Total is :  11.0
Count is:  3
Maximum number is:  7.0
Minimum number is:  1.0

--------Exercise 5: Chapter 6-----

0.8475 Type is:  <class 'str'>
0.8475 Type is:  <class 'float'>

 Solution 2 

0.8475 Type is:  <class 'float'> 

--------Exercise 6, Chapter 6-----

String Operations: 
4
-1
-1
4
Business Analytics-Python Languag
usiness Analytics-Python Languag
Python business analytics
4
1
BUSINESS ANALYTICS-PYTHON LANGUAGE
Businoss Analytics-Python Languago


"""