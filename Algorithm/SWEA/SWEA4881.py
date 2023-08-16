import sys

sys.stdin = open('input.txt', 'r')


def backtracking(row, col, N, s):
    global minimun
    global arr

    if row == N:
        if minimun > s:
            minimun = s
    else:
        selected[col] = True
        print(arr[row][col], row, col)
        s += arr[row][col]
        candidates = constructs_candidates(selected)
        if candidates:
            for i in candidates:
                row_count[row] += 1
                backtracking(row+1, i, N, s)
        else:
            for row in range(N):
                if row_count[row] != (N - 1 - row) * factorial(N) / factorial(N-1-row):
                    selected[row] = False
            backtracking(row + 1, col, N, s)


def constructs_candidates(selected):
    lst = []
    for i in range(len(selected)):
        if selected[i] == False:
            lst.append(i)
    return lst


def factorial(m):
    if m == 1 or m == 0:
        return 1
    return m * factorial(m-1)


T = int(input())
for tc in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    row = 0
    minimun = N * 10
    s = 0
    row_count = [0] * N
    for col in range(N):
        selected = [False] * N
        backtracking(row, col, N, 0)
    #print(f'#{tc} {minimun}')
