t = int(input())
t1 = 1
while t1 <= t:
    n, x = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr.sort()
    flag = 0
    i = 0
    while i < n - 3:
        s = arr[i]
        j = i + 1
        while j < n - 2:
            s1 = s + arr[j]
            k = j + 1
            l = n - 1
            while k < l:
                s2 = s1 + arr[k] + arr[l]
                if s2 == x:
                    flag = 1
                    print(arr[i], arr[j], arr[k], arr[l], '$', end="")
                    break
                elif s2 < x:
                    k += 1
                else:
                    l -= 1
            j += 1
        i += 1
    t1 += 1
    if(flag == 0):
        print(-1)
