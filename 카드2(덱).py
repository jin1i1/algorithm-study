from collections import deque   # 덱 사용

n = int(input())
c = deque([])

for i in range(1, n+1):
    c.append(i)

while len(c) > 1:               # 덱의 길이가 1이 될 때까지 반복
    c.popleft()
    c.append(c.popleft())       # 덱의 첫번째 요소를 제거하고, 그 다음 요소를 덱의 마지막에 추가

print(c[0])