n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if arr[i] > arr[i-1]:               # 내림차 순이 아닌 자리가 나오면 (바로 앞 자리 수가 작으면)
        for j in range(n-1, 0, -1):
            if arr[i-1] < arr[j]:       # 뒤에 자리 수들 중 큰 수와 자리 바꿈
                arr[i - 1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:])         # 바뀐 자리 뒤는 오름차 순으로 정렬
                print(' '.join(map(str, arr)))
                exit(0)

print(-1)   # 배열이 내림차 순이면 앞에서 종료 안되고 -1 출력