def fibo(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x + y

print(sum(fibo(10)))
print(list(fibo(10)))

