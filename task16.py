import csv

with open("Input/grades.csv") as f:
    reader = csv.DictReader(f)
    students = list(reader)

sum = int(0)

for student in students:
        if int(student["grade"]) == 5: 
             sum += 1
            

with open("Output/output16.txt", "w") as f1:
    f1.write(F"The number of students with highest result: {sum}")
