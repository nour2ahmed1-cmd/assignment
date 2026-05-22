# this is Level 1 Question 1: Ask the user to enter a number, then print its multiplication table from 1 to 10.
# use for loop to print the multiplication table
number = int(input("Enter a number: "))
print(f"Multiplication table for {number}:")
for x in range(1, 11):
    print(f"{number} x {x} = {number * x}")

# this is Level 1 Question 2: Write a program that prints all even numbers from 1 to 30.
# At the end, print how many even numbers were found.
# use a counter variable to count the even numbers
counter = 0
print("Even numbers from 1 to 30:")
for number in range(1, 31):
    if number % 2 == 0:
        print(number)
        counter += 1

print(f"Total even numbers from 1 to 30: {counter}")

# level 2 Question 3 : Write a program that asks the user to enter a password.
# The correct password is: "python123". The user has 3 attempts to enter the correct password.
# # If the user enters the correct password, print "Access granted".
# # If the user fails to enter the correct password after 3 attempts, print "Access denied".
# use a while loop
correct_password = "python123"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1
else:
    print("Access denied.")

# Question 4 : Ask the user how many marks they want to enter.
# Then ask them to enter the marks one by one.
# Finally, print the average mark.
# use a loop, a total variable, and division to calculate the average
total_marks = 0
number_of_marks = int(input("How many marks do you want to enter? "))
for x in range(number_of_marks):
    mark = float(input(f"Enter mark {x + 1}: "))
    total_marks += mark

print(f"Average mark: {total_marks / number_of_marks}")

#level 3 Question 5 : Create a number guessing game.
# Use this fixed secret number: 7 
# Ask the user to guess the number.
# the program should keep running until the user guesses the correct number.
# If the user's guess is too low, print "Too low"
# If the user's guess is too high, print "Too high"
# if the user guesses the correct number, print "Correct!" and end the program.
# use a while loop to keep the game running until the user guesses the correct number
secret_number = 7
is_guess_correct = True
while is_guess_correct:
    guess = int(input("Guess the number (1-20): "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        is_guess_correct = False

# Question 6 : create a simple ATM program
# balance = 1000
# show this menu repeatedlu: 1. Check balance 2. Deposit money 3. Withdraw money 4. Exit
# if the user chooses 1, print the current balance
# if the user chooses 2, ask them how much they want to deposit, then add that amount to the balance
# if the user chooses 3, ask them how much they want to withdraw, 
# If the amount is greater than the balance, print: "Insufficient balance"
# if the amount is less than or equal to the balance, subtract that amount from the balance
#use a while loop with a menu
balance = 1000
while True:
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: ${balance:.2f}")
    elif choice == '2':
        deposit_amount = float(input("Enter the amount to deposit: "))
        balance += deposit_amount
        print(f"${deposit_amount:.2f} deposited successfully.")
    elif choice == '3':
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw_amount
            print(f"${withdraw_amount:.2f} withdrawn successfully.")
    elif choice == '4':
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please try again.")

# question 7 : Create a simple shopping cart program.
# The user should be able to enter item prices one by one.
# Each time, ask: enter price or 0 to finish.
# when the user enters 0, stop asking for prices then print: Number of items: X, Total price: Y, Avarage item price: Z, Most expensive item: W, Cheapest item: V
# Requirements: Count the number of items. Calculate the total price. Calculate the average price. Find the most expensive item. Find the cheapest item. If the user enters 0 without adding any items, print: No items were added.
# You need variables for total, count, maximum, and minimum.
total_price = 0
item_count = 0
most_expensive = 0
cheapest = float('inf')  # Initialize to infinity for comparison
while True:
    price = float(input("Enter item price (or 0 to finish): "))
    if price == 0:
        break
    total_price += price
    item_count += 1
    if price > most_expensive:
        most_expensive = price
    if price < cheapest:
        cheapest = price
if item_count == 0:
    print("No items were added.")
else:
    average_price = total_price / item_count
    print(f"Number of items: {item_count}")
    print(f"Total price: ${total_price:.2f}")
    print(f"Average item price: ${average_price:.2f}")
    print(f"Most expensive item: ${most_expensive:.2f}")
    print(f"Cheapest item: ${cheapest:.2f}")

# last question : Create a program that manages marks for multiple students.
# First, ask the user: How many students do you want to enter?
# For each student, ask: Enter the student's name, then ask: How many marks this student has?, then enter the marks one by one. then calculate the average mark for that student, then print the student's result
# Student name: X, How many marks for X: Z, Average mark: Y.
# Rules: If the average is 50 or more, the student passes. If the average is below 50, the student fails. At the end, print:
# then print Total number of students, Number of passed studentsm Number of failed students, The highest average, The name of the student with the highest average
# This question uses nested loops: one loop for students, and another loop for each student’s marks.
number_students = int(input("How many students do you want to enter? "))
total_students = 0
passed_students = 0
failed_students = 0
highest_average = 0
student_with_highest_average = ""
for _ in range(number_students):
    student_name = input("Enter the student's name: ")
    number_marks = int(input(f"How many marks does {student_name} have? "))
    total_marks = 0
    for _ in range(number_marks):
        mark = float(input("Enter mark: "))
        total_marks += mark
    average_mark = total_marks / number_marks
    print(f"Student name: {student_name}, Average mark: {average_mark:.2f}")
    
    if average_mark >= 50:
        print(f"{student_name} passes.")
        passed_students += 1
    else:
        print(f"{student_name} fails.")
        failed_students += 1
    
    if average_mark > highest_average:
        highest_average = average_mark
        student_with_highest_average = student_name
total_students = number_students
print(f"Total number of students: {total_students}")
print(f"Number of passed students: {passed_students}")
print(f"Number of failed students: {failed_students}")
print(f"The highest average: {highest_average:.2f}")
print(f"The name of the student with the highest average: {student_with_highest_average}")
