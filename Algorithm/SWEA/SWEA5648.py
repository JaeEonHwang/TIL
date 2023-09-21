import sys

sys. stdin = open('input.txt', 'r')

T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip())
    atoms = []
    for _ in range(N):
        a = list(map(int, input().strip().split()))
        a[0] *= 2
        a[1] *= 2
        atoms.append(a)
    d = ((0, 1), (0, -1), (-1, 0), (1, 0)) #상하좌우 x, y
    total = 0
    cnt = 0
    while len(atoms) >= 2:
        pops = []
        # atoms.sort(reverse=True)
        for i in range(len(atoms)):
            if atoms[i][0] not in list(range(-2000, 2001)) or atoms[i][1] not in list(range(-2000, 2001)) or not atoms[i][3]:
                pops.append(i)
                continue
            atoms[i][0] += d[atoms[i][2]][0]
            atoms[i][1] += d[atoms[i][2]][1]
        for i in range(len(atoms)):
            change = False
            for j in range(1 + i, len(atoms)):
                if (atoms[i][0], atoms[i][1]) == (atoms[j][0], atoms[j][1]) and atoms[j][3]:
                    total += atoms[j][3]
                    cnt += 1
                    atoms[j][3] = 0
                    change = True
                    pops.append(j)
            if change:
                total += atoms[i][3]
                cnt += 1
                atoms[i][3] = 0
                pops.append(i)
        if cnt > N - 1:
            break
        pops.sort(reverse=True)
        for i in pops:
            del atoms[i]
    print(f'#{tc} {total}')
