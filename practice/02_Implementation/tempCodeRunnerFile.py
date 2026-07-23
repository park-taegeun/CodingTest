
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