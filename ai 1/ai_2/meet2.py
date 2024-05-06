colors = ["red", "green", "blue", "yellow", "purple"]
x = "Rudolf - 31D"
print(len(x))
print(colors[0:2]) #before 2
print(colors[2:]) #2 and after 2
print(colors[:2])
print(len(colors[:2]))

colors.append("yo lala") #add
print(colors)
del colors[:2] #delete
print(colors)
colors.insert(2, "Brown") #append by index
print(colors)

#tuple is static, cannot change remove add
color = ('red', 'green', 'blue')
print(color)
color1, color2, color3 = color
print(color1)
print(color2)
print(color3)
print("brown" in color) #true false