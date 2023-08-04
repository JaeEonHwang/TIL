import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T+1):
    P, A, B = list(map(int,input().split()))
    A_trial = 0
    B_trial = 0
    l = 1
    r = P
    while 