# 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하라.
# 만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력
# 리스트에 있는 점수 N개
# 랭킹 리스트에 올라 갈 수 있는 점수의 개수 P


n, new, p = map(int, input().split())
ans = 2000000000
if n:
    grade = list(map(int, input().split()))

    # 빈자리 존재 안하고 마지막 수 보다 작거나 같음
    if n == p and grade[-1] >= new:
        print(-1)
    else:
        # 빈자리 존재 하거나 마지막 수 보다 큼
        ans = n+1
        for i in range(n):
            # 처음으로 작거나 같은 자리 찾기
            if grade[i] <= new:
                ans = i + 1
                break
        print(ans)
else:
    print(1)
