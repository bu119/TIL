# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
import sys
sys.stdin = open("pass_input.txt", "r")

# 뒤집었을때 같은 것 제외
# 처음 같은 인덱스 찾기
for tc in range(10):
    n, num = input().split()
    cnt = 1          # cnt 초기값 1
    while cnt != 0:  # cnt가 1이 아니면 계속 실행
        # arr = ''  위치 조정
        cnt = 0      # 반복문이 실행되면 cnt 값을 0으로 바꿔줌
        for i in range(len(num)-1):  # 아래서 연속된 수를 +1로 비교하므로 범위를 하나 줄여줌
            if num[i] == num[i+1]:   # 연속된 두개의 값이 같으면
                arr = ''
                arr += num[:i]    # 인덱스 전후의 값을 arr에 넣어줌
                arr += num[i+2:]
                cnt = 1  # 같은 값이 존재하면 cnt값을 1로 바꿈
                break
        num = arr # 같은 값을 지운 값으로 반복 시행 하므로 num값을 arr로 바꿔 반복 시행
        # 같은 값이 존재하지 않으면 cnt는 0이 되므로 반복문 종류

    print(f'#{tc+1} {num}')
