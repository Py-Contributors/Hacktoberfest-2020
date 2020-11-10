t = int(input())
for i in range(0, t):
    h, u, d = map(int, input().strip().split())
    dis = 0
    steps = 0
    while(True):
        steps = steps + 1
        dis = dis + u
        if(dis < h):
            dis = dis - d
        elif(dis > h):
            break
    print(steps)
