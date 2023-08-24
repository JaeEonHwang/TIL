import sys
sys.stdin = open('input.txt', 'r')

import math
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
T = math.lcm(w, h)
t %= T


