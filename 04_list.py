list = [3,6,5,3,6,3]
print(list)

print(list[2])

list.pop(0)
print(list)

list[3] = 100
print(list)


list = list + [7,6,8]

print(list)

list.append(300)
print(list)

print(list[:2])
list[:2] = [0,0]
print(list)


list[:2]=[]
print(list)

list[:]=[]

print(list)
