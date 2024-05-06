class Person:
  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height

  def sayHello(self):
    print(f"Hello {self.name}, nice to meet you!")
  
  def ride(self):
    self.sayHello()
    if self.age > 10 and self.height >= 100:
      print(f"Congratulations {self.name}! You may ride the roller coaster.")
    else:
      print(f"Sorry {self.name}, you cannot ride the roller coaster yet.")
  
james = Person("James", 10, 140)
rose = Person("Rose", 12, 150)
dove = Person("Dove", 12, 150)
diva = Person("Diva", 8, 130)

while True:
  print("--Fantasy Roller Coaster--")
  print("1. James\n2. Rose\n3. Dove\n4. Diva")
  name = input("Enter name: ").lower()
  if name == "james":
    james.ride()
  elif name =="rose":
    rose.ride()
  elif name == "dove":
    dove.ride()
  elif name =="diva":
    diva.ride()
  else:
    print("Invalid Input")
  ans = input("y to continue/n to quit: ")
  if ans =="n":
    break