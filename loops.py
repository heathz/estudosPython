x = [1, 4, 7, 8, 5, 2, 3, 6, 9]
i = 0

##### FOR #####

for i in range(10):
    print(i)
print()

for i in x:
    print(i)
print()

for i in range(len(x)):
    print(x[i])
print()

for i, element in enumerate(x):
    print(i, element)


##### WHILE #####

while i < 10:
    print("run")
    i += 1
