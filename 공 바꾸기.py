n, m = map(int, input().split())    # N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

b = [i for i in range(1, n+1)]      # 1번부터 N번까지 공이 차례대로 번호가 적힌 것
t = 0

for i in range(m):
    i,j = map(int, input().split()) # (1 ≤ i ≤ j ≤ N)
    t = b[i-1]                      # 공 위치 교환
    b[i-1] = b[j-1]
    b[j-1] = t

for i in range(n):
    print(b[i], end=' ')            # 공의 번호를 공백으로 구분해 출력