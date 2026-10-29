#  == 피보나치 수열: 단순 재귀 코드 ==
def fibo(x):
    if x==1 or x==2: return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# == 피보나치 수열: 탑다운 다이나믹 프로그래밍 소스 코드 ==
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화 - dp 테이블 생성
d = [0] * 100 

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x==1 or x==2: return 1

    if d[x] != 0: return d[x] # 이미 계산한 적 있는 문제라면 그대로 반환
    # 아직 계산하지 않은 문제라면 
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# == 피보나치 수열: 보텀업 다이나믹 프로그래밍 소스코드 ==
# dp 테이블 생성
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])