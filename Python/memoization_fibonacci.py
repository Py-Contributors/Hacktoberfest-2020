known = {}
def fib(n):
    if n in known:
        return known[n]
    
    if n == 1:
        value =1 
    elif n == 2:
        value =1
    elif n>2:
        value =  fib(n-1) + fib(n-2)
    known[n] = value
    return value

print(fib(1000))