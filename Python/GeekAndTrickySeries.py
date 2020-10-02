t = int(input())
for i in range(0, t):
    series = [7]
    n = int(input())
    for j in range(1, n):
        series.append((series[j - 1] * 2) + j)
    print(series[n - 1] % 1000000007)
