# def burger():
#   quantity = 2
#   price = 10
#   total_price = quantity * price
#   print(f"Total bill ${total_price}")

# burger()

def pizza(quantity, discount = 0.3): #so if we call without parameter we will get a default value of 1
  quantity = int(input("How much pizza would you like to order?: "))
  price = 10
  bill = (price*quantity) - (price*discount)
  print(f"total bill ${bill} with {quantity} purchased")

pizza()