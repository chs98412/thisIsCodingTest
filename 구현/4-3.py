inp = str(input())
answer = 0
idx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = idx.index(inp[0])
y = int(inp[1])

calc = [[2, 1], [2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2], [-2, 1], [-2, -1]]

for i in calc:
    x_temp = x+i[0]
    y_temp = y+i[1]
    if x_temp > 0 and x_temp < 9 and y_temp > 0 and y_temp < 9:
        answer += 1
print(answer)
