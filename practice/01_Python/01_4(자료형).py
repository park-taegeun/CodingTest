# 실수형
a = .7
print(a)

a = 5.
print(a)

a = 1e9
print(a)

# 지수 표현
a = 75.25e1
print(a) # e1은 10을 곱한다는 뜻과 같음 -> 75.25 x 10 = 752.5

a = 3954e-3
print(a) # e-3은 1000을 나눈다는 뜻과 같음

# 실수 더 알아보기
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

# 연산자
a = 7
b = 3

print(a/b)
print(a%b)
print(a//b)
print(a ** b)

# 리스트
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[3])

n = 10
a = [0] * n # 내용이 [0]인 리스트 1개를 n번만큼 곱해서 리스트 초기화
print(a)

## 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[7])
print(a[-2]) # 뒤에서 접근 가능

## 슬라이싱
print(a[0:3]) # 첫번째 ~ 세번째

## 리스트 컴프리헨션
array = [i for i in range(10)] # range(10): 0~9
print(array)

a = [i for i in range(50)]
print(a)

## 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

## 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i*i for i in range(10)] # i*i 이 부분이 '원소 설정' 부분
print(array)

## N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)] # 길이가 m인 리스트 생성을 n번 반복
# n번 반복할 때마다 길이가 m인 리스트 생성
# _: 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용

print(array)
array[1][1] = 5
print(array)

## _ 사용
summary = 0
for i in range(1, 10):
    summary += i
print(summary)

for _ in range(5):
    print("Hello World") # 변수 필요 없는 단순 작업 반복

## 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형

result = [i for i in a if i not in remove_set] # remove_set에 포함되어 있지 않은 i로 리스트 생성
print(result)

# 문자열 자료형
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

## 문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a*3)

# 튜플 자료형
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a[3])
print(a[1:4])

# 사전 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

key_list = data.keys() # 키 데이터만 모아 놓은 리스트
value_list = data.values() # 값 데이터만 모아 놓은 리스트
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

a = dict()
a['홍길동'] = 97
a['이순신'] = 98
print(a)

b = {
    '홍길동': 97,
    '이순신': 98,
}
print(b)

key_list = list(b.keys())
print(key_list)
print(b['이순신'])

# 집합 자료형
data = set([1, 1, 2, 3, 4, 4, 5]) # 초기화 방법 1
print(data)

data = {1, 1, 2, 3, 4, 4, 5} # 초기화 방법 2
print(data)

## 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합

data = set([1, 2, 3])
print(data)

data.add(4)
print(data)

data.update([5, 6])
print(data)

data.remove(3)
print(data)

# 입력
# n = int(input())
# print(n)
# data = list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)

# a, b, c = map(int, input().split())
# print(a, b, c)

## 빠르게 입력 받기
# import sys

# data = sys.stdin.readline().rstrip()
# print(data)

#  출력
a = 1
b = 2
print(a, b)
print(7, end=" ") # 개행x
print(8, end=" ") # 개행x

answer = 7
print("정답은 " + str(answer) + "입니다.")

## f스트링
answer = 7
print(f"정답은 {answer}입니다.") 
