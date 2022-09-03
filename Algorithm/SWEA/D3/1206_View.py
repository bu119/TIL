import sys
sys.stdin = open("input.txt", "r")

for t in range(10):
    n = int(input())
    arr = list(map(int, input().split()))

    view = 0   # 확보된 조망권 수

    for i in range(2,n-2):
        height = 0
        for j in [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]:   # 양옆에 건물 2개씩 총 4 건물 비교
            if height < j:    # 주변 건물 중에서 가장 높은 층 찾기
                height = j

        v = arr[i] - height   # 현재 건물 - 주변에 가장 높은 건물 (조망권 확보된 층 수)
        if v > 0:             # 조망권이 확보되면 view에 더하기
            view += v
    print(f'#{t+1} {view}')


            


