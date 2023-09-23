import sys
sys.stdin = open('input.txt', 'r')

from math import floor
import sys
sys.setrecursionlimit(20000)


def tornado(r, c, d):
    global total
    temp = 0
    if r == 0 and c == 0:
        print(total)
        return
    else:
        dr = delta[d][0]
        dc = delta[d][1]
        r += dr
        c += dc
        y = arr[r][c]
        temp += wind(y, r, c, 2 * dr, 2 * dc, 0.05)
        temp += wind(y, r, c, 2 * dc, 2 * dr, 0.02)
        temp += wind(y, r, c, - 2 * dc, - 2 * dr, 0.02)
        temp += wind(y, r, c, dc, dr, 0.07)
        temp += wind(y, r, c, -dc, -dr, 0.07)
        if dr == 0:
            temp += wind(y, r, c, dc, dc, 0.1)
            temp += wind(y, r, c, -dc, dc, 0.1)
            temp += wind(y, r, c, dc, -dc, 0.01)
            temp += wind(y, r, c, -dr, -dc, 0.01)
        else:
            temp += wind(y, r, c, dr, dr, 0.1)
            temp += wind(y, r, c, dr, -dr, 0.1)
            temp += wind(y, r, c, -dr, dr, 0.01)
            temp += wind(y, r, c, -dr, -dr, 0.01)
        wind(arr[r][c] - temp, r, c, dr, dc, 1)
        arr[r][c] = 0
    if (r - c == 1 and r <= N // 2) or r + c == N-1 or (r - c == 0 and r > N // 2):
        d = (d + 1) % 4
    tornado(r, c, d)


def wind(center, r, c, dr, dc, ratio):
    global total
    if 0 <= r + dr < N and 0 <= c + dc < N:
        arr[r + dr][c + dc] += floor(center * ratio)
    else:
        total += floor(center * ratio)
    return floor(center * ratio)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((0, -1), (1, 0), (0, 1), (-1, 0))
total = 0
tornado(N // 2, N // 2, 0)