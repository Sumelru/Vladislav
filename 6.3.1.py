n=int(input('Введите длину массива: '))
D=[]
S=0
for i in range(n):
    print('Введите', i+1, 'элемент:')
    D.append(int(input()))
for i in range(n):
    if i%2!=0:
        S+=D[i]
print(S)