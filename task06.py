students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}

avg = sum(students.values()) / len(students)
values = students.items()

for name,value in values:
    if value > avg: 
        print (name)

    

