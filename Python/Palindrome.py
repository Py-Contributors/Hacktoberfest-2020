#code
t = int(input())
for i in range(0,t):
    string = input().lower()
    stringnew = ''.join(e for e in string if e.isalnum())
    if(stringnew==stringnew[::-1]):
        print('YES')
    else:
        print('NO')
