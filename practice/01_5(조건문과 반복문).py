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