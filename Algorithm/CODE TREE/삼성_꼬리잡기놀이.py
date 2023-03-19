# 공이 던져지는 경우에 해당 선에 사람이 있으면 최초에 만나게 되는 사람만이 공을 얻게 되어 점수를 얻게 됩니다.
# 점수는 해당 사람이 머리사람을 시작으로 팀 내에서 k번째 사람이라면 k의 제곱만큼 점수를 얻게 됩니다.
# 공을 획득한 팀의 경우에는 반대 방향으로 움직임.
from collections import deque

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]


# 팀별 길 위치 찾기
def wayDfs(i, j):
    global tmp, idx, startEnd, teamNum, people

    for z in range(4):
        ni = i + di[z]
        nj = j + dj[z]
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] and not visited[ni][nj]:
            if board[i][j] == 3 and board[ni][nj] == 4:
                continue
            visited[ni][nj] = teamNum
            idx += 1
            tmp.append((ni, nj))
            if board[ni][nj] == 1:
                startEnd.append([0, idx])
            if board[ni][nj] == 2 or board[ni][nj] == 1:
                people.append((ni,nj))
            wayDfs(ni, nj)

        # 팀별 사람 저장

# 꼬리, 머리 사람 움직이기
def move(num, d):
    # num : 몇번째 팀인지
    if d:
        team[num].popleft()
        # d == 1이면 시계 방향
        e, s = startEnd[num]
        x, y = way[num][s]
        board[x][y] = 2
        x, y = way[num][e]
        board[x][y] = 4

        startEnd[num][0] = (startEnd[num][0] + 1) % len(way[num])
        startEnd[num][1] = (startEnd[num][1] + 1) % len(way[num])

        e, s = startEnd[num]
        x, y = way[num][s]
        board[x][y] = 1
        team[num].append((x, y))
        x, y = way[num][e]
        board[x][y] = 3

    else:

        team[num].pop()
        # d == 0이면 반시계 방향
        s, e = startEnd[num]
        x, y = way[num][s]
        board[x][y] = 2
        x, y = way[num][e]
        board[x][y] = 4

        startEnd[num][0] = (startEnd[num][0] - 1) % len(way[num])
        startEnd[num][1] = (startEnd[num][1] - 1) % len(way[num])

        s, e = startEnd[num]
        x, y = way[num][s]
        board[x][y] = 1
        team[num].appendleft((x,y))
        x, y = way[num][e]
        board[x][y] = 3


# 공의 움직임 배열
def throwBall(roundNum):
    roundNum %= (4 * n)
    ballPos = []

    if 0 <= roundNum < n:
        for z in range(n):
            ballPos.append([roundNum, z])

    elif n <= roundNum < 2 * n:
        roundNum %= n
        for z in range(n-1, -1, -1):
            ballPos.append([z, roundNum])

    elif 2 * n <= roundNum < 3 * n:
        roundNum %= n
        for z in range(n-1, -1, -1):
            ballPos.append([n-1-roundNum, z])

    elif 3 * n <= roundNum < 4 * n:
        for z in range(n):
            roundNum %= n
            ballPos.append([z, n-1-roundNum])
    return ballPos


# 점수 계산
def getScore():
    global ball, dire, team, score
    cnt = 0
    for r, c in ball:
        if board[r][c] != 0 and board[r][c] != 4:
            for px, py in team[visited[r][c]-1]:
                cnt += 1
                if px == r and py == c:
                    break

            # 시계방향
            if dire[visited[r][c]-1]:
                cnt = len(team[visited[r][c]-1]) - cnt + 1
                dire[visited[r][c]-1] = 0
            else:
                dire[visited[r][c]-1] = 1
            score += (cnt * cnt)
            return

# 격자의 크기 n, 팀의 개수 m, 라운드 수 k
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
teamNum = 0

# 팀별 점수
score = 0

# 팀별 길위치 저장
way = []
# 팀별 사람 저장
team = []

# 시작과 끝 idx 담기 : [꼬리,머리]
startEnd = []

# 팀 위치 담기
for i in range(n):
    for j in range(n):
        # 꼬리 위치 찾기
        if board[i][j] == 3 and not visited[i][j]:
            teamNum += 1
            idx = 0
            visited[i][j] = teamNum
            tmp = [(i, j)]
            people = deque()
            people.append((i, j))
            wayDfs(i, j)
            way.append(tmp)
            team.append(people)

        # 시간 줄이기 (없어도 무관)
        if teamNum == m:
            break
    # 시간 줄이기 (없어도 무관)
    if teamNum == m:
        break

# print(team)
# 방향 : 1이면 시계 방향/ 0이면 반시계 방향
dire = [1] * m
for roundNum in range(k):
    # 공 움직임
    ball = throwBall(roundNum)
    # print(ball)
    # 사람들 움직임
    for num in range(m):
        move(num, dire[num])

    getScore()
    # print(board)
    # print(way)
    # print(team)

print(score)