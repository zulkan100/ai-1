import numpy as np
# Array2D = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# print(Array2D)

#2d array
before = np.array([[1,2,3,4], 
                   [5,6,7,8], 
                   [9,10,11,12]])
print(before)
print(before[1,2])
print(before[-2,-2])
print(before[1, 1:3])

print(before[1:3, 1:4])

print(before[0:2, 1:4])
print(before.diagonal(2))
print(np.fliplr(before).diagonal(0))

data = np.zeros((4,4), dtype='int')
data[0, 1:4] = [1,55,3]
data[-1, -3] = 14

# data[2, 2:4] = [0,70]
# data[3, 2:4] = [14,22]

data[2:,2:] = [[0,70], [14,22]]
print(data)

c = np.array([3,6,9,12])
d = np.array([6,12,18,24])


print(np.add(c[2],d[3]))
print(np.multiply(c,d))