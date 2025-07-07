numbers = [
    {'value': -5}, 
    {'value': 10}, 
    {'value': -1}, 
    {'value': 7}
]
# p_num =[num for num in numbers if num["value"] > 0]

p_num = list(filter(lambda num: num['value'] > 0, numbers))


print(p_num)
