from json import load, dump

with open("Input/students.json") as f:
    students = load(f)

names = [student["name"] for student in students]
names.sort()

with open("Output/output12.json", "w") as f1:
        dump({"sorted_names": names}, f1, indent=4)