import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T + 1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    delta_row = [1,-1,0,0]
    delta_col = [0,0,1,-1]
    max_pop = 0
    for row in range(1,N-1):
        for col in range(1,M-1):
            pop = arr[row][col]
            for i in range(4):
                pop += arr[row+delta_row[i]][col+delta_col[i]]
            if pop > max_pop:
                max_pop = pop
    print(f'#{tc} {max_pop}')