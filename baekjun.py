import sys

n = int(sys.stdin.readline())
data = sys.stdin.readline().split()
n = int(sys.stdin.readline())

data2 = sys.stdin.readline().split()


data.sort()
for i in data2:
    lst = data
    l, r = 0, len(data)-1
    while True:
        num = (r+l)//2
        temp = lst[num]
        if temp == i:
            print(1)
            break
        if r < l:
            print(0)
            break
        if temp > i:
            r = num-1
        else:
            l = num+1
