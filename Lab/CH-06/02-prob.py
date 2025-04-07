# problem 2
# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100
if percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("The student has passed.", "Percentage:", percentage, "%")
    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 40:
        print("Grade: C")
else:  
    print("The student has failed." , "Percentage:", percentage, "%")