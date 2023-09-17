from collections import Counter


t = int(input())
for _ in range(t):
    input()
    res = {}
    for el in map(int, input().split()):
        res[el] = res.get(el, 0) + 1
        if res[el] > 2:
            print(el)
            break
    else:
        print(-1)


