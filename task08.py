with open("Input/numbers.txt") as f:
    numbers=[int(line.strip()) for line in f ]

with open("Output/output08.txt","w") as f1:
    f1.write(f"Sum: {sum(numbers)}")