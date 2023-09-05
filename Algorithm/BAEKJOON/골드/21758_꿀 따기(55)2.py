import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다.
# 벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
ans = 0
total = sum(arr)
for move in range(1,n-1):
    # 양 끝 고정
    # 벌A 벌B(이동) 꿀통
    beeA = total - arr[0] - arr[move]
    beeB = total - sum(arr[:move+1])
    ans = max(ans, beeA+beeB)

    # 벌A 꿀통(이동) 벌B
    beeA = total - sum(arr[move+1:]) - arr[0]
    beeB = total - sum(arr[:move]) - arr[n-1]
    ans = max(ans, beeA + beeB)

    # 꿀통 벌A(이동) 벌B
    beeA = total - sum(arr[move:])
    beeB = total - arr[move] - arr[n-1]
    ans = max(ans, beeA + beeB)

print(ans)