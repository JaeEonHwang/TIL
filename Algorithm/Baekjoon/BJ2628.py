width, height = map(int, input().split())
N = int(input())
width_list = [0, width]
height_list = [0, height]
for _ in range(N):
    direction, cut = map(int, input().split())
    if direction == 0:
        height_list.append(cut)
    else:
        width_list.append(cut)
max_width = 0
max_height = 0