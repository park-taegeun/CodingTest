# == pro ==
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이 때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

# 입력 조건: 첫 째줄에 하나의 문자열 S가 주어집니다.
# 출력 조건: 첫 째줄에 문제에서 요구하는 정답을 출력합니다.

# == sol (내가 푼 것) ==
input_str = str(input()) # 입력 문자열 (알파벳 대문자 + 숫자)
num_list = [c for c in input_str if c.isdigit()] # 숫자 리스트
alphabet_list = [c for c in input_str if c.isalpha()] # 알파벳 리스트

# 출력 로직
alphabet_sorted_list = sorted(alphabet_list) # 알파벳 리스트 정렬

total_sum = 0
for i in range(len(num_list)): total_sum += int(num_list[i])

# 출력
for i in range(len(alphabet_sorted_list)):
    print(f"{alphabet_sorted_list[i]}", end="")

if num_list: print(f"{total_sum}")

# == sol (권장 방식) ==
input_str = input()
num_list = [c for c in input_str if c.isdigit()]
alphabet_list = [c for c in input_str if c.isalpha()]

result = ''.join(sorted(alphabet_list))
if num_list:
    result += str(sum(int(c) for c in num_list))

print(f"{result}")