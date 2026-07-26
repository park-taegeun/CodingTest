# stack 구현
stack = []

stack.append(5) # 삽입
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 삭제
stack.append(1)
stack.append(4)
stack.pop()

print(f"{stack[::-1]}") # 최상단 원소부터 출력
print(f"{stack}") # 최하단 원소부터 출력

# queue 구현
from collections import deque # 큐 이용을 위한 deque 라이브러리 사용

queue = deque()

queue.append(5) # 삽입
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(f"{queue}")
queue.reverse()
print(f"{queue}")

# 재귀 함수(Recursive Function)
# def recursive_function():
#     print(f"재귀 함수를 호출합니다.")
#     recursive_function()

# recursive_function()

def recursive_function(i):
    if i == 100: return # 종료 조건

    print(f"{i}번째 재귀함수에서 {i+1}번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(f"{i}번째 재귀함수를 종료합니다.")

recursive_function(1)

# 팩토리얼 구현 예제
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1: return 1

    return n * factorial_recursive(n - 1)

print(f"반복적으로 구현: {factorial_iterative(5)}")
print(f"재귀적으로 구현: {factorial_recursive(5)}")

# 유클리드 호제법
# 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 합시다.
# 이 때, A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.

def gcd(a, b):
    if a % b == 0: return b
    else: return gcd(b, a % b)

print(f"{gcd(192, 162)}")

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

## 각 노드가 연결된 정보를 표현
graph = [
    [],
    [2, 3, 8], # 1번 노드와 인접한 노드
    [1, 7], # 2번 노드와 인접한 노드
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9 # 각 노드가 방문한 정보를 표현
dfs(graph, 1, visited)

# BFS
from collections import deque

def bfs(graph, start, visited): # 파라미터: 인접 리스트, 시작 노드 번호, 방문 기록 배열
    queue = deque([start]) # start로 시작
    visited[start] = True # 현재 노드를 방문 처리

    while queue: # 큐가 비어있지 않은 동안 반복
        v = queue.popleft() # 큐의 맨 앞 원소를 꺼내서 v에 담음
        print(v, end=' ') # 꺼낸 노드 출력

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [ # grpah: 인접 리스트 -> graph[v]: v번 노드와 직접 연결된 노드들
    [],
    [2, 3, 8], # 1번 노드와 인접한 노드
    [1, 7], # 2번 노드와 인접한 노드
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9 # 방문 기록 배열
bfs(graph, 1, visited)