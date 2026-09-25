Python Basic Practice Assignments (Assignment 01)

This repository contains step-by-step problem-solving plans and Python code solutions for basic programming concepts including user input, data type conversion, arithmetic operations, boolean logic, and conditional statements (if-elif-else).

Submission Info

Email: h03331146@gmail.com

Questions & Solutions

Q1. Simple Greeting

Problem: Ask the user for their name and age (as integer). Print a message like: "Hello Ali, you are 20 years old."

Plan

Prompt the user for their name as a string.

Prompt the user for their age and convert it to an integer (int).

Print the formatted message using string formatting.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")


Q2. Area of a Rectangle

Problem: Take the length and width of a rectangle from the user (as floats) and print the area.

Plan

Get the rectangle length from the user as a floating-point number (float).

Get the rectangle width from the user as a float.

Calculate the area using area = length * width.

Print the calculated area.

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area of the rectangle is: {area}")


Q3. Even or Odd

Problem: Ask the user to enter a number. Using an if statement, tell them whether it is even or odd.

Plan

Ask the user for an integer number.

Check if number % 2 == 0.

If true, print that the number is even; otherwise, print that it is odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


Q4. Positive, Negative, or Zero

Problem: Take a number as input and print whether it is positive, negative, or zero.

Plan

Take a number input from the user (convert to float).

Use if to check if number > 0 (Positive).

Use elif to check if number < 0 (Negative).

Use else for Zero.

number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


Q5. Pass or Fail

Problem: Ask the user to enter their marks (out of 100). If marks are 40 or above, print "Pass", otherwise print "Fail".

Plan

Prompt user for their marks and parse as float.

Check if marks >= 40.

Output "Pass" if condition is met, else output "Fail".

marks = float(input("Enter your marks (out of 100): "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


Q6. Voting Eligibility

Problem: Ask the user for their age. If age is 18 or above, print "You are eligible to vote", otherwise print "You are not eligible to vote".

Plan

Input user's age as int.

Verify if age >= 18.

Print appropriate eligibility message based on the comparison.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


Q7. Temperature Checker

Problem: Take today's temperature (in Celsius) as input. If it is above 35, print "It's a hot day", if it is below 15, print "It's a cold day", otherwise print "The weather is pleasant".

Plan

Input temperature value as float.

Check if temp > 35 -> "It's a hot day".

Check if temp < 15 -> "It's a cold day".

Otherwise -> "The weather is pleasant".

temp = float(input("Enter today's temperature in Celsius: "))
if temp > 35:
    print("It's a hot day")
elif temp < 15:
    print("It's a cold day")
else:
    print("The weather is pleasant")


Q8. Simple Calculator (Addition Only)

Problem: Take two numbers from the user as input, convert them to floats, and print their sum.

Plan

Read the first number as float.

Read the second number as float.

Add the numbers together and print the result.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
total = num1 + num2
print(f"The sum is: {total}")


Q9. Boolean Practice

Problem: Ask the user to enter their age. Store the result of age >= 18 in a variable of boolean type and print whether the value is True or False.

Plan

Get age as int.

Create boolean variable is_adult = age >= 18.

Print the boolean variable value directly.

age = int(input("Enter your age: "))
is_adult = age >= 18
print(is_adult)


Q10. Number Guessing Game (Challenge)

Problem: Store a secret number in a variable (e.g., 7). Ask the user to guess the number. If their guess matches, print "Correct guess!", otherwise print "Wrong guess, try again next time."

Plan

Assign secret_number = 7.

Take user's guess as an integer input.

Compare guess == secret_number.

Output response based on comparison outcome.

secret_number = 7
guess = int(input("Guess the secret number: "))

if guess == secret_number:
    print("Correct guess!")
else:
    print("Wrong guess, try again next time.")
