# == pro ==
# 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했습니다. 오늘은 떡볶이 떡을 만드는 날입니다.
# 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않습니다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다.
# 절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단합니다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고 낮은 떡은 잘리지 않습니다.
# 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm으로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것입니다.
# 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm입니다. 손님은 6cm만큼의 길이를 가져갑니다.
# 손님이 왔을 때 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.

# 입력 조건
# - 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어집니다.
# - 둘째 줄에는 떡의 개별 높이가 주어집니다. 떡 높이의 총합은 항상 M이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있습니다.

# 입력 예시
# 4 6
# 19 15 10 17 -> 답은 15

# 출력 조건
# - 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력합니다.

# == sol(내가 푼 것) ==
# 떡의 개별 높이를 내림차순 정렬을 시키고
# 절단기 높이 설정을 0번 인덱스의 숫자부터 -1을 해나가면서 손님이 가져갈 수 있는 양을 합계로 구하다가
# 손님이 원하는 양을 가져갈 수 있게끔 가장 먼저 나온 절단기 높이 설정값이 출력값이 되게 하면 될듯?

n, m = map(int, input().split()) # 떡의 개수 n, 요청한 떡의 길이 m 입력
n_height = list(map(int, input().split())) # 떡의 개별 높이 배열 입력

n_sorted_height = sorted(n_height, reverse=True) # 내림차순 정렬

# 로직
h = n_sorted_height[0] # 절단기 높이 초깃값

while (h>=0):
    total = 0

    for i in range(0, n): # 떡 개별 높이 배열 순회
        if n_sorted_height[i] > h: total += n_sorted_height[i] - h
        else: continue

    if total >= m:
        result = h
        break

    h -= 1

print(f"답은 {result}")        

# == sol(이진 탐색) ==
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid: total += x - mid

    # 떡의 양이 부족한 경우 더 많이 자르기
    if total < m: end = mid - 1
    else: # 떡의 양이 충분한 경우 덜 자르기
        result = mid
        start = mid + 1

print(result)