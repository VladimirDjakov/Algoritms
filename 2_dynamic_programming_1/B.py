def solve(n, a, b, c):
    turn = [0] * n  # turn[i] - минимальное время обслуживания очереди, при условии что i-ый человек последний
    turn[0] = a[0]
    if n == 1:
        return turn[0]
    turn[1] = min(a[0] + a[1], b[0])
    if n == 2:
        return turn[1]
    turn[2] = min(a[0] + a[1] + a[2], a[0] + b[1], b[0] + a[2], c[0])
    if n == 3:
        return turn[2]
    for i in range(3, n):
        turn[i] = min(turn[i - 3] + c[i - 2], turn[i - 2] + b[i - 1], turn[i - 1] + a[i])
    return turn[-1]


n = int(input())
a, b, c = [0] * n, [0] * n, [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

print(solve(n, a, b, c))
