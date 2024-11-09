def natur():
	n=int(input('Введите ряд натуральных чисел: '))
	A=[]
	if n%10==0:
		n//=10
	for i in range(len(str(n))):
		A.append(str(n)[i])
	for i in range(len(A)):
		if i%2==0:
			print(A[i])
		
natur()
