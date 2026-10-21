# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 0 직전까지 1씩 감소하면 반복하는 문법
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] # 스와프
        else: break

print(array)

# 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: return

    pivot = start
    left = start + 1 # 왼쪽에서 찾는 거는 Pivot 보다 큰 수
    right = end # 오른쪽에서 찾는 거는 Pivot 보다 작은 수

    while (left <= right): # 엇갈렸을때 탈출
        while (left <= end and array[left] <= array[pivot]):
            left += 1 # 피벗보다 크지 않으면 계속 전진 → 큰 값 만나면 멈춤
        while (right > start and array[right] >= array[pivot]):
            right -= 1 # 피벗보다 작지 않으면 계속 후진 → 작은 값 만나면 멈춤

        if (left > right): # 엇갈림 = 분할 끝 -> right와 pivot 상호 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 안 엇갈림 -> left와 right 상호 교체
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 퀵 정렬 (파이썬 장점)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1: return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1,4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')