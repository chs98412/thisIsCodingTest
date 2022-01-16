import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(sys.stdin.readline().rstrip()))

array = [[0 for col in range(n)] for row in range(n)]

answer = [0, 0]


def dfs2(y, x):
    array[y][x] = 1
    if y+1 < n and array[y+1][x] == 0 and (data[y+1][x] == data[y][x] or (data[y+1][x] == "R" and data[y][x] == "G") or (data[y+1][x] == "G" and data[y][x] == "R")):
        dfs(y+1, x)
    if x+1 < n and array[y][x+1] == 0 and (data[y][x+1] == data[y][x] or (data[y][x+1] == "R" and data[y][x] == "G") or (data[y][x+1] == "G" and data[y][x] == "R")):
        dfs(y, x+1)

    if y > 0 and array[y-1][x] == 0 and (data[y-1][x] == data[y][x] or (data[y-1][x] == "R" and data[y][x] == "G") or (data[y-1][x] == "G" and data[y][x] == "R")):
        dfs(y-1, x)
    if x > 0 and array[y][x-1] == 0 and (data[y][x-1] == data[y][x] or (data[y][x-1] == "R" and data[y][x] == "G") or (data[y][x-1] == "G" and data[y][x] == "R")):
        dfs(y, x-1)
    return 1


def dfs(y, x):
    array[y][x] = 1
    if y+1 < n and array[y+1][x] == 0 and data[y+1][x] == data[y][x]:
        dfs(y+1, x)
    if x+1 < n and array[y][x+1] == 0 and data[y][x+1] == data[y][x]:
        dfs(y, x+1)

    if y > 0 and array[y-1][x] == 0 and data[y-1][x] == data[y][x]:
        dfs(y-1, x)
    if x > 0 and array[y][x-1] == 0 and data[y][x-1] == data[y][x]:
        dfs(y, x-1)
    return 1


for i in range(len(data)):
    for j in range(len(data[0])):
        if array[i][j] == 0:
            answer[0] += dfs(i, j)

array = [[0 for col in range(n)] for row in range(n)]

for i in range(len(data)):
    for j in range(len(data[0])):
        if array[i][j] == 0:
            answer[1] += dfs2(i, j)
            print(array)

print(answer[0], answer[1])
