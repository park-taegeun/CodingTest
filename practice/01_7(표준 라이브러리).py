# 내장 함수
## sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7") # 사람이 계산하는 것처럼의 결과를 반환
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key 
array = [('홍길동', 35), ('이순신', 50), ('박태근', 25)]
result1 = sorted(array, key=lambda x: x[1]) # 각 튜플의 1번째 원소를 기준으로 오름차순 정렬
result2 = sorted(array, key=lambda x: x[1], reverse=True) # 각 튜플의 1번째 원소를 기준으로 내림차순 정렬
print(result1)
print(result2)

# 순열과 조합
## 순열
from itertools import permutations # 순열 -> permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3)) # data에서 3개를 골라 순서를 고려해서 나열 -> 순열
print(result)

## 조합
from itertools import combinations # 조합 -> combinations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data, 2)) # data에서 순서를 고려하지 않고 2개를 골라 나열 -> 조합
print(result)

## 중복 순열
from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2)) ## 중복을 허용하여 2개를 뽑는 모든 순열 구하기
print(result)

## 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2)) ## 중복을 허용하여 2개를 뽑는 모든 조합 구하기
print(result)

# Counter
from collections import Counter

color_list = ['red', 'blue', 'red', 'green', 'blue', 'blue']
counter = Counter(color_list)

print(counter['blue'])
print(counter['red'])
print(counter['green'])
print(dict(counter))

# math
import math

## 최소 공배수(LCM)을 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산사 -> 두 수가 주어졌을 때 공통 약수 중에 가장 큰 값
print(math.lcm(21, 14)) # 최소 공배수(LCM) 계산 -> 두 수의 공통된 배수 중에서 가장 작은 수