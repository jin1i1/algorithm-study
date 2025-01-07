#과제 안 내신 분?

arr = [int(input()) for _ in range(28)] # 과제를 제출한 학생들의 출석번호
n_arr = [] # 과제를 제출하지 않은 학생들의 춣석석번호

for i in range(1,31): # 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)
    if i not in arr:
        n_arr.append(i) #과제를 제출하지 않은 학생들의 출석번호를 n_arr에 추가

print(min(n_arr)) #제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력
print(max(n_arr)) #제출하지 않은 학생의 출석번호 중 가장 큰 것을 출력
