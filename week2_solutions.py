#Question 1

# Write a program which asks the user for an integer number. 
# The program should print “The war is over!!” if the number is 
# exactly 1945, otherwise do nothing.

year = int(input("Enter the year "))
if year == 1945:
    print("The war is over!")

#Question 2

# Write a program which asks the user for an integer number. If 
# the number is less than zero, the program should print out 
# the number multiplied by -1. Otherwise, the program prints 
# out the number as is. For example, if -9 is inputted then the 
# output should be 9. If 150 is inputted, then the output 
# should be 150. 

print("Negative number will be mutiplied with -1 and positive number will be as it is")
num= int(input("Enter a number: "))
if num <0:
    mulnum= num*-1
    print(f"The answer is: {mulnum}")
else:
    print(f"The answer is: {num}")

#Question 3

# Write program that asks the user for 2 numbers and an 
# operation. If the operation is add, multiply or subtract, the 
# program should calculate and print out the result of the 
# operation with the given numbers. If the user types anything 
# else, the program should print out nothing. For example, if 
# the numbers are 4 and 5 and the operation is add, then the 
# output should be as follows: 
# number 1: 4 
# number 2: 5 
# operation: add 
# 4 + 5 = 9

def operation(op):
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    match op:

        case 1:
            sum= num1+num2
            print(f"Sum= {sum}")

        case 2:
            sub= num1-num2
            print(f"Difference= {sub}")

        case 3:
            mul= num1*num2
            print(f"Result: {mul}")


print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
op = int(input("Select operation "))

if op == 1 or op==2 or op== 3:
    operation(op)
else:
    print("Invalid input")


#Question 4

# Write a program which asks for the hourly wage, hours worked 
# and the day of the week. The program should then print out 
# the daily wages, which equal hourly wage multiplied by hours 
# worked, except on Sundays when the hourly wage is double. The 
# output could look as follows: 
# hourly wage: 8.5 
# hours worked: 3 
# day of the week: Monday 
# daily wages: 25.5 pounds 
# hourly wage: 12.5 
# hours worked: 10 
# day of the week: Sunday 
# daily wages: 250.0 pounds

day = input("Enter the day: ")
hwa = float(input("Enter the hourly wage: "))
hwo = float(input("Enter the hours worked: "))

if day == "Monday" or day =="Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
   dw = hwa*hwo
   print(f"Hourly wag: {hwa}")
   print(f"Hours worked: {hwo}")
   print(f"Day: {day}")
   print(f"Daily wage is: {dw}")

elif day == "Sunday":
    dw1 = hwa*2
    print(f"Hourly wag: {hwa}")
    print(f"Day: {day}")
    print(f"Daily wage is doubled: {dw1}")

else:
    print("Incorrect day!")

#Question 5

# Write a program which asks for tomorrow’s weather forecast 
# and then suggests weather-appropriate clothing. The 
# suggestion should change if the temperature is over 20, 10 or 
# 5 degrees and if there is rain on the way. The output could 
# look as follows: 
# what is the weather forecast for tomorrow? 
# temperature: 21 
# will it rain (yes / no): no 
# wear jeans and a T 
# what is the weather forecast for tomorrow? 
# temperature: 10 
# will it rain (yes / no): no 
# wear jeans and a T 
# a jumper is recommended 
# what is the weather forecast for tomorrow? 
# temperature: 3 
# will it rain (yes / no): yes 
# wear jeans and a T 
# a jumper is recommended 
# take a warm coat 
# take an umbrella

print("Whats the weather forcast for tomorrow looking like?")
temp = int(input("Temperature in Celsius?: "))

def rain(rainfall):
    match rainfall:

        case "yes":
            print("carry umbrella")
        case "no":
            print("a jumper is recommended")

if temp > 20:
    rainfall = input("Will it rain? ")
    rain(rainfall)
    print("Wear jeans and T")

elif temp > 10:
    rainfall = input("Will it rain? ")
    rain(rainfall)
    print("Wear jeans and T")

elif temp > 5:
    rainfall = input("Will it rain? ")
    rain(rainfall)
    print("Wear jeans and T")

else:
    rainfall = input("Will it rain? ")
    rain(rainfall)
    print("take a warm coat")

#Question 6

# Write a program to produce a grade calculator. Ask the user 
# to ender a grade (0 to 100). Print the grade as follows: 
# A -> 70+ 
# B 
# C 
# D -> 60 to 69 -> 50 to 59 -> 40 to 49 
# Fail -> under 40

gradenum = int(input("Enter the grade: "))

if gradenum >= 70:
    print("A")

elif 60 <= gradenum <= 69:
    print("B")

elif 50 <= gradenum <= 59:
    print("C")

elif 40 <= gradenum <= 49:
    print("D")

else:
    print("Fail")

#---------------------------------------
#WHILE LOOP

#Question 1

# This program has some syntactic issues, fix them so that the 
# output is correct: 
# num = int(input(“Enter a number:”) 
# while num = 0: 
# print(num) 
# print(“DONE!!!”) 
# Output: 
# Enter a number:5 
# 5 
# 4 
# 3 
# 2 
# 1 
# DONE!!! 

num = int(input("Enter a number: "))
while num != 0:
    print(num)
    num=num-1
print("DONE!!!")

#Question 2

# You have been tasked with developing a small shop “print a 
# receipt” for items bought. The shopkeeper enters the item 
# name, quantity and price of each item. Your program should: 
# a. Use a loop to repeat the input and calculation until no more 
# items are to be entered. 
# b. Calculate the total price for each item. 
# c. If the quantity is more than 10 then apply a 10% discount to 
# the total price. 
# d. Print each item’s details and the total. 
# e. Accumulate each total to show a grand total at the end. To 
# end the application, enter XXX. 
# Enter item: Apples 
# Enter quantity: 5 
# Enter unit price: 0.50 
# Total for Apples: £2.50 
# Enter item: Milk 
# Enter quantity: 12 
# Enter unit price: 2.50 
# Total for Milk: £27.00 (10% discount applied) 
# Enter item: Bread 
# Enter quantity: 2 
# Enter unit price: 1.45 
# Total for Bread: £2.90 
# Grand total: £32.40

grand_total = 0.00 

item = input("Enter item , if you want to exit type XXX: ")

while item !="XXX": 
    
    quantity = int(input("Enter quanity: "))
    price = float(input("Enter unit price: "))
    total= quantity*price 
    if quantity > 10:
        discount_price = (price * quantity)* 0.10
        total-=discount_price
    print(f"Total for the {item} is: {total}")
    grand_total= grand_total+total
    item = input("Enter item , if you want to exit type XXX: ")

print(f"The grand total is: {grand_total}")

#Question 3

# In the game of Lucky Sevens, the player rolls a pair of dice. 
# If the dots add up to 7, the player wins £4, otherwise the 
# player loses £1. You need to write a program that should take 
# as input the amount of money that the player wants to put 
# into the pot and ask the user if they want to play – yes / no - quite while they are ahead. Play the game until the pot is 
# empty or they don’t want to play. At that point, the program 
# should print the number of rolls it took to break the player, 
# or print the maximum amount of money in the pot.

import random 

print("Welcome to lucky sevens game!")
pm = int(input("Enter the amount to you to add in the pot "))
total_rolls = 0
cho = input("Do you wish to play the game? Y or N ")
while cho!= "N"and pm!= 0:
    print("Rolling dice!")
    d1 = random.randint(1,9)
    print(f"Die 1: {d1}")
    d2 = random.randint(1,9)
    print(f"Die 1: {d2}")
    if(d1+d2 == 7):
        print("You won 4 pounds!")
        pm= pm+4
        total_rolls = total_rolls+1
    else:
        print("You lost 1 pound!")
        pm = pm-1
        total_rolls = total_rolls+1
    cho = input("Do you wish to play the game? Y or N ")

if pm== 0:
    print(f"Total rolls that broke you: {total_rolls}")
    print(f"Money in pot: {pm}")
else:
    print("You quit!")
    print(f"Total rolls: {total_rolls}")
    print(f"Money in pot: {pm}")

#Question 4

# Create a math game for small children to practise their basic 
# maths.  
# Question 1: What is 9 + 2? 
# Your answer: 11 
# Correct!! 
# Question 1: What is 5 + 6? 
# Your answer: 15 
# Inorrect. The correct answer was 11 
# (and so on, do this 10 times and then print 
# You got 9 out of 10 correct (as an example) 
# Hint: play around with the game, include other elements.  

import random

print("Welcome to fun game for kids! ")
print("We will check if you know addition!!")

i= 0
correct= 0

while i <=10:

    q1 = random.randint(1,9)
    q2 = random.randint(1,9)
    print(f"What is: {q1} + {q2}? ")
    ans= int(input("Enter the answer: "))
    if ans == q1+q2:
        print("Correct answer! YAYYYY ")
        correct=correct+1
    else:
        print("Oh no! The answer is wrong :( ")
    i=i+1
print(f"You got {correct} out of 10 questions!")


#Challenge 

#Question 6

#  Create a mini food delivery app (console simulation), 
# include the following features as part of your code: 
# a. Login simulation, create a username = “student” and a 
# password = “python4Ever” 
# b. Ask the use to enter their username/password  
# c. verify if it is valid (it should match what is in “a”) 
# d. ask the user the choose a delivery time (1 – standard 30
# 40min, 2 Express (less than 30min) 
# e. if the delivery time is 1, then there is no fee, otherwise 
# express means a fee of 3.50, if they don’t choose the 
# correct choice then a message must be displayed. 
# f. print the delivery time chosen and the fee 
# g. ask the user to enter the order total 
# h. if the total is less than £20 then print that they can use 
# contactless payment, otherwise they need to use a pin 
# i. ask them to enter the pin, if the pin is “12345” then this 
# is correct otherwise it is incorrect 
# j. print that the order has been place successfully 
# k. what the delivery time will be  
# l. ask them to rate the service 
# m. 5 to 1, if they enter 5 then print a message *** thank you, 
# you are awesome, a rating less than 5 but at least 3, print – thank you for your feedback we’ll keep improving, lastly 
# sorry you are unhappy we will be in contact!!

def deliverycharge(tim):
    match tim:
        case 1:
            print("No delivery fees for standard delivery")
        case 2:
                print("The option chose is Express 30 mins to 40 mins delivery")
                print(f"The delivery charge is: {express}")
        case 3:
              print("The option selected is Express (less than 30 mins)")
              print(f"The delivery charge is: {express}")
return tim


def amt(amount):
    if amount < 20:
        print("contactless delivery")
    else:
        upin = int(input("For amount over 20, enter pin: "))
        if upin == pin:
            print("Order placed Successfully")
        else:
            print("Failed!")

def rating(rate):
    if rate == 5:
          print("thank you, you are awesome")
    if 3 <= rate >5:
        print("thank you for your feedback we’ll keep improving")
    if rate > 3:
        print("lastly sorry you are unhappy we will be in contact!!")
return rate


print("Mini delivery app")
print("Login page")
user= "python4Ever"
pas = "student"
pin = 12345
express = 3.50
amount = 0
us = input("Enter username: ")
ps = input("Enter password: ")

if us == user and ps == pas:
    print("Select delivery time: ")
    print("1 - Standard")
    print("2 - 30 mins to 40 mins")
    print("3 - Express (less than 30 mins)")
    tim = int(input("select time: "))
    if tim ==1 or tim == 2 or tim ==3:
        deliverycharge(tim)
        amount = int(input("Enter total amount "))
        amt(amount)
    if express == True:
         print(f"The delivery will take place in {express}")
    else: 
         print("It will take 30 mins!")
    rate= int(input("Rate our services! "))
    rating(rate)
else:
     print("Wrong input!")