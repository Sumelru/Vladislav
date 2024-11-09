def rev(n):
	s=len(str(n))-1
	if s==0:
		return n
	return (n%10)*(10**s)+rev(n//10)
		
n=int(input('n='))
print(rev(n))
