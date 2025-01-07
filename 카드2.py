
n = int(input())
c = list(range(1, n+1))

while (len(c) > 1):
    c.append(0)
    t = c.pop(0)
    c.append(t)

print(c.pop(0))