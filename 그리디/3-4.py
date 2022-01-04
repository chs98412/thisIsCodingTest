n, m = map(int, input().split())
answer = 0
while n > m:
    q = (n//m)*m
    answer += (n-q)
    n = q

    answer += 1
    n //= m

print(answer+(n-1))
