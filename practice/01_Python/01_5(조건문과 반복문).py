# 조건문과 반복문
x = 15
if x >= 10:
    print(f"x>=10")

if x >= 0:
    print(f"x>=0")

if x >= 30:
    print(f"x>=30")

## 들여쓰기
score = 85

if score >= 70:
    print(f"score값이 70 이상입니다.")

    if score >= 90:
        print(f"우수한 성적입니다.")

else:
    print(f"성적이 70점 미만입니다.")
    print(f"조금 더 분발하세요.")

print(f"프로그램을 종료합니다.")

## 조건문의 기본 형태
score = 85

if score >= 90:
    print(f"A")

elif score >= 80 and score < 90:
    print(f"B")

elif score >= 70 and score < 80:
    print(f"C")

else: print(f"F")

## 논리 연산자
if True or False:
    print(f"yes")

if True and False:
    print(f"no")

## pass
score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else: print(f"성적이 80점 미만입니다.")

print(f"프로그램을 종료합니다.")

## 조건부 표현식
score = 85
result = "Success" if score >= 80 else "Fail" ## 조건부 표현식 -> 가운데에 조건이 들어가고 참이면 왼쪽 값으로 거짓이면 오른쪽 값으로
print(f"{result}")

# 반복문
## while 문
i = 1
result = 0

while i<=9:
    result += i
    i += 1

print(f"{result}")

### 1부터 9까지의 정수 중에서 홀수만 구하기
i = 1
result = 0

while i<=9:
    if i % 2 == 0:
        i += 1
    else:
        result += i
        i += 1

print(f"{result}")

## for 문
array = [1, 2, 3, 4, 5]

for x in array:
    print(x)

### range()
result = 0

for i in range(1, 10): # i는 1부터 9까지의 모든 수를 순회
    result += i

print(f"{result}")

### continue 키워드
result = 0

for i in range(1, 10): # i는 1~9
    if i % 2 == 0: continue
    result += i

print(f"{result}")

### break 키워드
i = 1

while True:
    print(f"현재 i값: {i}")
    if i == 5: break
    i+=1

scores = [90, 85, 77, 65, 97]

for i in range(5): # 0~4
    if scores[i] >= 80:
        print(f"{i+1} 번 학생은 합격입니다.")

scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i+1 in cheating_student_list: continue
    if scores[i] >= 80:
        print(f"{i+1}번 학생은 합격입니다.")


### 중첩된 반복문
### 구구단 예제
for i in range(2, 10): # 2~9
    for j in range(1, 10): # 1~9
        print(f"{i} X {j} = {i*j}")
    print()
