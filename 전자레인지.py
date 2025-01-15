def tb(Time, T):
    count = []
    for i in range(len(Time)):
        cnt = T // Time[i]
        count.append(cnt)
        T -= cnt * Time[i]

        if T != 0:
            print(-1)
        
    return count

T = int(input())
Time = [300, 60, 10]

print(tb(Time, T), end=' ')
