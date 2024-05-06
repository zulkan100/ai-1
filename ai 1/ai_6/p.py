import numpy as np

data = np.zeros((6, 4), dtype = "int")
print(data)

data[1, 1] = 1
data[2:4, :2] = [[12,14], [13,15]]
data[-1, :-1] = [12,13,14]

print(data)

# data1 = np.array([[1,2,3,4], 
#           [5,6,7,8]])
data1 = [[1,2,3,4], [5,6,7,8]]

data1[1][0] = 4

for row in (data1):
  print(row)

