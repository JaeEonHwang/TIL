# N과 M(2)
# pop 안 쓰고 풀어보기

from copy import copy


def backtracking(cnt, k):
    global result

    if cnt == M:
        print(*result)
        return

    for i in range(k, N + 1):
        result[cnt] = i
        backtracking(cnt+1, i + 1)


N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = [0] * M
ans = []
backtracking(0, 1)
