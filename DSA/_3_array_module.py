import array as arr

data = arr.array('i',[4,5,3,5,7,21])
print(data)

data = arr.array('d',[4.6,5.4,3.3,5.1,7.1,21])
print(data)

data.append(1.2)
print(data)

data.pop()
print(data)

data.extend([1.2,4,5,6])
print(data)








