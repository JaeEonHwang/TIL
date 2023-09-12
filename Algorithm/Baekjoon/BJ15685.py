import sys
sys.stdin = open('input.txt', 'r')


from copy import deepcopy

def dragon(k, lst):
    global g
    if k == g:
        return
    else:
        lst1 = deepcopy(lst)
        er, ec = lst1[-1]
        temp = []
        for i in range(len(lst)-1):
            temp.append([0, 0])
            temp[i][0] = er + (ec - lst[i][1])
            temp[i][1] = ec + (er - lst[i][0])
        for i in temp:
            if i not in lst:
                lst.append(i)
        dragon(k+1, lst)


def curve0(r, c, n):
    sr = r
    sc = c
    if n == 0:
        sc += 1
    elif n == 1:
        sr -= 1
    elif n == 2:
        sc -= 1
    else:
        sr += 1
    return [sr, sc]


N = int(input())
all = []
cnt = 0
for i in range(N):
    c, r, d, g = map(int, input().split())
    dots = [[r, c]]
    dots.append(curve0(r, c, d))
    dragon(0, dots)
    for i in dots:
        if i not in all:
            all.append(i)
for r, c in all:
    if [r, c+1] in all and [r+1, c] in all and [r+1, c+1] in all:
        cnt += 1
print(cnt)