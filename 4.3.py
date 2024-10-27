a=int(input('a='))
b=int(input('b='))
if a<b:
    for i in range(a, (b+1)):
        if i%2!=0:
            print(i)