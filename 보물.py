n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
S = 0

a.sort()

for i in range(n):
    b_max = max(b)
    S += a[i] * b_max
    b.pop(b.index(b_max))
    
print(S)
