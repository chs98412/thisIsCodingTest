import operator

inp = int(input())

a = {}

for i in range(inp):
    data = list(map(str, input().split()))
    a[data[0]] = int(data[1])

a = sorted(a.items(), key=operator.itemgetter(1))
print(a)
for i in a:
    print(i[0])
