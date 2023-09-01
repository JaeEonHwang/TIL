import sys
sys.stdin = open('input.txt', 'r')


def oasis2():
    global visit
    global dist
    global cp1, cp2, addidx
    delta = (-1, 1, -M, M)
    for j in range(cp1, cp2):
        a = visit[j]
        for d in delta:
            if 0 <= a + d < N * M:
                if a + d not in visit:
                    if arr[a + d] == 'W':
                        return
                    else:
                        visit[addidx] = a + d
                        addidx += 1
    dist += 1
    cp1 = cp2
    cp2 = addidx
    oasis2()


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = ''
    for _ in range(N):
        arr1 += input()
    total = 0
    for i in range(N*M):
        if N*M//2 >= i:
            arr = arr1[-(N*M//2 - i):] + arr1[:-(N*M//2 - i)]
        else:
            arr = + arr1[:i - N*M//2]
        if arr1[i] == 'L':
            arr = arr1[:N*M//2 - i]
        visit = [-1] * M * N
        visit[0] = i
        dist = 1
        cp1 = 0
        cp2 = 1
        addidx = 1
        oasis2()
        total += dist
    print(f'#{tc} {total}')
