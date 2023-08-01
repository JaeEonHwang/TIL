import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for i in range(1,T+1):
    K,N,M = list(map(int,input().split()))
    numberM = list(map(int,input().split()))
    charging = 0
    busstop = K
    previous_busstop = 0
    while busstop < 10:
        while busstop not in numberM:
            busstop -= 1
            if busstop == previous_busstop:
                print(f'#{i} 0')
                break
        previous_busstop = busstop
        busstop += K
        charging += 1

    print(f'#{i} {charging}')