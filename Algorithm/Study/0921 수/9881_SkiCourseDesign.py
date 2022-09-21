# 가장 높은 언덕과 가장 낮은 언덕의 차이가 17초과일 때 세금냄
# 언덕을 k만큼 쌓거나 깍는데 k*k만큼 비용 발생
# 가장 적은 cost
# 쌓고 올리기 동시에 진행

n = int(input())
hills = [int(input()) for _ in range(n)]
hills.sort()
# print(hills)
cost = [0] * (hills[-1])        # 인덱스가 최소 높이

for low in range(hills[-1]):    # 각 인덱스를 최소 높이로 탐색 (조건 실패, 전부 탐색)
    cnt = 0                     # 비용
    for j in range(n):
        num = hills[j]          # 비교할 숫자
        high = low + 17         # 최대 높이
        if num < low:
            cnt += (low - num) ** 2
        elif num > high:
            cnt += (num - high) ** 2
    cost[low] = cnt
# print(cost)
print(min(cost))
