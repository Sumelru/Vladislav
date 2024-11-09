A=[]
C=[]
n=int(input('Длинна строки: '))
m=int(input('Длинна стобца: '))
for i in range(n):
	B=[]
	for j in range(m):
		B.append(int(input('Введите элемент массива: ')))
	A.append(B)
for i in range(n):
	for j in range(m):
		print(A[i][j], end=' ')
	print()
for i in range(n):
	S=0
	for j in range(m):
		S+=A[i][j]
	C.append(S)
print('Строка с наибольшей суммой элементов:\n', A[C.index(max(C))], max(C))
print('Строка с наименьшей суммой элементов:\n', A[C.index(min(C))], min(C))