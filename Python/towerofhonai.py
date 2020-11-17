def movetower(n,source,aux,dest):
    if n == 1:
        print(source + '-->' + dest)
        return
    movetower(n-1,source,dest,aux)
    print(source + '-->' + dest)
    movetower(n-1, aux, source, dest)
n=int(input())
print(movetower(n,'a','b','c'))
