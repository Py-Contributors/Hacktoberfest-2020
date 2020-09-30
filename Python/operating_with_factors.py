x = list()
y = list()
c = 0
j = 0
N = int(input())

for i in range(N):
    X,K = map(int,input().split())
    
    for t in range(2,X+1):
        if X%t == 0:
            x.append(t)

    for f in range(2,K+1):
        if K%f == 0:
            y.append(f)
    
    for o in x:
        v = o**K
        c += v

    for p in y:
        pg = p*X
        j += pg

    print(c ,j)