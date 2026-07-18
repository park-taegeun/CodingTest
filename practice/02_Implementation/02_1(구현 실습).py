# 행렬 (Matrix)
for i in range(5):
    for j in range(5):
        print(f"({i}, {j})", end=" ")
    print()

# 방향 벡터
# 동 북 서 남
dx = [0, -1, 0, 1] # 행 -> x 좌표가 -1이 되었다는 건 행이 위로 올라감 / +1이 되었다는 건 행이 아래로 내려감
dy = [1, 0, -1, 0] # 열

x, y = 2, 2 # 현재 위치

for i in range(4): # i: 0 ~ 3
    nx = x + dx[i]
    ny = y + dy[i]
    print(f"{nx}, {ny}")