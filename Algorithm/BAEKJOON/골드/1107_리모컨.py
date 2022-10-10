channel = int(input())
broken_n = int(input())
if broken_n:
    broken = input().split()
else:
    broken = []

cnt = abs(channel - 100)                # up_down으로 채널 검색하는 수

for number in range(1000001):           # 완전탐색으로 버튼 눌러서 찾기

    num = str(number)
    n = len(num)

    for i in range(n):
        if num[i] in broken:            # 버튼을 누를 수 없는 수가 나오면 다른 수 탐색
            break
        if i == n - 1:                  # 모든 수가 버튼을 누를 수 있으면
            cnt = min(cnt, abs(number - channel) + n)   # 버튼 누른 수와 +-로 찾은 수 중 최소값 찾기

print(cnt)