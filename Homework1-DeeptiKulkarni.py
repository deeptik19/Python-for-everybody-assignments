# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:50:12 2018

@author: Deepti Kulkarni.
"""

# Chapter 2: Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

x= float(input('Enter Hours: '))

y=float(input('Enter Rate: '))

print('Pay: ',x*y)


# Chapter 2:Exercise 5: Write a program which prompts the user for a Celsius temperature, 
#convert the temperature to Fahrenheit, and print out the converted temperature.

Celsius= float(input('Enter temperature in celsius: '))

Fahrenheit= Celsius*1.8+32

print('Temparature in Fahrenheit is:',Fahrenheit)

#Sample Output:
#
#Enter Hours: 2.3
#
#Enter Rate: 5.6
#Pay:  12.879999999999999
#
#Enter temperature in celsius: 3.9
#Temparature in Fahrenheit is: 39.019999999999996

#References: 
#1. Formula to convert to Fahrenheit, https://www.rapidtables.com/convert/temperature/how-celsius-to-fahrenheit.html
