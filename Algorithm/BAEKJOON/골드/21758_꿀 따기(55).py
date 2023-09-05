import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다.
# 벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
ans = 0

for move in range(1,n-1):
    # 벌A 벌B(이동) 꿀통
    beeA = sum(arr[1:]) - arr[move]
    beeB = sum(arr[move+1:])
    ans = max(ans, beeA+beeB)

    # 벌A 꿀통(이동) 벌B
    beeA = sum(arr[1:move+1])
    beeB = sum(arr[move:n-1])
    ans = max(ans, beeA + beeB)

    # 꿀통 벌A(이동) 벌B
    beeA = sum(arr[:move])
    beeB = sum(arr[:n-1]) - arr[move]
    ans = max(ans, beeA + beeB)

print(ans)