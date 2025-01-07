T = int(input()) # 테스트 데이터 개수
arr = [] # 괄호 문자열 입력받을 리스트


for _ in range(T):
    arr = input()
    if arr == '(':
        arr.append('(')
        if arr == ')':
            arr.pop('(')
        else:
            print('NO')
            break
    else: 
        if len(arr) == 0:
            print('YES')
        else:
            print('NO')


