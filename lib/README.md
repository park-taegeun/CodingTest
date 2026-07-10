# 📚 lib — 알고리즘 라이브러리

문제 풀면서 자주 쓰는 알고리즘/자료구조를 모아두는 곳.
복습용 레퍼런스이자, 로컬 테스트에서 갖다 쓰는 도구 상자.

## 목록

| 파일 | 내용 |
| :--- | :--- |
| `binary_search.py` | 이분 탐색 (기본 / lower_bound / upper_bound) |

## 추가 규칙

- 파일명: 알고리즘 이름 소문자 + 언더스코어 (예: `union_find.py`, `dijkstra.py`)
- 함수마다 무엇을 하는지 주석(docstring)과 예시를 남긴다
- 파일 맨 아래 `if __name__ == "__main__":` 에 간단한 테스트를 넣어둔다

## 사용법

**로컬 테스트에서 import:**

```python
from lib.binary_search import lower_bound

idx = lower_bound([1, 2, 2, 3], 2)  # 1
```

**LeetCode 제출 시:** 필요한 함수를 복사해서 풀이 파일 안에 붙여넣는다.
(LeetCode 채점기는 이 저장소의 lib를 못 불러오므로 import가 아니라 복붙)

## 앞으로 채워갈 것들 (예시)

강의 들으면서 배우는 것들을 하나씩 추가:
- DFS / BFS (그래프 탐색)
- Union-Find (서로소 집합)
- Dijkstra (최단 경로)
- 힙 / 우선순위 큐 활용
- 그 외 자주 쓰게 되는 것들
