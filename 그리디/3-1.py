def a(n):
    a = 0
    l = [500, 100, 50, 10]
    for i in l:
        a += n//i
        n = n % i

    return a


print(a(1260))
print(a(260))
print(a(60))
print(a(10))
print(a(0))
