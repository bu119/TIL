# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
import sys
sys.stdin = open("pass_input.txt", "r")

# 뒤집었을때 같은 것 제외
# 처음 같은 인덱스 찾기
for tc in range(10):
    n, num = input().split()
    cnt = 1
    while True:
        # arr = ''  위치 조정
        cnt = 0
        for i in range(len(num)-1):  # 아래서 연속된 수를 +1로 비교하므로 범위를 하나 줄여줌
            if num[i] == num[i+1]:
                arr = ''
                arr += num[:i]
                arr += num[i+2:]
                cnt = 1
                break
        if cnt == 0:
            break

        num = arr

    print(f'#{tc+1} {num}')