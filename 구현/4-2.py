inp = int(input())

answer = 0

h = 0
for i in range(inp+1):
    m = 0
    for j in range(60):
        s = 0
        for k in range(60):
            s += 1
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                answer += 1
        m += 1
    h += 1
print(answer)

# 짧게


inp = int(input())
a = [3, 13, 23]
answer = 0
for i in range(inp+1):
    if i in a:
        answer += 3600
    else:
        answer += 1575
print(answer)
