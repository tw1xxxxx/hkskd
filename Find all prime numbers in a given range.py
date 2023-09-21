line = input("Введите числа через пробел ")
a = []
for i in line.split(' '):
    a.append(int(i))

for i in a:
    if i != 2:
        if i % 2 != 0:
            print(i)
    elif i == 2:
        print(i)
    

        