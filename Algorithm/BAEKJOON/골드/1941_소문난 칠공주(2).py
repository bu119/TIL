# 7명의 자리는 서로 가로나 세로로 반드시 인접
# 따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.
# ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수
# 'S'(이다‘솜’파의 학생을 나타냄) 또는 'Y'(임도‘연’파의 학생을 나타냄)을 값
#  5*5 행렬
import sys
input = sys.stdin.readline

def dfs(yCnt):
    global candidate

    # 임도‘연’파 학생수 체크
    if yCnt >= 4:
        return

    # 조건에 만족하는 칠공주 모이면
    if len(candidate) == 7:
        members.add(tuple(sorted(candidate)))
        return

    # 이미 확인한 후보 경우이면 리턴
    if tuple(sorted(candidate)) in visited:
        return

    # 각 위치에서 4방향 탐색으로 인접한 모든 경우 찾기
    for x, y in candidate:
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5 and (ni, nj) not in candidate:
                # 임도‘연’파 변화 저장
                newY = yCnt
                if students[ni][nj] == 'Y':
                    newY += 1
                candidate.append((ni,nj))
                dfs(newY)
                candidate.pop()

    # 확인이 끝난 후보들 방문 체크
    # 탐색이 끝나서 return되는 후보들
    visited.add(tuple(sorted(candidate)))


students = [input() for _ in range(5)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
# 7공주 가능한 경우 저장
members = set()
# 멤버 후보 방문 체크
visited = set()

for i in range(5):
    for j in range(5):
        # 이다‘솜’파 이면 탐색
        if students[i][j] == 'S':
            # 멤버 선택
            candidate = [(i, j)]
            dfs(0)

# ‘소문난 칠공주’ 모든 경우의 수
print(len(members))