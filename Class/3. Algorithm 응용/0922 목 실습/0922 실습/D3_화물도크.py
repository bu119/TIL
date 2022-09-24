import sys
sys.stdin = open('testcase/input_화물도크.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0])) 	# 종료 시점을 기준으로 정렬
    cnt = 1
    end = arr[0][1]             			# 첫번째 종료지점을 end로 지정
    for i in range(1, n):
        if end <= arr[i][0]:				# 시작시점이 종료시점보다 크거나 같으면
            cnt += 1						# 카운트
            end = arr[i][1]

    print(f'#{tc+1} {cnt}')