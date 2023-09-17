from math import sqrt


def f(x): return x ** 2 + sqrt(x + 1)


def criteria(x, y): return round(f(x) - y, 6) == .0


def grad_f(x): return 2 * x + 0.5 / sqrt(x + 1)


y = float(input())
x = sqrt(y)
step = 1
while not criteria(x, y) and step <= 10**5:
    alph = 1 / (y * sqrt(step))
    x -= alph * (f(x) - y) * grad_f(x)
    x = max(0, x)
    step += 1

print(x)
