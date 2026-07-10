"""
이분 탐색 (Binary Search)

정렬된 배열에서 O(log n)으로 원하는 값을 찾는 알고리즘.
문제 풀다가 자주 쓰는 형태들을 모아둠. 필요할 때 복사해서 쓰거나
로컬 테스트에서 import 해서 쓰면 됨.
"""

from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    정렬된 배열에서 target의 인덱스를 찾는다. 없으면 -1.

    >>> binary_search([1, 3, 5, 7, 9], 7)
    3
    >>> binary_search([1, 3, 5, 7, 9], 4)
    -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def lower_bound(arr: List[int], target: int) -> int:
    """
    target 이상인 값이 처음 나오는 인덱스 (target을 넣을 수 있는 가장 왼쪽 위치).
    파이썬 표준 bisect.bisect_left 와 동일.

    >>> lower_bound([1, 2, 2, 2, 3], 2)
    1
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr: List[int], target: int) -> int:
    """
    target 초과인 값이 처음 나오는 인덱스 (target을 넣을 수 있는 가장 오른쪽 위치).
    파이썬 표준 bisect.bisect_right 와 동일.

    >>> upper_bound([1, 2, 2, 2, 3], 2)
    4
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


# 로컬 테스트
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9]
    print(binary_search(data, 7))   # 3
    print(binary_search(data, 4))   # -1
    print(lower_bound([1, 2, 2, 2, 3], 2))  # 1
    print(upper_bound([1, 2, 2, 2, 3], 2))  # 4
