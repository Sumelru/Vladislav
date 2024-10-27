x=input('Введите строку: ')
y=[]
for i in range(len(x)):
    y.append(x[i])
print(sorted(y))