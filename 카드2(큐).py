n = int(input())
c = []

for i in range(1, n+1):
    c.append(i)

while len(c) > 1:
    c.pop(0)
    c.append(c.pop(0))

print(c[0])