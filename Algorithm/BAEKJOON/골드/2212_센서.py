# 집중국은 센서의 수신 가능 영역을 조절
# 각 집중국의 수신 가능 영역의 길이의 합을 최소화
# 센서의 개수
n = int(input())
# 둘째 줄에 집중국의 개수
k = int(input())
# N개의 센서의 좌표
pos = list(map(int, input().split()))
# 센서 좌표 정렬
pos.sort()
# print(pos)
dif = []
# 인접한 센서들 간의 거리의 차
for i in range(n-1):
    dif.append(pos[i+1]-pos[i])

dif.sort()
# 구간으로 집중국 설치 (k-1 개 구간)
# 거리의 차가 큰 값을 k-1개 만큼 제거
# print(dif)
print(sum(dif[:n-k]))