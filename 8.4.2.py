A=[]
Sn=0
n=int(input('Размер матрицы: '))
for i in range(n):
	B=[]
	for j in range(n):
		B.append(int(input('Введите элемент матрицы: ')))
	A.append(B)
for i in range(n):
	for j in range(n):
		if A[i][j]<=0:
			A[i][j]=0
			Sn+=1
		else:
			A[i][j]=1
A=[]
for i in range (n):
	B=[]
	for j in range(n):
		if j>i:
			B.append(0)
			Sn=Sn-1
		else:
			B.append(1)
	A.append(B)
for i in range(n):
	for j in range(n):
		if i>=j and Sn>0:
			A[i][j]=0
			Sn=Sn-1
for i in range(n):
	for j in range(n):
		print(A[i][j], end=' ')
	print()