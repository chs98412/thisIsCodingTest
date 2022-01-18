from collections import deque
import sys


m, n = map(int, sys.stdin.readline().split())
array = [[0 for col in range(n)] for row in range(m)]

if m+n == 2:
    a = int(sys.stdin.readline())
    if a == 1:
        print("1")
        print("1")
    else:
        print("0")
        print("0")
else:
    data = []
    for i in range(m):
        data.append(list(map(int, sys.stdin.readline().split())))

    answer = 0
    cnt = []

    def bfs(i, j):
        cnt = 0
        stk = [[i, j]]

        while len(stk) > 0:
            temp = stk.pop()
            y, x = temp[0], temp[1]
            if array[y][x] == 0:

                cnt += 1
                array[y][x] = 1

                if x > 0 and data[y][x-1] == 1:
                    stk.append([y, x-1])
                if x+1 < n and data[y][x+1]:
                    stk.append([y, x+1])
                if y > 0 and data[y-1][x]:
                    stk.append([y-1, x])
                if y+1 < m and data[y+1][x]:
                    stk.append([y+1, x])
        return cnt

    for i in range(m):
        for j in range(n):
            if data[i][j] == 1 and array[i][j] == 0:
                cnt.append(bfs(i, j))
    print(len(cnt))

    if len(cnt) == 0:
        print("0")
    else:
        print(max(cnt))
