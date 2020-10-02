import math
t = int(input())
for i in range(0, t):
    n = int(input())
    n = list(str(n))
    start = 0
    end = -1
    while(start != math.floor(len(n) / 2)):
        n[end] = n[start]
        end = end - 1
        start = start + 1
    print(int(''.join(n)))
