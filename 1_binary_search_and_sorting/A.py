def merge(x: list, l: int, mid: int, r: int):
    i, j = 0, 0
    res = []
    while l + i < mid and mid + j < r:
        if x[l + i] < x[mid + j]:
            res.append(x[l + i])
            i += 1
        else:
            res.append(x[mid + j])
            j += 1

    while l + i < mid:
        res.append(x[l + i])
        i += 1

    while mid + j < r:
        res.append(x[mid + j])
        j += 1

    x[l: l + i + j] = res


def mergeSort(x: list, l: int, r: int):
    if l + 1 >= r:
        return
    mid = (l + r) // 2
    mergeSort(x, l, mid)
    mergeSort(x, mid, r)
    merge(x, l, mid, r)

n = int(input())
x = list(map(int, input().split()))
mergeSort(x, 0, n)
print(*x)
