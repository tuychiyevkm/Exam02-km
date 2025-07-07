from json import load, dump

with open("Input/students.json") as f:
    students = load(f)

names = [student["name"] for student in students if student["name"].startswith("A") ]

with open("Output/output14.json", "w") as f1:
        dump({"a_names": names}, f1, indent=4)