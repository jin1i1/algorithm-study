n = int(input())
sc = 1000 - n
count = 0 

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    count += sc // coin
    sc %= coin

print(count)