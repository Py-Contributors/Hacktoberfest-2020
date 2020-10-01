#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    n = n - 1
    m = (int(n / 2), int(n / 2))
    p_poss = [(0, 0), (n, 0), (0, n), (n, n)]
    p = [x for x in p_poss if grid[x[0]][x[1]] == 'p']

    diff = [a - b for a, b in zip(m, p[0])]
    steps = sum(map(abs, diff))

    for i in range(steps):
        if diff[0] > 0:
            command = 'UP'
            diff[0] += -1
        elif diff[0] < 0:
            command = 'DOWN'
            diff[0] += 1
        elif diff[1] > 0:
            command = 'LEFT'
            diff[1] += -1
        elif diff[1] < 0:
            command = 'RIGHT'
            diff[1] += 1
        print(command)


# print all the moves here


displayPathtoPrincess(3, [['-', '-', 'p'], ['-', 'm', '-'], ['-', '-', '-']])
