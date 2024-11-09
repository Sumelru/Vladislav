A=[]
Sn=0
n=0
with open('10.4.2\Гонтарь Владислав_УБ-41_vvod.txt', 'r') as vvod:
    for line in vvod:
        S=line.strip()
        B=S.split(' ')
        m=len(B)
        for i in range(m):
            B[i]=int(B[i])
        A.append(B)
        n+=1
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
vivod=open('10.4.2\Гонтарь Владислав_УБ-41_vivod.txt', 'w')
for i in range(n):
	for j in range(n):
	    vivod.writelines((str(A[i][j]), ' '))
	vivod.write('\n')
vivod.close()