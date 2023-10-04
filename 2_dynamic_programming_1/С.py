from copy import deepcopy
from itertools import accumulate


N, M = map(int, input().split())
mtrx = [list(map(int, input().split())) for _ in range(N)]
max_path = deepcopy(mtrx)
max_path[0] = list(accumulate(mtrx[0]))

for j in range(1, N):
    max_path[j][0] += max_path[j - 1][0]


for i in range(1, N):
    for j in range(1, M):
        max_path[i][j] = mtrx[i][j] + max(max_path[i][j - 1], max_path[i - 1][j])

print(max_path[-1][-1])

revert_path = ''
i, j = N - 1, M - 1
while i and j:
    if max_path[i][j] - mtrx[i][j] == max_path[i][j - 1]:
        revert_path += 'R'
        j -= 1
    else:
        revert_path += 'D'
        i -= 1
revert_path += 'R' * j + 'D' * i

print(*revert_path[::-1])
