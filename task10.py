with open("Input/numbers.txt") as f:
    numbers=[int(line.strip()) for line in f ]
    numbers.sort()

with open("Output/output10.txt","w") as f1:
    for number in numbers:
        f1.write(f"{number}\n")