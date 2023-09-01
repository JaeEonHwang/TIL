import sys
sys.stdin = open('input.txt', 'r')

from copy import deepcopy


def game2048(k):
    global cnt
    global max_v
    if k == 5:
        for row in range(N):
            if max(arrs[5][row]) > max_v:
                max_v = max(arrs[5][row])
        return

    for i in range(4):
        if arrs[k+1] != arrs[k]:
            arrs[k + 1] = deepcopy(arrs[k])
            arr = arrs[k + 1]
        else:
            arr = arrs[k + 1]
        if i == 0:
            for row in range(N):
                for col in range(N-1, 0, -1):
                    if arr[row][:arr[row].count(0)] == [0] * arr[row].count(0):
                        break
                    temp = 0
                    while arr[row][col] == 0:
                        temp += 1
                        if temp > N:
                            break
                        for j in range(col):
                            arr[row][col - j] = arr[row][col - j - 1]
                        arr[row][0] = 0
                for col in range(N - 1, 0, -1):
                    if arr[row][col] == arr[row][col-1] and arr[row][col] != 0:
                        arr[row][col] *= 2
                        for j in range(1, col):
                            arr[row][col - j] = arr[row][col - j - 1]
                            if arr[row][col - j - 1] == 0:
                                break
                        arr[row][0] = 0
        elif i == 1:
            for row in range(N):
                for col in range(N - 1):
                    if arr[row][-arr[row].count(0):] == [0] * arr[row].count(0):
                        break
                    temp = 0
                    while arr[row][col] == 0:
                        temp += 1
                        if temp > N:
                            break
                        for j in range(N - 1 - col):
                            arr[row][col+j] = arr[row][col + j + 1]
                        arr[row][-1] = 0
                for col in range(N - 1):
                    if arr[row][col] == arr[row][col+1] and arr[row][col] != 0:
                        arr[row][col] *= 2
                        for j in range(1, N - 1 - col):
                            arr[row][col + j] = arr[row][col + j + 1]
                            if arr[row][col + j + 1] == 0:
                                break
                        arr[row][-1] = 0
        elif i == 2:
            for col in range(N):
                for row in range(N - 1, 0, -1):
                    temp = 0
                    while arr[row][col] == 0:
                        temp += 1
                        if temp > N:
                            break
                        for j in range(row):
                            arr[row-j][col] = arr[row-j-1][col]
                        arr[0][col] = 0
                for row in range(N - 1, 0, -1):
                    if arr[row][col] == arr[row - 1][col] and arr[row][col] != 0:
                        arr[row][col] *= 2
                        for j in range(1, row):
                            arr[row-j][col] = arr[row-j-1][col]
                            if arr[row-j-1][col] == 0:
                                break
                        arr[0][col] = 0
        elif i == 3:
            for col in range(N):
                for row in range(N-1):
                    temp = 0
                    while arr[row][col] == 0:
                        temp += 1
                        if temp > N:
                            break
                        for j in range(N-1-row):
                            arr[row + j][col] = arr[row + j + 1][col]
                        arr[-1][col] = 0
                for row in range(N-1):
                    if arr[row][col] == arr[row+1][col] and arr[row][col] != 0:
                        arr[row][col] *= 2
                        for j in range(1, N-1-row):
                            arr[row+j][col] = arr[row+j+1][col]
                            if arr[row+j+1][col] == 0:
                                break
                        arr[-1][col] = 0
        game2048(k + 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
arrs = [[]] * 6
arrs[0] = board
game2048(0)
print(max_v)