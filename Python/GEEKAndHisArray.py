t = int(input())
t1 = 1
while t1 <= t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    x = int(input())
    flag = 0
    c = 0
    i = 0
    while i < n - 3:
        s = arr[i]
        j = i + 1
        k = n - 1
        while j < n - 2:
            s1 = s + arr[j] + arr[k]
            if s1 % x == 0:
                c = c + 1
                flag = 1
                break
            j += 1
        i += 1
    t1 += 1
    if(flag == 0):
        print(-1)
