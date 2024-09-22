v=int(input('v='))
k=int(input('k='))
if v>k:
    Z=v-k+1
    print('Z=', Z, sep='')
elif v<k:
    Z=(k**2)-(v**2)
    print('Z=', Z, sep='')
else:
    Z=(k**2)-k
    print('Z=', Z, sep='')