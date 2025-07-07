def calculate_tax(salary): 

    if salary > 5000000: return salary * 0.20
    else : return  salary * 0.13

def calculate_net_salary(salary): 
    
    tax = calculate_tax(salary)
    return salary - tax


salary = int (input("Type salary: "))

print(f"Tax: {calculate_tax(salary)}")
print(f"Net amount: {calculate_net_salary(salary)}")


