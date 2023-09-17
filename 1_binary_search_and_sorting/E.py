def f(t):
    distances = tuple(x_i + v_i * t for x_i, v_i in zip(x, v))
    return max(distances) - min(distances)


def ternarySearch(l, r):
    t = (r + l) / 2
    if r - l < eps * max(1, t):
        return t

    a, b = (2 * l + r) / 3, (l + 2 * r) / 3
    if f(a) < f(b):
        return ternarySearch(l, b)
    else:
        return ternarySearch(a, r)


n = int(input())
x, v = [0] * n, [0] * n
for i in range(n):
    x[i], v[i] = map(int, input().split())

eps = 1e-6 / max(v + [1.])
t_max = 10 ** 9
t_best = ternarySearch(0, t_max)
print(t_best, f(t_best))
