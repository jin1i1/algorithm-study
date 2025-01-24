def lotto(arr, s, idx, x):
  if x == 6:
    print(*arr)
    return
  
  for i in range(idx, len(s)):
    arr[x] = s[i]
    lotto(arr, s, i + 1, x + 1)

while True:
  s = list(map(int, input().split()))
  k = s[0]
  if k == 0:
    break
  arr = [0] * 6
  lotto(arr, s[1:], 0, 0)
  print()