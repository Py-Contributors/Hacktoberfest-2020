t = int(input())
for i in range(0, t):
    C1, C2 = map(int, input().strip().split())
    s1 = list(map(int, input().strip().split()))
    s2 = list(map(int, input().strip().split()))
    if(sum(s1) > sum(s2)):
        print("C1")
    else:
        print("C2")
