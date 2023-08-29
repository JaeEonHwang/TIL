import sys
sys.stdin = open('input.txt', 'r')


def game2048(arr, n, move):
    global max_v
    if move == 4:
        for row in range(n):
            for col in range(n):
                if arr[row][col] > max_v:
                    max_v = arr[row][col]
        return max_v
    else:
        for d in range(1, 5):
            for i in range(drt[d][0][0], drt[d][0][1], drt[d][0][2]):
                for j in range(drt[d][1][0], drt[d][1][1], drt[d][1][2]):
                    if arr[i][j] == 0:
                        for k in range(0, n):
                            try:
                                arr[i+k*drt[d][2]][j+k*drt[d][3]] = arr[i+(k+1)*drt[d][2]][j+(k+1)*drt[d][3]]
                            except:
                                arr[i+k*drt[d][2]][j+k*drt[d][3]] = 0
                for j in range(drt[d][1][0], drt[d][1][1], drt[d][1][2]):
                    try:
                        if arr[i][j] == arr[i+drt[d][2]][j+drt[d][3]]:
                            arr[i][j] *= 2
                            for k in range(1, n):
                                try:
                                    arr[i + k * drt[d][2]][j + k * drt[d][3]] = arr[i + (k + 1) * drt[d][2]][j + (k + 1) * drt[d][3]]
                                except:
                                    arr[i + k * drt[d][2]][j + k * drt[d][3]] = 0
                            # try:
                            #     for k in range(j, drt[d][1][1]):
                            #         arr[i][k] = arr[i + drt[d][2]][k + drt[d][3]]
                            # except:
                            #     arr[i][n] = 0
                    except:
                        continue
            return game2048(arr, n, move + 1)


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
# 동, 서, 남, 북 = 1, 2, 3, 4
drt = {1: ((0, N, 1), (N-1, -1, -1), 0, -1), 2: ((0, N, 1), (0, N, 1), 0, 1), 3: ((0, N, 1), (0, N, 1), 1, 0), 4: ((N-1, -1, -1), (0, N, 1),  -1, 0)}
max_v = 0
print(game2048(table, N, 0))