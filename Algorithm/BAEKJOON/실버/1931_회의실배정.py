n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort(key=lambda x: (x[1], x[0]))   # 끝나는 시간으로 정렬, 같으면 시작 시간으로 정렬
end = time[0][1]                        # 첫 번째 인덱스의 끝나는 시간
cnt = 1                                 # 두 번째 인덱스부터 비교하므로 1

for i in range(1, n):
    if end <= time[i][0]:               # 끝나는 시간과 시작 시간을 비교
        cnt += 1
        end = time[i][1]                # 통과한 시간의 끝나는 시간으로 바꿔줌

print(cnt)