import sys

n, m = map(int, sys.stdin.readline().split())
walk = list(map(int, sys.stdin.readline().split()))
plus_walk = []
minus_walk = []
max_walk = 0  # 제일 멀리 있는 책의 위치

for i in walk:
    # 양수와 음수를 나눈다.
    if i > 0:
        plus_walk.append(i)
    else:
        minus_walk.append(i)

    # 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요 없기때문에
    # 마지막 책은 제일 멀리 있는 책으로 정한다.
    if abs(i) > abs(max_walk):
        max_walk = i

# 양수는 내림차순으로 음수는 오름차순으로 정렬한다.
plus_walk.sort(reverse=True)
minus_walk.sort()

# 최소 걸음 수
walking = 0

# m권을 들고 양수 방향에 책을 모두 제자리에 놔둔다.
for j in range(0, len(plus_walk), m):
    # 제일 멀리 있는 책은 무시한다.
    if plus_walk[j] != max_walk:
        walking += plus_walk[j]

# m권을 들고 음수 방향에 책을 모두 제자리에 놔둔다.
for k in range(0, len(minus_walk), m):
    # 제일 멀리 있는 책은 무시한다.
    if minus_walk[k] != max_walk:
        # 최소 걸음 수를 계산하기 위해 절대값으로 바꿔 더한다.
        walking += abs(minus_walk[k])

# 최소 걸음 수는 책의 제자리 위치와 현재 책의 위치를 왕복하여 계산한다.
walking *= 2
# 제일 멀리 있는 책을 놔둔다.
walking += abs(max_walk)

print(walking)
