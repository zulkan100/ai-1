print(""" Burger List: 
      1. Beef Burger = 15$
      2. Krabby Patty = 30$
      3. Kids Burger = 5$""")
menu_price = input("Menu Price: ")
amount = input("Amount: ")
bill = int(menu_price)*int(amount)
print("You need to pay " +str(bill))
