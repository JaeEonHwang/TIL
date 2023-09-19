def backtracking(cnt):
    global path
    global result

    # 종료 조건
    if cnt == M:
        print(result)
        return

    for i in range(1, N + 1):
        # 중복 방지 가지 치기
        if path[i] == 1:
            continue

        path[i] = 1
        result.append(arr[i])
        backtracking(cnt+1)
        path[i] = 0
        result.pop()



N, M = 4, 3
# print(N,M)
arr = [i for i in range(N+1)]
# print(arr)
path = [0] * (N + 1)
result = []
backtracking(0)
