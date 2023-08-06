import sys

stdin = open("input.txt", "r")

data = []
n = int(sys.stdin.readlines())
data.append(list(map(int,sys.stdin.readlines().split())) for _ in range(n))

print(data)