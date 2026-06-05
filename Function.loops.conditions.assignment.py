# the main task is to create a training center performance system
# build one complete python program for a training center that helps the trainer evaluate students in a Python basic course
# the trainer enters students scores
# the program calculates each student’s final grade, status, advice, and a final group summary.
# use variables, input(), print(),if/elif/else, for loop, while loop, functions and returns in your program.
# Step 1 — Ask for the Number of Students. The program should ask the trainer how many students they want to evaluate.
# Step 2 — Repeat the Process for Each Student. For every student, ask for the following information: student’s name, atteendance score out of 100: homework score out of 100: Quiz score out of 100: participation score out of 100:
# Step 3 — Calculate the Final Grade. For each student, calculate the final grade using this weighted formula: final grade = (attendance score * 20%) + (homework score * 35%) + (quiz score * 35%) + (participation score * 10%)
# Step 4 — Decide the Student Status. After calculating the final grade, print the student’s status using these rules: final grade is 85 or more: status: "Excellent", final grade is between 70 and 84: status: "Good", final grade is between 50 and 69: status: "Needs Improvement", final grade is below 50: status: "Failed"
# important condition: Even if the final grade is high, the student should fail if attendance is less than 50. status  should be "Failed because of low attendance"
# the program must contain and use the following functions. Do not write the whole program inside one big block. 
# Returns the weighted final grade: calculate_final_grade(attendance, homework, quiz, participation), Returns the student status as text: get_student_status(final_grade, attendance), Returns an advice message based on the weakest area: get_student_advice(attendance, homework, quiz, participation), Prints one clean student report: print_student_report(name, final_grade, status, advice), Keep asking until the score is between 0 and 100: get_valid_score(message), Keep asking until the number of students is greater than 0: get_valid_students_number()
# The score validation function must keep asking until the user enters a score between 0 and 100: Invalid score. Please enter a number between 0 and 100.
# The number of students must also be validated. It must be greater than 0: Invalid number. Please enter a number greater than 0.
# Student Report Output: After each student is evaluated, print a clean report: Student Report: Name: [Student's Name], Final Grade: [Final Grade], Status: [Status], Advice: [Advice]
# Advice System: After printing each student report, print one extra advice message based on the student’s weakest area.If attendance is less than 50: Message: You need to attend more sessions. 
# Else if homework score is less than 50: Message: You need to focus more on homework. Else if quiz score is less than 50: Message: You need to study more for quizzes. Else if participation score is less than 50: Message: Try to participate more during sessions. Else: Message: Keep up the good work.
# Create a function called get_student_advice(attendance, homework, quiz, participation). It should return the correct advice message as text.
# After all students are evaluated, print a final summary for the whole group. The summary should include: Total students, number of excellent students, number of good students, number of students who need improvement, number of failed students, number of students failed because of low attendance. class avarage. highest grade. lowest grade. The summary should be printed in a clean format.
# You are not allowed to use lists. To find the highest and lowest grades, use the first student’s grade as the starting value, then compare the rest of the students one by one.
def get_valid_students_number():
    while True:
        num_students = int(input("Enter the number of students to evaluate: "))
        if num_students > 0:
            return num_students
        else:
            print("Invalid number. Please enter a number greater than 0.")
def get_valid_score(message):
    while True:
        score = float(input(message))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score. Please enter a number between 0 and 100.")
def calculate_final_grade(attendance, homework, quiz, participation):
    final_grade = (attendance * 0.20) + (homework * 0.35) + (quiz * 0.35) + (participation * 0.10)
    return final_grade
def get_student_status(final_grade, attendance):
    if attendance < 50:
        return "Failed because of low attendance"
    elif final_grade >= 85:
        return "Excellent"
    elif 70 <= final_grade < 85:
        return "Good"
    elif 50 <= final_grade < 70:
        return "Needs Improvement"
    else:
        return "Failed"
def get_student_advice(attendance, homework, quiz, participation):
    if attendance < 50:
        return "You need to attend more sessions."
    elif homework < 50:
        return "You need to focus more on homework."
    elif quiz < 50:
        return "You need to study more for quizzes."
    elif participation < 50:
        return "Try to participate more during sessions."
    else:
        return "Keep up the good work."
def print_student_report(name, final_grade, status, advice):
    print(f"Student Report: Name: {name}, Final Grade: {final_grade:.2f}, Status: {status}, Advice: {advice}")
def main():
    num_students = get_valid_students_number()
    total_students = num_students
    excellent_count = 0
    good_count = 0
    needs_improvement_count = 0
    failed_count = 0
    failed_low_attendance_count = 0
    total_grade = 0
    highest_grade = None
    lowest_grade = None
    for _ in range(num_students):
        name = input("Enter the student's name: ")
        attendance = get_valid_score("Enter attendance score out of 100: ")
        homework = get_valid_score("Enter homework score out of 100: ")
        quiz = get_valid_score("Enter quiz score out of 100: ")
        participation = get_valid_score("Enter participation score out of 100: ")
        final_grade = calculate_final_grade(attendance, homework, quiz, participation)
        status = get_student_status(final_grade, attendance)
        advice = get_student_advice(attendance, homework, quiz, participation)
        print_student_report(name, final_grade, status, advice)
        total_grade += final_grade
        if highest_grade is None or final_grade > highest_grade:
            highest_grade = final_grade
        if lowest_grade is None or final_grade < lowest_grade:
            lowest_grade = final_grade
        if status == "Excellent":
            excellent_count += 1
        elif status == "Good":
            good_count += 1
        elif status == "Needs Improvement":
            needs_improvement_count += 1
        elif status == "Failed because of low attendance":
            failed_low_attendance_count += 1
        else:
            failed_count += 1
    class_average = total_grade / total_students if total_students > 0 else 0
    print("\nFinal Group Summary:")
    print(f"Total students: {total_students}")
    print(f"Number of excellent students: {excellent_count}")
    print(f"Number of good students: {good_count}")
    print(f"Number of students who need improvement: {needs_improvement_count}")
    print(f"Number of failed students: {failed_count}")
    print(f"Number of students failed because of low attendance: {failed_low_attendance_count}")
    print(f"Class average: {class_average:.2f}")
    print(f"Highest grade: {highest_grade:.2f}")
    print(f"Lowest grade: {lowest_grade:.2f}")
main()