import sys
sys.stdin = open('input.txt', 'r')

'''
for _ in range(4):
    ans = ''
    x = []
    y = []
    xy = list(map(int, input().split()))
    # x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    for i in range(4):
        x.append(xy[2*i])
        y.append(xy[2*i+1])
    arr = [[0] * (max(x)+2) for _ in range(max(y)+2)]
    for i in range(2):
        for row in range(y[2*i], y[2*i+1]):
            for col in range(x[2*i], x[2*i+1]):
                arr[row][col] += 1

    for row in arr:
        if 2 in row:
            ans = 'a'
            break

    for row in range(y[0]-1, y[1]+1):
        arr[row][x[0] - 1] += 1
        arr[row][x[1] + 1] += 1
    for col in range(x[0], x[1]):
        arr[y[0] - 1][col] += 1
        arr[y[1] + 1][col] += 1

    count2 = 0
    for row in arr:
        for col in row:
            if col == 2:
                count2 += 1

    if ans == '':
        if count2 == 0:
            ans = 'd'
        elif count2 == 1:
            ans = 'c'
        else:
            ans = 'b'

    print(ans)
'''

for _ in range(4):
    ans = ''
    x = []
    y = []
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if x3 < x1:
        x1, x3 = x3, x1
        y1, y3 = y3, y1
        x2, x4 = x4, x2
        y2, y4 = y4, y2




