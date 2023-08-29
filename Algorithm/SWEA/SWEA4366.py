import sys
sys.stdin = open('input.txt', 'r')


def jinsu(number, n):
    lst = []
    while number > 0:
        lst.insert(0, str(number % n))
        number //= n
    return ''.join(lst)


def check_difference(num1, num2):
    if len(num1) != len(num2):
        return False
    countd = 0
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            countd += 1
            if abs(int(num1[i]) - int(num2[i])) > 1:
                return False
            if countd > 2:
                return False
    if countd == 1:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    binary = input()
    ternary = input()
    for t in range(2**len(binary)):
        if check_difference(binary, bin(t)[2:]) and check_difference(ternary, jinsu(t, 3)):
            print(f'#{tc} {t}')
