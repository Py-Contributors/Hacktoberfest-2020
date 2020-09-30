def mp(s1,s2):
    count= 0
    s2.sort()
    plat_needed = 1
    result = 1
    first = 1
    second = 0
    while first<len(s1) and second<len(s2):
        if s1[first]<s2[second]:
            plat_needed+=1
            first+=1
            if plat_needed > result:
                result = plat_needed
        else:
           plat_needed-=1
           second+=1
    return result

#code
for i in range(int(input())):
    n = int(input())
    s1 = list(map(int,input().split()))
    s2 = list(map(int,input().split()))
    print(mp(s1,s2))