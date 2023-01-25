# 공이 구분되지 않으므로 방향이 바뀌면 다른 공이 그 자리를 대체한다.
# 따라서, 충돌 후에도 같은 방향을 유지한다고 생각하면된다.
# 임의의 두 공(nC2) 사이의 거리가 2t 이하이면서,
# 마주보며 운동할 때만(1/4의 확률) 부딪힌다.
# 공 하나 당 오른쪽, 왼쪽 가능 (전체 4 중에 -> <- 방향 일때만 부딪힌다.) = 1/4

import sys
input = sys.stdin.readline

n = int(input()) # 공의 개수
posi = list(map(int,input().split())) # 각 공의 위치
t = int(input()) # 시간

posi.sort()
cnt = 0

for i in range(n-1):
    for j in range(i+1, n):
        if (posi[j]-posi[i]) <= 2*t:
            cnt += 1

print(cnt/4)