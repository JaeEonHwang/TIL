import sys
sys.stdin = open('input.txt', 'r')

def go_straight(row,col,arr,direction):
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(arr)