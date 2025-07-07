def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b): 
    if b!=0:
        return a / b
    else:
        return None
    
a = float (input("1st num: ")) 
op = input("operation: ")      
b = float (input("2nd num: "))

if op == "+":  print(round(add(a,b),2))

elif op == "-": print(round(subtract(a, b),2))

elif op == "*": print(round(multiply(a, b),2))

elif  op == "/" and divide(a, b) is not None:
    print(round(divide(a, b), 2))


else: print("Wrong operation!")


