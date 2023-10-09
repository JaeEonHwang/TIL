import matplotlib.pyplot as plt

# 예제1: x, y가 같을 때
# plt.plot([1, 2, 3, 4])
# plt.show()

# 참고: 지금까지 그렸던 plot 지우기
plt.clf()

# 예제2: x, y가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
y2 = [1, 2, 3, 4]
plt.plot(x, y)
plt.plot(x, y2)
# plt.show()
plt.clf()

# 예제3: 제목 + 각 축의 설명
plt.plot(x, y)
plt.title('Test Graph')
# 한글 쓰고 싶으면 추가적인 세팅이 필요

# x, y축
plt.xlabel('x label')
plt.ylabel('y label')
# plt.show()


# 파일로 저장하기
plt.savefig('filename.png')
# 저장하려면 plt.show()하면 안 됨, 출력되는 순간 지워짐