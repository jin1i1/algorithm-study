n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
S = 0

for i in range(n):
    S += a[i] * b[i]

print(S)