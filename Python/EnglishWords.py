t = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(0, t):
    con = 0
    s = list(input().lower())
    if(s[0] not in vowels):
        con = 1
        ch = s[0]
        s.remove(s[0])
        s.append(ch)
    if(con == 1):
        s.append('at')
    s = ''.join(s)
    print(s.upper())
