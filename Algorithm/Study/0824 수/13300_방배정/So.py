N, K = map(int, input().split())
room = [[[],[]] for _ in range(7)] # 빈방 구현

for _ in range(N):
    s, y = map(int, input().split())
    room[y][s].append(1) # 학년 y, 성별 s
# 방에 학년과 성별에 맞춰 배치
# [[[], []], [[1], [1, 1]], [[1, 1], [1]], [[1], [1, 1, 1]], [[], [1]], [[1], [1, 1]], [[1], [1]]]

cnt = 0
for i in range(1, 7):
    for j in range(2):
        # 정원이 성립할 때
        if len(room[i][j]) <= K and len(room[i][j]) > 0:
            cnt += 1
        # 정원을 초과할 때
        elif len(room[i][j]) > K:
            cnt += len(room[i][j]) // K + 1

print(cnt)