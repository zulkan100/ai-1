class laptop:
  def __init__(self,brand, year, color, ram):
  #self = this (in js)
    self.brand = brand
    self.year = year
    self.color = color
    self.ram = ram

  def information(self):
    return f"Company: {self.brand}\nColor: {self.color}\nProduction Year: {self.year}\nRam: {self.ram}"
  
  def coding(self):
    print("Laptop is being used for coding...")
    print("Ram usage: 2GB")
    self.ram -= 2
    print(f'Ram remaining: {self.ram}GB')
  def powerpoint(self):
    print("Laptop is being used for making powerpoints...")
    print("Ram usage: 1GB")
    self.ram -= 1
    print(f'Ram remaining: {self.ram}GB')
  def editing(self):
    print('Laptop is being used for video editing...')
    print("Ram usage: 3GB")
    self.ram -=3
    print(f"Remaining ram {self.ram}GB")


  
laptop_1 = laptop("lenovo", 2020, "Gray", 8)
laptop_2 = laptop("Asus", 2021, "Black", 12)
laptop_3 = laptop("Samsung", 2024, "Titanium", 16)
# print(laptop_1)
# print(laptop_1.brand)

print(laptop_1.information())
print(laptop_2.information())

print("--this laptop 1--")
laptop_1.coding()
laptop_1.powerpoint()
laptop_1.editing()
print("--this laptop 2--")
laptop_2.coding()
laptop_2.powerpoint()
laptop_2.editing()
print(f"--this laptop 3--")
laptop_3.coding()
laptop_3.powerpoint()
laptop_3.editing()

class gamingLaptop(laptop):
  def __init__(self, brand, year, color, ram, vga):
    super().__init__(brand, year, color, ram)
    self.vga = vga
  
  def infogame(self):
    return(super().information() + f"{self.vga}")
  def gaming(self):
    print("Laptop used for gaming...")
    print("Ram used: 8GB")
    self.ram -= 8
    print(f"Remaining RAM: {self.ram}GB")
  def recording(self):
    print("Currently recording...")
    print("Ram used: 2gb")
    self.ram -= 2
    print(f'Remaining RAM: {self.ram}GB')
  

laptop_4 = gamingLaptop("Logitech", 2021, "Silver", 16, "RTX 1650")
print("--THIS LAPTOP 4!!")
print(laptop_4.infogame())
laptop_4.gaming()
laptop_4.recording()
laptop_4.powerpoint()


# class superCar:
#   def __init__(self, brand, model, cost):
#     self.brand = brand
#     self.model = model
#     self.cost = cost

#   def information1(self):
#     return(f"Comes from: {self.brand} \nModel: {self.model} \nCost: {self.cost}")

# supaCar_1 = superCar("Toyota", "BMW", "1.500.000.000")
# print('---welcome to car shophop---')
# print(supaCar_1.information1())

