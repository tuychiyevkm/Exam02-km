import csv

with open("Input/grades.csv") as f:
    reader = csv.DictReader(f)
    students = list(reader)

max = int(0)
h_student =""

for student in students:
        if int(student["grade"]) > max: 
            max = int(student["grade"])
            h_student = student["name"]

with open("Output/output15.txt", "w") as f1:
    f1.write(F"The student with highest result: {h_student}")
