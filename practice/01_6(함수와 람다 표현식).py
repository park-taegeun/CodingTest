# 함수
# def add(a, b):
#     return a + b

# print(add(3, 7))

# def add(a, b):
#     print(f"함수의 결과: {a+b}")

# add(3, 7)

## global 키워드
a = 0

def func():
    global a
    a += 1

for i in range(10): # 0~9
    func()

print(a)

## 지역 변수 우선 참조
array = [1, 2, 3, 4, 5]

def func():
    array = [3, 4, 5]
    array.append(6)
    print(array)

func()
print(array)

array = [1, 2, 3, 4, 5]

def func():
    global array # 전역 변수 참조
    array.append(6)
    print(array)

func()

## 여러 개의 반환 값
def operator(a, b):
    add_var = a+b
    sub_var = a-b
    multiply_var = a*b
    divide_var = a/b
    
    return add_var, sub_var, multiply_var, divide_var # 여러 개의 값이 한 꺼번에 반환되는 것 = 패킹

a, b, c, d = operator(7, 3)
print(f"{a}, {b}, {c}, {d}")

# 람다 표현식
print((lambda a, b: a+b)(3, 6)) # lambda 매개변수: 함수 내용(입력값)

## 점수 순으로 오름차순 정렬
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1] # 한 튜플의 두 번째 원소

print(sorted(array, key=my_key)) # array의 정렬 기준이 key -> my_key
print(sorted(array, key=lambda x: x[1]))

## 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)

print(list(result))