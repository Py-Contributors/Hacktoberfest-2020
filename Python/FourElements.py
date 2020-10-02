
t = int(input())
t1 = 1
while t1 <= t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    x = int(input())
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
                    break
                elif s2 < x:
                    k += 1
                else:
                    l -= 1
            j += 1
        i += 1
    print(flag)
    t1 += 1
