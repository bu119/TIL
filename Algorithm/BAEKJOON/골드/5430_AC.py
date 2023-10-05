#AC는 정수 배열에 연산을 하기 위해 만든 언어
# 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수
# D는 첫 번째 수를 버리는 함수이다.
# 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 수행할 함수
    p = input().rstrip().replace('RR', '')
    # 배열에 들어있는 수의 개수
    n = int(input())
    arrX = input().rstrip().strip('[]')
    if arrX:
        arrX = deque(map(int, arrX.split(',')))

    # 뒤집었는 지 확인
    checkRev = False
    # 에러 인지
    checkE = False
    # 연산 시행
    for i in p:
        if i == 'D':
            # 에러 체크
            if not arrX:
                checkE = True
                break

            # 처음 방향
            if not checkRev:
                arrX.popleft()
            else:
                # 뒤집은 방향일 때
                arrX.pop()
        else:
            # 뒤집기
            checkRev = not checkRev

    if checkE:
        print('error')
    else:
        if checkRev:
            arrX = reversed(arrX)
        print('['+','.join(map(str, arrX))+']')
