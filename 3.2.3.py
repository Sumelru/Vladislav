a=int(input('a='))
b=int(input('b='))
if a<b:
    C=a+b
    print('C=', C, sep='')
elif a>b and a>3:
    C=(b**2)-b
    print('C=', C, sep='')
else:
    C=(b**2)-1
    print('C=', C, sep='')