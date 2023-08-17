import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    pizza = {0:0}
    for i in range(1, M+1):
        pizza[i] = C[i-1]
    start = 0
    in_progress = []
    cooked = []
    for i in range(N):
        in_progress.append(i+1)
    next_one = N+1
    while len(cooked) < M:
        if pizza[in_progress[start % N]] == 0:
            if in_progress[start % N] != 0:
                cooked.append(in_progress[start % N])
            if next_one > M:
                in_progress[start % N] = 0
            else:
                in_progress[start % N] = next_one
                next_one += 1
        pizza[in_progress[start % N]] //= 2
        start += 1
    print(f'#{tc} {cooked[-1]}')
