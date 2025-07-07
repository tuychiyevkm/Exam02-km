def deposit(balance, amount): return balance + amount

def withdraw(balance, amount): return balance - amount

def check_balance(balance): return balance

balance = 100000
op = input ("Choose operations:  \n" \
"   if deposit input - d\n" \
"   if withdraw input - w\n"
"   if check_balance input - c\n")

if op == "d":
    amount = int(input("Type amount: "))
    balance = deposit(balance, amount)

elif op == "w":
    amount = int(input("Type amount: "))
    
    if amount <= balance:
        balance = withdraw(balance, amount) 
    else:
        print("Insuficcient funds")

elif op == "c": 
    print(f"Your balance {balance}")

print(F"Your new balance: {balance}")