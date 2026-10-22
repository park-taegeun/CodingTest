# 이진 탐색 소스코드: 재귀적 구현
def binary_search(array, target, start, end):
    if start > end: return None
    mid = (start + end) // 2

    if array[mid] == target: return mid
    elif array[mid] > target: return binary_search(array, target, start, mid-1) # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else: return binary_search(array, target, mid+1, end) # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인

n, target = list(map(int, input().split())) # 원소의 개수, 찾고자 하는 값 입력 받기
array = list(map(int, input().split())) # 전체 원소 입력 받기

result = binary_search(array, target, 0, n-1)

if result == None: print(f"원소가 존재하지 않습니다.")
else: print(f"{result+1}")

# bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
# 1 2 4 4 8 이라는 배열이 존재할 때 bisect_left(a, 4)를 하면 인덱스 2가 반환되며 bisect_right(a, 4)를 하면 인덱스 4가 반환

# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4)) # 값이 4인 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 값이 [-1, 3] 범위에 있는 데이터 개수 출력

# 파라메트릭 서치
# - 최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법
# ex.. 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있음