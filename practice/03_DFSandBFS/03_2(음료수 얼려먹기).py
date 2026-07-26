# == pro ==
# N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다. 
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것처럼 간주합니다.
# 이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# 다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

# 입력 조건 
# - 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다.
# - 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어집니다.
# - 이 때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.

# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력 조건: 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.

# == sol (내가 푼 것) ==
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(x, y):
    queue = deque() 
    queue.append((x, y)) # append의 파라미터는 1개
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < n and 0<= ny < m) and (not visited[nx][ny]) and (graph[nx][ny] == 0):
                queue.append((nx, ny))
                visited[nx][ny] = True

n, m = map(int, input().split()) # N, M 입력
graph = [] # 격자 담을 리스트

for i in range(n):
    row = [int(x) for x in input()] # 한 행씩 입력 받고
    graph.append(row) # 열 단위로 그래프에 append

visited = [[False] * m for _ in range(n)] # 방문 기록 배열
count = 0 # 아이스크림 개수

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]: # 새로운 아이스크림 시작점 판별
            bfs(i, j) # (i, j)에서 출발해서 상하좌우로 연결된 0들을 전부 방문 처리(visited = True)
            count += 1 

print(f"만들 수 있는 아이스크림 개수: {count}")

# 내가 생각한 bfs 함수의 역할 flow
# 1. 큐 생성 -> 시작점 append -> visited True
# 2. 큐 빌 때까지 반복
# - popleft -> 이웃 판별 로직 -> 조건 통과한 이웃: append + visited True

# 이웃 판별 로직
# 인접 리스트: for i in graph[v]
# 격자: for k in range(4)