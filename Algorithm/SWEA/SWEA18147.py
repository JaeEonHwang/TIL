import sys
sys.stdin = open("input.txt", "r")


def my_extend(lst1,lst2):
    new_list = [0] * (len(lst1) + len(lst2))
    for i in range(len(lst1)):
        new_list[i] = lst1[i]
    for i in range(len(lst2)):
        new_list[i+len(lst1)] = lst2[i]
    return new_list

def my_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx],lst[i]
        


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    whole_list = []
    for i in range(N):
        numbers = list(map(int,input().split()))
        whole_list = my_extend(whole_list,numbers)
    
    arr = [[0]*N for _ in range(N)]

    for i in range(N):
        arr[0][i] = whole_list[i]
    row = 0
    col = N-1
    for i in range(1,N):
        if i % 2 == 1:
            for j in range((N(i) - i(i-1)/2) * 2 - 5, (N(i) - i(i-1)/2) * 2 - 5 + N - i):
                arr[row-i][col] = 
                           (N(i+1) - i(i+1)/2) * 2 - 5):

        

    # row_end = 4
    # col_end = 4
    # row = 0
    # col = 0
    # arr = [[0] * N for _ in range(N)]
    # for row in range(N):
    #     for col in range(N):
    #         arr[row][col]

    