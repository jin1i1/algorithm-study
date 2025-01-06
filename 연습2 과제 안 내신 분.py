#과제 안 내신 분?

arr = [int(input()) for _ in range(28)]
n_arr = []

for i in range(1,31):
    if i not in arr:
        n_arr.append(i)

print(min(n_arr))
print(max(n_arr))
