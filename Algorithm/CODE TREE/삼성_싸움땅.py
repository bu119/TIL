'''
1.
1-1. 첫 번째 플레이어부터 순차적으로 향하고 있는 방향대로 한 칸만큼 이동
1-2. 격자를 벗어나는 경우에는 반대 방향으로 방향을 바꾸어서 1만큼 이동

2. 이동한 방향에 총이 있는 경우,
2-1. 해당 플레이어는 총을 획득
2-2. 플레이어가 이미 총을 가지고 있는 경우에는 공격력이 더 쎈 총을 획득
2-3. 나머지 총은 해당 격자에 둠

3. 이동한 방향에 플레이어가 있는 경우
3-1. 두 플레이어가 싸움
3-2. 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 승
3-3. 만일 이 수치가 같은 경우, 플레이어의 초기 능력치가 높은 플레이어가 승
3-4 이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득

4. 진 플레이어
4-1. 본인이 가지고 있는 총을 해당 격자에 내려놓고,
4-2. 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동
4-3. 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는 오른쪽으로 90도씩 회전
4-4. 빈 칸이 보이는 순간 이동
4-5. 만약 해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총을 획득
4-6. 나머지 총들은 해당 격자에 내려 놓습니다.

5. . 이긴 플레이어
5-1. 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득
5-2. 나머지 총들은 해당 격자에 내려 놓습니다.
'''

def move(i):
    # i번 사람 이동
    px = player[i]['x']
    py = player[i]['y']
    people[px][py] = -1         # 사람 이동한 자리

    d1 = dir[player[i]['d']]
    nx = px + d1[0]
    ny = py + d1[1]
    if not (0 <= nx < n and 0 <= ny < n):           # 벽 만나면
        player[i]['d'] = (player[i]['d'] + 2) % 4
        d2 = dir[player[i]['d']]
        nx = px + d2[0]
        ny = py + d2[1]

    player[i]['x'] = nx
    player[i]['y'] = ny


def loser(i):
    # 방향 탐색
    while True:
        d1 = dir[player[i]['d']]
        nx = player[i]['x'] + d1[0]
        ny = player[i]['y'] + d1[1]
        if not (0 <= nx < n and 0 <= ny < n) or (people[nx][ny] > -1):
            player[i]['d'] = (player[i]['d'] + 1) % 4
        else:
            break
    player[i]['x'] = nx
    player[i]['y'] = ny
    people[nx][ny] = i      # 사람 표시
    # 총 줍기
    guns[nx][ny].append(player[i]['gun'])
    guns[nx][ny].sort()
    gun_choice = guns[nx][ny].pop()
    player[i]['gun'] = gun_choice


def winner(i):
    nx = player[i]['x']
    ny = player[i]['y']
    people[nx][ny] = i      # 사람 표시
    # 총 줍기
    guns[nx][ny].append(player[i]['gun'])
    guns[nx][ny].sort()
    gun_choice = guns[nx][ny].pop()
    player[i]['gun'] = gun_choice


def fight(i, j):
    global ans
    my_power = player[i]['s'] + player[i]['gun']
    your_power = player[j]['s'] + player[j]['gun']
    if (my_power, player[i]['s']) > (your_power, player[j]['s']):
        ans[i] += my_power - your_power
        loser(j)
        winner(i)

    else:
        ans[j] += your_power - my_power
        loser(i)
        winner(j)


n, m, k = map(int, input().split())
guns = [[] for _ in range(n)]
for z in range(n):
    for num in list(map(int, input().split())):
        guns[z].append([num])

people = [[-1]*n for _ in range(n)]
player = []
for p in range(m):
    x, y, d, s = map(int, input().split())
    info = {'x': x-1, 'y': y-1, 'd': d, 's': s, 'gun': 0}
    player.append(info)
    people[x - 1][y - 1] = p        # 사람 위치 표시

# 상우하좌 (0,1,2,3)
dir = [-1, 0], [0, 1], [1, 0], [0, -1]
ans = [0] * m

for _ in range(k):
    for i in range(m):
        move(i)
        # i번 사람이 이동한 위치
        mx = player[i]['x']
        my = player[i]['y']
        # 이동한 위치에 사람이 있으면 싸움
        if people[mx][my] > -1:
            fight(i, people[mx][my])
        else:
            # 총이 있으면 쎈 총으로 교체
            guns[mx][my].append(player[i]['gun'])
            guns[mx][my].sort()
            gun = guns[mx][my].pop()
            player[i]['gun'] = gun
            # 사람이 이동한 위치 표시
            people[mx][my] = i


print(' '.join(map(str, ans)))