def f(n, x, v, t):
    distances = [x[i] + v[i] * t for i in range(n)]
    return max(distances) - min(distances)


def ternary_search(n, x, v):
    left = 0
    right = 2e7
    eps = 1e-10
    while right - left > eps or 2 * (right - left) / right > eps:
        mid = (left + right) / 2
        first = f(n, x, v, mid)
        second = f(n, x, v, mid + (right - mid) / 1000)
        if first < second:
            right = mid
        else:
            left = mid

    t = (left + right) / 2
    l = f(n, x, v, t)
    return t, l


n = int(input())
x, v = [0] * n, [0] * n
for i in range(n):
    x[i], v[i] = map(int, input().split())

result_time, result_dist = ternary_search(n, x, v)
print(result_time, result_dist)