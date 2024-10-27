x=[]
for i in range(8):
    print('Введите', i+1, 'элемент:')
    x.append(int(input()))
for i in range(8):
    if x[i]<15:
        x.insert(i, x[i]*2)
        x.pop(i+1)
print(x)