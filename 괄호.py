T = int(input())                    # 테스트 데이터 개수

for _ in range(T):
    arr = []                        # 괄호 문자열 입력받을 리스트
    str = input()                   # 괄호 문자열 입력받기
    
    for i in str:                   # 괄호 문자열을 반복
        if i == '(':                # 괄호 문자열이 '('이면
            arr.append('(')         # 리스트에 추가
        elif i == ')':              # 괄호 문자열이 ')'이면
            if len(arr) == 0:
                arr.append(')')     # 리스트에 추가
                break
            else:
                arr.pop()           # 리스트의 마지막 요소를 제거

    if len(arr) != 0:               # 리스트의 길이가 0이 아니면
        print('NO') 
    else:
        print('YES')


