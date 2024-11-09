A=[]
C=[]
n=0
with open('10.4.1\Гонтарь Владислав_УБ-41_vvod.txt', 'r') as vvod:
    for line in vvod:
        S=line.strip()
        B=S.split(' ')
        m=len(B)
        for i in range(m):
            B[i]=int(B[i])
        A.append(B)
        n+=1
for i in range(n):
	S=0
	for j in range(m):
		S+=A[i][j]
	C.append(S)
with open('10.4.1\Гонтарь Владислав_УБ-41_vivod.txt', 'w') as vivod:
      vivod.writelines('Строка с наибольшей суммой элементов:\n')
      vivod.writelines((str(A[C.index(max(C))]), '\n'))
      vivod.writelines(((str(max(C))), '\n'))
      vivod.writelines('Строка с наименьшей суммой элементов:\n')
      vivod.writelines((str(A[C.index(min(C))]), '\n'))
      vivod.writelines(((str(min(C))), '\n'))