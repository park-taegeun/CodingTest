# == pro ==
# 행복 왕실의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면입니다. 왕실 정원의 특정한 한 칸에 나이트가 서 있습니다.
# 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다.

# 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# 이처럼 8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요.
# 왕실의 정원에 행 위치를 표현할 때는 1부터 8로 표현하며 열 위치를 표현할 때는 a부터 h로 표현합니다.

# 입력 조건
# - 첫 째줄에 8 x 8 좌표 평면 상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
# - 입력 문자는 a1처럼 열과 행으로 이루어진다.

# 출력 조건: 첫 째줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오

# == sol (내가 푼 것) ==
knight_position = str(input()) # 나이트 현재 위치
knight_row = knight_position[:1] # 행
knight_col = int(knight_position[1:]) # 열
cnt = 0 # 경우의 수

row_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # 행 리스트
col_list = [int(i) for i in range(1, 9)] # 열 리스트

for i in range(8):
    if row_list[i] == knight_row: knight_row_num = i # row_list에서 나이트의 행 인덱스

# 이동 가능 여부 판단 로직
if (knight_row_num + 2 <= 7):
    if knight_col + 1 in col_list: cnt += 1
    if knight_col - 1 in col_list: cnt += 1

if (knight_row_num - 2 >= 0):
    if knight_col + 1 in col_list: cnt += 1
    if knight_col - 1 in col_list: cnt += 1

if (knight_col - 2 in col_list):
    if knight_row_num + 1 <= 7: cnt += 1
    if knight_row_num - 1 >= 0: cnt += 1

if (knight_col + 2 in col_list):
    if knight_row_num + 1 <= 7: cnt += 1
    if knight_row_num - 1 >= 0: cnt += 1

print(f"나이트가 {knight_position}에서 움직일 수 있는 경우의 수는 {cnt}개 입니다.")