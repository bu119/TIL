n = int(input())
p = list(map(int,input().split()))

time = [0] * n
p.sort()                            # 시간이 빠른 순으로 정렬
time[0] = p[0]
for i in range(1, n):
    time[i] = p[i] + time[i-1]  # 누적합 구하기

print(sum(time))