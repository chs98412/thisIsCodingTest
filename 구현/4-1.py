# n = int(input())

# data = list(map(str, input().split()))
# x = 1

# y = 1
# for i in data:
#     if i == 'R' and x < n:
#         x += 1
#     elif i == 'L' and x > 1:
#         x -= 1
#     elif i == 'U' and y > 1:
#         y -= 1
#     elif i == 'D' and y < n:
#         y += 1

# print(x, y)


# 짧게


n = int(input())

data = list(map(str, input().split()))

xy = [1, 1]
calc = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}

for i in data:
    temp = xy
    xy = [xy[0]+calc[i][0], xy[1]+calc[i][1]]
    if xy[0] < 1 or xy[0] > n or xy[1] < 1 or xy[1] > n:
        xy = temp
print(xy[0], xy[1])
