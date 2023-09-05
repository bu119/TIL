# 상사가 직속 부하를 칭찬하면 그 부하가 부하의 직속 부하를 연쇄적으로 칭찬하는 내리 칭찬이 있다.
# 상사가 한 직속 부하를 칭찬하면 그 부하의 모든 부하들이 칭찬을 받는다.
# 모든 칭찬에는 칭찬의 정도를 의미하는 수치가 있는데, 이 수치 또한 부하들에게 똑같이 칭찬 받는다.
# 각자 얼마의 칭찬을 받았는지 출력하시오
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, w):
    global compliment

    for k in tree[v]:
        compliment[k] += w
        dfs(k, compliment[k])


n, m = map(int, input().split())
superior = list(map(int, input().split()))
# 부하직원 저장
tree = [[] for _ in range(n+1)]
# 칭찬 수치를 저장
compliment = [0]*(n+1)

# 부하직원을 기준으로 저장하는 배열
for p in range(n):
    # 인덱스+1이 부하직원
    # super은 상사
    super = superior[p]
    if super > 0:
        tree[super].append(p+1)

# 칭찬받은 각 직원의 칭찬 수치 저장
for _ in range(m):
    i, w = map(int, input().split())
    compliment[i] += w

# 한번에 칭찬 수치 처리하기
dfs(1, compliment[1])
print(*compliment[1:])