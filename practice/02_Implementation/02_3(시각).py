# == pro ==
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하지오
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
# - 00시 00분 03초
# - 00시 13분 30초

# 반면에 다음은 3이 하나라도 포함되어 있지 않으므로 세면 안 되는 시각입니다.
# - 00시 02분 55초
# - 01시 27분 45초

# 입력 조건: 첫 째줄에 정수 N이 입력됩니다. (0 <= N <= 23)
# 출력 조건: 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력합니다.

# == sol (내가 푼 것) ==
n = int(input()) # 시간
cnt = 0 # 경우의 수
hours = 0 # 시

number_list = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53] # 0 ~ 59 중 3 포함 넘버 리스트

while (hours <= n):
    for minutes in range(60): # minutes: 0 ~ 59
        for secs in range(60): # secs: 0 ~ 59
            if hours in number_list or minutes in number_list or secs in number_list: cnt += 1
            else: continue
    
    hours += 1

print(f"00시 00분 00초 ~ {n}시 59분 59초 중 3이 포함된 시각의 경우의 수는 총 {cnt}개 입니다.")

# == sol (권장 방식) ==
n = int(input())
cnt = 0
hours = 0

while (hours <= n):
    for minutes in range(60):
        for secs in range(60):
            if '3' in str(hours) + str(minutes) + str(secs): cnt += 1
            else: continue
    
    hours += 1

print(f"00시 00분 00초 ~ {n}시 59분 59초 중 3이 포함된 시각의 경우의 수는 총 {cnt}개 입니다.")