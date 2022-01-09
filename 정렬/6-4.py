data = list(map(int, input().split()))

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for i in range(data[1]):
    list1[list1.index(min(list1))], list2[list2.index(
        max(list2))] = list2[list2.index(max(list2))], list1[list1.index(min(list1))]

print(list1)
