import sys
sys.stdin = open('input.txt', 'r')


# def my_sort(dict):
#     change = 0
#     while True:
#         gap = 0
#         num = len(dict)+1//2
#         for i in range(1, N + 1):
#             if abs(i - dict[i]) > gap or (abs(i - dict[i]) == gap and abs(len(dict)+1//2 - i) > abs(len(dict)+1//2 - num)):
#                 gap = abs(i - dict[i])
#                 num = i
#         if gap == 0:
#             return change
#         else:
#             if num > dict[num]:
#                 for i in range(1, len(dict) + 1):
#                     if num >= dict[i] > dict[num]:
#                         dict[i] -= 1
#                 dict[num] = num
#             else:
#                 for i in range(1, len(dict) + 1):
#                     if num <= dict[i] < dict[num]:
#                         dict[i] += 1
#                 dict[num] = num
#         change += 1
#
#
# N = int(input())
# kids = {}
# # 숫자: 인덱스
# for i in range(1, N + 1):
#     kids[int(input())] = i
#
# print(my_sort(kids))

from collections import deque

def order(s, lst):
    global max_order
    if kids[s] == max(kids[s:]):
        if max_order < len(lst):
            max_order = len(lst)
    else:
        for i in range(s+1, N):
            if lst[-1] < kids[i]:
                lst.append(kids[i])
                order(i, lst)
                lst.pop()


N = int(input())
kids = []
max_order = 1
for _ in range(N):
    kids.append(int(input()))


for i in range(N):
    deq = deque()
    deq.append(kids[i])
    order(i, deq)

print(N - max_order)
