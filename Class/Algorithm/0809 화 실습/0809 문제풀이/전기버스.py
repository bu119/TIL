def f(arr, k, n, m):
    arr = [0] + arr + [n]   # 출발점과 도착점 추가
    last = 0    # 마지막으로 충전한 충전소 번호
    cnt = 0     # 충전 횟수

    for i in range(1, m + 2):
        # 충전기 사이가 K보다 크면 충전할 수 없음
        if arr[i] - arr[i-1] > k:
            return 0
        # 충전할 수 없는 경우 앞쪽에서 충전해야 함
        if arr[i] > last + k:
            last = arr[i-1]
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    # K = 최대이동횟수, N = 종점, M = 충전기 설치 위치
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {f(arr, K, N, M)}')