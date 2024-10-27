s=input('Введите строку: ')
string=''
for i in range(len(s)):
    if s[i]!='.':
        string+=s[i]
print(len(s)-len(string))