#Question1

#Write Python code to calculate: 
# a. 15 divided by 4 
# b. The remainder when 17 is divided by 3 
# c. 53

x = 15
y= 4
remainder = x%y
print(f"15/4 = {remiander}")
print(f"Remainder/3= " , remainder%3)
print("5 cubed is: ",  5*5*5)

#Question2

# Look at the values below and identify their type (use lines of code to show you ach type): 
# a. 42 
# b. 3.14159 
# c. “Hello World”

num = 42
num1 = 3.14159
char = "Hello World!"
print(type(num))
print(type(num1))
print(type(char))

#Question3

# Write lines of code to store your first name in one variable and your last name in another variable, combine then into a full name and print.

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print(f"Full name is: {first_name} {last_name}")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
full_name = first_name+last_name
print(f"Full name is: {full_name}")

#Question4

# Write a program that: 
# a. Stores your age in a variable. 
# b. Stores the current year in another variable. 
# c. Calculates what year you will turn 100. 
# d. Prints the result. 

current_age = int(input("Enter current age: "))
current_year = int(input("Enter current year: "))
ageinhun = current_age+100
yearinhun = current_year+100
print(f"Your age in 100 years ({yearinhun}) will be {ageinhun} ")

#Question5

# Ask the user for their favourite colour. Print their favourite colour.

color = input("Enter fav color: ")
print(color)

#Question6

# Print how many letters are in that colour word.

print(len(color))

#Question7

# The variable height = “2.453” is a string. Convert it to a float and multiply it by 2 and print the result.

height = 2.452
answer = float(height)*2
print(answer)

#Question8

# Given that is_monday = True and is_sunny = False predict what each will 
# output: 
# a. Print(is_monday and is_sunny) 
# b. print(is_monday or is_sunny) 
# c. print(not is_sunny) 

is_monday = True
is_sunny = False
print(is_monday and is_sunny)
print(is_monday or is_sunny)
print(not is_monday)

#Question9

# Write Python code that compares two numbers x = 12 and y = 8. Check and print 
# whether: 
# a. x is greater than y 
# b. x is equal to y 
# c. x is less than or equal to 25

x = 12
y = 8
print("x is greater than y", x>y)
print("x is equal to y", x==y)
print("x is less than or equal to 25", x<=25)

#Question 10

# Write the code that asks the user for their name and age and prints it as 
# follows (where Jack is the name inputted and age is the age inputted): 
# Hello Jack, you are 21 years old. 
# a. Print whether their age is older than 18.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name} , you are {age} years old")
print("Are you older than 18: ", age>18)

#Question 11

# Write the code using ONE print() to produce the following: 
# Humpty Dumpty sat on a wall 
# Humpty Dumpty had a GREAT fall 
# All the kings horses and all the kings men 
# Couldn’t put Humpty together again!!! 

print("Humpty Dumpty sat on a wall \nHumpty Dumpty had a great fall \nAll the kings horses and all the kings men \nCouldn’t put Humpty together again!!!")

#Question 12

# Using the print() write the code that asks for the user’s first 
# name, like John, and prints it out in a single line, twice, so that 
# there is an exclamation mark at the beginning, in between the name, and 
# at the end, like this: 
# !John!John!

name = input("Enter name: ")
print(f"!{name}!{name}!")

#or

name = input("What is your name?")
pattern = "!"+name
print(f"{pattern * 2}!") #repeat the pattern twice


#Question 13

# Fix this code so that the whole calculation, complete with the 
# result is printed on a single line. Do not change the number of print 
# commands. 
# print(10) 
# print(“ + “) 
# print(8) 
# print(“ – “) 
# print(5) 
# print(“ = “) 
# print( 10 + 8 – 5)

print("10" , end="") #, end = "" means that dont start at a new line, by default at the end of the print is \n = new line
print("+", end="") 
print("8", end="") 
print("-", end="") 
print("5", end="") 
print("=",end= "") 
print(10+8-5)

#Question 14

# Write Python code that calculates and prints the BMI (body mass 
# index) for a person, given their weight and height as variables. 
# Display the result as rounded to 2 decimal places. Play around with a 
# variety of different ways to print(), use f-strings, .format(), etc. 
# Wight: 70kg 
# Height: 1.75m 
# BMI: 22.86 

height = float(input("Enter your height in meter: "))
weight = float(input("Enter your weight in kg: "))
BMI = float(weight%(height**2))
print("Your BMI is", round(BMI, 2))
print(f"Your height is {height:.2f} and your weight is {weight:.2f}", end =" ")
print("and Your BMI is {:.2f}" .format (BMI)) #:.2f means to show and round up to 2 decimal places

#Question 15

# Your friend is working on an app for jobseekers. She sends you this 
# bit of code (see code in jobseekers.py). The code is almost correct, 
# please fix the code so that it looks as follows: 
# my name is Henry Jones, I am 20 years old 
# my skills are 
# - python (beginner) - java (veteran) - programming (semiprofessional) 
# I am looking for a job with a salary of 2000-3000 pounds per month

name = "Henry Jones"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is ", name, " , I am ", age, "years old")
print("my skills are")
print("- ", skill1, " (", level1, ")")
print("- ", skill2, " (", level2, ")" , end= " ")
print("- ", skill3, " (", level3, " )")
print("I am looking for a job with a salary of", lower, "-", "pounds per month")
