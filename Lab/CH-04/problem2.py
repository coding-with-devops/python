#Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
for i in range(6):
    mark = float(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

# Sort the marks in ascending order
marks.sort()
# Display the sorted marks
print("Sorted marks:", marks)