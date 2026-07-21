# == pro ==
# 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있습니다.
# 가장 왼쪽 위 좌표는 (1, 1)이며 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다. 
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1) 입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하며 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있습니다. 각 문자의 의미는 다음과 같습니다.

# L: 왼쪽으로 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위쪽으로 한 칸 이동
# D: 아래쪽으로 한 칸 이동

# 이 때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다.
# 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시됩니다.

# 입력 조건
# - 첫 째줄에 공간의 크기를 나타내는 N이 주어집니다.
# - 둘 째줄에 여행가 A가 이동할 계획서 내용이 주어집니다.

# 출력 조건: 첫 째줄에 여행가 A가 최종적으로 도착할 지점의 (X, Y)를 공백을 기준으로 구분하여 출력합니다.

# == sol (내가 푼 것) ==
n = int(input()) # 공간 크기
move_list = list(map(str, input().split(" "))) # 이동 계획서

# 시작 위치
state_x = 1
state_y = 1

# 방향 벡터
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 이동 로직
for i in move_list:
    if i == 'L': 
        if state_y + dy[2] < 1: continue
        state_y += dy[2]

    elif i == 'R': 
        if state_y + dy[0] > n: continue
        state_y += dy[0]

    elif i == 'U':
        if state_x + dx[1] < 1: continue
        state_x += dx[1]

    elif i == 'D':
        if state_x + dx[3] > n: continue
        state_x += dx[3]

print(f"이동 후 마지막 위치: ({state_x}, {state_y})")

# == sol (권장) ==
n = int(input()) # 공간 크기
move_list = list(map(str, input().split(" "))) # 이동 계획서

# 시작 위치
state_x = 1
state_y = 1

moves = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}

for command in move_list:
    dx, dy = moves[command]
    
    nx = state_x + dx
    ny = state_y + dy

    if (1<= nx <= n) and (1 <= ny <= n):
        state_x = nx
        state_y = ny

    else: continue

print(f"이동 후 마지막 위치: ({state_x}, {state_y})")