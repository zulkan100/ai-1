# def burger(quantity):
#   price = 10
#   total_price = quantity * price
#   print(f"Total bill ${total_price}")
  
# burger(quantity = int(input("Order:")))

def burger(quantity, discount=0.4):
  price = 10
  total_price = (quantity * price) - (price *discount)
  print(f"Total bill ${total_price}")

orders = input("Yes? ")

if (orders.isdigit()):
  burger(int(orders), discount=5)
