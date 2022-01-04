
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

answer = 0
cnt = 0
data.sort(reverse=True)
for i in range(m):
    if cnt < k:
        answer += data[0]
        cnt += 1
    else:
        cnt = 0
        answer += data[1]


print(answer)


# 시간복잡도 개선

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

answer = 0
cnt = 0
data.sort(reverse=True)
print((m//(k+1)))
answer += data[0]*(m//(k+1))*k
answer += data[0]*(m % (k+1))
answer += data[1]*(m//(k+1))
print(answer)
