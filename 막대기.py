n = int(input()) # 막대기 개수 입력받기 정수 N (2 ≤ N ≤ 100,000)
h = [int(input()) for _ in range(n)] # 막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)
cnt = 0 # 보이는 막대기의 개수
max_h = 0 # 가장 높은 막대기의 높이

for i in range(n-1, -1, -1): # 입력받은 막대기 높이를 가장 마지막에 입력받은 막대기부터 첫번째 막대기까지 역방향으로 반복 - 스택
    if h[i] > max_h:
        cnt += 1
        max_h = h[i]

print(cnt)