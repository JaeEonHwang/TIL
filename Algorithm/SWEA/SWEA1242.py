import sys
sys.stdin = open('input.txt', 'r')


def password_sum(lst):
    global ratio
    temp = []
    for j in range(8):
        number = ''
        try:
            for i in range(7):
                number = lst[-1 - ratio * i - 7 * j * ratio] + number
            temp.insert(0, secret_code[number])
        except:
            ratio -= 1
            return password_sum(lst)

    my_sum = 0
    for i in range(4):
        my_sum += (temp[2 * i] * 3)
        my_sum += temp[2 * i + 1]
    if my_sum % 10 == 0:
        return sum(temp)
    else:
        return 0


secret_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,\
               '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    arr = []
    for row in range(N):
        arr.append(list(input().strip()))
    for row in range(N-1, 0, -1):
        for col in range(M):
            if arr[row][col] == arr[row-1][col]:
                arr[row][col] = '0'
    new_arr = []
    for row in range(N):
        if int(''.join(arr[row]), 16) != 0:
            new_arr.append(arr[row])
    for row in range(len(new_arr)):
        new_arr[row] = list(''.join(new_arr[row]).strip('0'))
        new_arr[row].insert(0, '0')

    total = 0
    for row in new_arr:
        binary = []
        for i in row:
            for j in range(3, -1, -1):
                binary.append('1' if int(i, 16) & 1 << j else '0')

        while sum(map(int, binary)) != 0:
            binary = list(''.join(binary).strip('0'))
            while len(binary) % 56 != 0:
                binary.insert(0, '0')
            count1 = 0
            idx1 = -1
            while binary[idx1] == '1':
                count1 += 1
                idx1 -= 1
            ratio = min(count1, len(binary) // 14)
            total += password_sum(binary)
            del binary[len(binary) - ratio * 56:]
    print(f'#{tc} {total}')




