with open("Input/numbers.txt") as f:
    numbers=[int(line.strip()) for line in f ]

with open("Output/output09.txt","w") as f1:
    f1.write(f"Max: {max(numbers)}")