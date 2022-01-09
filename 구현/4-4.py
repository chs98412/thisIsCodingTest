n, m = 4, 4
x, y, d = 1, 1, 0
map_real = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

map = []
for i in range(n):
    map.append([0 for i in range(m)])

rotation = [[-1, 0], [0, -1], [1, 0], [0, 1]]

answer = 1
while True:
    ck = False
    for i in range(4):
        d -= 1
        if d < 0:
            d = 3

        x_temp = x+rotation[d][1]
        y_temp = y+rotation[d][0]
        if x_temp >= 0 and x_temp < m and y_temp >= 0 and y_temp < n:
            if map[y_temp][x_temp] == 0 and map_real[y_temp][x_temp] == 0:
                map[y_temp][x_temp] = 1
                x = x_temp
                y = y_temp
                ck = True
                answer += 1
                break
    if ck == False:
        break

print(answer)
