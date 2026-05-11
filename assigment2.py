
#Ask the user to enter marks for these 5 courses:
Math = float(input("Enter marks for Math: "))
Science = float(input("Enter marks for Science: "))
History = float(input("Enter marks for History: "))
Geography = float(input("Enter marks for Geography: "))
English = float(input("Enter marks for English: "))

# After entering each course mark:
# check if the student passed or failed the course.
# A student passes if the mark is 50 or more.
# Print the result before moving to the next course.
if Math >= 50:
    print("You passed Math.")
else:
    print("You failed Math.")

if Science >= 50:
    print("You passed Science.")
else:
    print("You failed Science.")

if History >= 50:
    print("You passed History.")
else:
    print("You failed History.")

if Geography >= 50:
    print("You passed Geography.")
else:
    print("You failed Geography.")

if English >= 50:
    print("You passed English.")
else:
    print("You failed English.")

# After entering all marks, calculate the final average percentage.
total_marks = Math + Science + History + Geography + English
average_percentage = total_marks / 5
print(f"Your average percentage is: {average_percentage:.2f}%")

#After entering all marks, Check the final grade based on the average percentage:

if average_percentage >= 85:
    print("Your final grade is: Excellent")
else:
    if average_percentage >= 75:
        print("Your final grade is: Very Good")
    else:
        if average_percentage >= 65:
            print("Your final grade is: Good")
        else:
            if average_percentage >= 50:
                print("Your final grade is: Pass")
            else:
                print("Your final grade is: Fail")

#Competition rules: The student can join the competition if: Final average is 85 or more AND Math mark is at least 80
if average_percentage >= 85 and Math >= 80:
    print("Congratulations! You are eligible to join the competition.")
#or Final average is less than 85 AND Math mark is at least 90
if average_percentage < 85 and Math >= 90:
    print("Congratulations! You are eligible to join the competition.")


