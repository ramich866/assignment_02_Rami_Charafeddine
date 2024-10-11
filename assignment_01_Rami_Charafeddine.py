# Ex1:

number1 = float(input("enter first number:"))
number2 = float(input("enter second number:"))
number3 = float(input("enter third number:"))

if number1 > number2 and number1 > number3:
    print("the max value is ", number1)
elif number2 > number1 and number2 > number3:
    print("the max value is ", number2)
else:
    print("the max value is ", number3)


# Ex2:

n = int(input("Enter a positive integer:"))
number = 1
product = 1

while (n >= number):
    if number % 2 != 0:
        product = product * number
    number += 1

if product >= 100:
    print("multiplication exceeded bzyede hbb")
else: 
    print("Final product: ", product)


# Ex3:

score = int(input("Enter a score: "))
list_of_scores = []

while score != -1: 
    list_of_scores.append(score)
    score = int(input("Enter a score: "))

if len(list_of_scores) == 0:
    print("no scores were entered. au revoir!")
else:
    average = sum(list_of_scores)/len(list_of_scores) 
    print("the average is: ", average)


# Ex4: 

number = int(input("Enter a four digit number: "))

first_digit = (number // 1000) % 10
second_digit = (number // 100) % 10
third_digit = (number // 10) % 10
fourth_digit = number % 10

if (first_digit + second_digit == third_digit + fourth_digit):
    print("F")
else: print("U")
