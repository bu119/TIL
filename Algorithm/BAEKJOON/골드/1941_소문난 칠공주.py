# ‘이다솜파’의 학생들은 과감히 현재의 체제를 포기, ‘소문난 칠공주’를 결성
# 7명의 여학생들로 구성
# 7명의 자리는 서로 가로나 세로로 반드시 인접
# 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
# ‘이다솜파’가 반드시 우위를 점해야 한다.
# 따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.
# ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수

# 'S'(이다‘솜’파의 학생을 나타냄) 또는 'Y'(임도‘연’파의 학생을 나타냄)을 값
#  5*5 행렬
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


def bfs(x, y):
    total = 1
    deq = deque()
    deq.append((x, y))
    # 방문 위치 제거
    visited[i][j] = 0

    while deq:
        x, y = deq.popleft()

        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj] == 1:
                # 방문한 위치 제거
                visited[ni][nj] = 0
                deq.append((ni,nj))
                total += 1
    if total == 7:
        return 1
    return 0


students = [input() for _ in range(5)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
cnt = 0
for members in combinations(range(25), 7):
    # 7공주 체크
    visited = [[0] * 5 for _ in range(5)]
    yCnt = 0
    for num in members:
        i = num // 5
        j = num % 5
        visited[i][j] = 1
        if students[i][j] == 'Y':
            yCnt += 1

        if yCnt >= 4:
            break

    if yCnt < 4 and bfs(i, j):
        cnt += 1

print(cnt)
