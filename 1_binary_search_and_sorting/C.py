n, k = map(int, input().split())
a, b = (tuple(map(int, input().split())) for _ in range(2))


def BinSearch(x, a, l, r):
    if r - l < 2:
        return min(a[l], a[r], key=lambda y: (abs(x - y), y))
    if x <= a[l]:
        return a[l]
    if x >= a[r]:
        return a[r]

    mid = (l + r) // 2

    if a[l] < x <= a[mid]:
        return BinSearch(x, a, l, mid)
    if a[mid] < x < a[r]:
        return BinSearch(x, a, mid, r)


for x in b:
    print(BinSearch(x, a, 0, len(a) - 1))
