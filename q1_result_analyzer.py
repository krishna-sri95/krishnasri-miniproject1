def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"
    print(f"\nStudent: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")

    below_40 = []
    for i in range(len(marks)):
        if marks[i] < 40:
            below_40.append(f"Subject {i + 1}")
    if below_40:
        print("Subjects below 40:", ", ".join(below_40))
    else:
        print("No subjects below 40")

name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

marks = []
for i in range(5):
    mark = float(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)

analyze_result(name, roll, marks)
