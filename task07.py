cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}

products = cart.values()
sum = 0
          

for product in products:
    sum += product["price"] * product["quantity"]

print(F"Total: {sum}")