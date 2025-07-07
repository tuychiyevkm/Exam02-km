from json import load, dump

with open("Input/students.json") as f:
    students = load(f)

    with open("Output/output11.json", "w") as f1:
        dump({"count": len(students)}, f1, indent=4)