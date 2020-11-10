t = int(input())
for i in range(0, t):
    s = input()
    c = 0
    for j in range(0, len(s) - 1, 1):
        if(s[j:j + 3] == 'gfg'):
            c = c + 1
    if(c == 0):
        print(-1)
    else:
        print(c)
