n, m = map(int, input().split())

list_data = []
for i in range(n):
    list_data.append(list(map(int, input().split())))

temp = min(list_data[0])
for a in list_data:
    q = min(a)
    if q > temp:
        temp = q

print(temp)

n, m = map(int, input().split())

temp = 0

for i in range(n):
    q = min(list(map(int, input().split())))
    if q > temp:
        temp = q


print(temp)
