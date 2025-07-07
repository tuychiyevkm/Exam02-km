numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]


sq_num = list(map(lambda num: {"value": num["value"]** 2 }, numbers))

print(sq_num)
