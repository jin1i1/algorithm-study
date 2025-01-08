n = int(input())
c = []

for i in range(1, n+1):
    c.append(i)

while len(c) > 1:       # 리스트의 길이가 1이 될 때까지 반복
    c.pop(0)
    c.append(c.pop(0))  # 리스트의 첫번째 요소를 제거하고, 그 다음 요소를 리스트의 마지막에 추가

print(c[0])