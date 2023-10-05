# 총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 있다.
# 톱니는 N극 또는 S극 중 하나를 나타내고 있다.
# 톱니바퀴를 총 K번 회전시키려고 한다.
# 회전은 시계 방향과 반시계 방향이 있고, 아래 그림과 같이 회전한다.

#  서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다.
# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면,
# B는 A가 회전한 방향과 반대방향으로 회전하게 된다.
from collections import deque
import sys
input = sys.stdin.readline

# 옆에 톱니바퀴가 같은 극인지 다른 극인지 확인하기
# 왼쪽 톱니 바퀴들 확인
def check_left(left_wheel, left_dir):
    global rotate_dir

    left_wheel -= 1

    while 0 <= left_wheel:
        # 같은 극이면 탐색 종료
        if cogwheel[left_wheel][2] == cogwheel[left_wheel+1][6]:
            break

        # 다른 극이면 방향 바꿔주기
        left_dir = -left_dir
        # 바뀐 방향 저장
        rotate_dir[left_wheel] = left_dir
        # 다음 오른쪽 휠 탐색
        left_wheel -= 1


# 오른쪽 톱니 바퀴들 확인
def check_right(right_wheel, right_dir):
    global rotate_dir

    right_wheel += 1

    while right_wheel < 4:
        # 같은 극이면 탐색 종료
        if cogwheel[right_wheel-1][2] == cogwheel[right_wheel][6]:
            break

        # 다른 극이면 방향 바꿔주기
        right_dir = -right_dir
        # 바뀐 방향 저장
        rotate_dir[right_wheel] = right_dir
        # 다음 오른쪽 휠 탐색
        right_wheel += 1


# 회전 가능한 톱니바퀴 회전
def rotate_wheel():
    global cogwheel, rotate_dir

    for i in range(4):

        if rotate_dir[i] == 1:
            # 시계 방향으로 회전
            cogwheel[i].appendleft(cogwheel[i].pop())
        elif rotate_dir[i] == -1:
            # 반시계 방향으로 회전
            cogwheel[i].append(cogwheel[i].popleft())


# 톱니바퀴 정보 저장
cogwheel =[deque(map(int, input().rstrip())) for _ in range(4)]

k = int(input())
for _ in range(k):
    wheel, direction = map(int, input().split())
    wheel -= 1
    # 방향이 1이면 시계 방향, -1이면 반시계 방향
    # 회전 가능 정보 저장
    rotate_dir = [0] * 4
    rotate_dir[wheel] = direction
    # 2번위치, 6번위치 확인
    # 톱니 바퀴 회전 가능 정보 저장
    check_right(wheel, direction)
    check_left(wheel, direction)

    # 전체 톱니바퀴 회전
    rotate_wheel()

# 톱니바퀴 점수 합
score = 0
for k in range(4):
    # s극 이면 해당 점수를 더한다.
    # N극은 0, S극은 1
    if cogwheel[k][0]:
        score += 2**k
print(score)