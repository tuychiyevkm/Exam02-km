from json import load, dump

with open("Input/students.json") as f:
    students = load(f)

names = [student["name"] for student in students if len(student["name"]) > 5]

with open("Output/output13.json", "w") as f1:
        dump({"long_names": names}, f1, indent=4)