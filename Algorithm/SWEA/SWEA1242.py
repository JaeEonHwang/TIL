import sys
sys.stdin = open('input.txt', 'r')


def decode(lst):
    code_check = []
    a = 1
    check = ''.join(lst[-7::a])
    while check not in secret_code.values():
        a += 1
        check = ''.join(lst[-7*a::a])
    while len(code_check) < 8:
        number = ''
        for j in range(7):
            for _ in range(1, a):
                lst.pop()
                lst.insert(0, '0')
                lst.insert(0, '0')
            number = lst.pop() + number
        for j in range(10):
            if number == secret_code[j]:
                code_check.insert(0, j)
                break

    total = 0
    for j in range(4):
        total += (code_check[2 * j] * 3)
        total += code_check[2 * j + 1]
    if total % 10 == 0:
        return sum(code_check)
    else:
        if sum(list(map(int, lst))) == 0:
            return 0
        else:
            decode(lst)


secret_code = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011',\
               5: '0110001', 6: '0101111', 7: '0111011', 8: '0110111', 9: '0001011'}


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in range(N):
        try:
            int(arr[i])
        except:
            if i == 0 or arr[i] != arr[i-1]:
                binary = []
                for z in range(M):
                    for k in range(3, -1, -1):
                        binary.append('1' if int(arr[i][z], 16) & 1 << k else '0')
                while binary[-1] == '0':
                    binary.pop()
                print(decode(binary))