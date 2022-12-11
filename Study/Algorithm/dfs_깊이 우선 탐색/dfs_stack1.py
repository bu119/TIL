'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 시작점 v

def dfs(v, N):
    top = -1

    visited[v] = 1                  # 시작점 방문 표시
    print(v, end=' ')               # 방문해서 할 일: 방문한 곳 출력

    while True:
        for w in adj_list[v]:       # v의 인접 정점 중 
            if visited[w] == 0:     # 방문 안한 정점 w가 있으면
                top += 1            # push(v)
                stack[top] = v
                v = w               # v <- w (w에 방문)

                visited[w] = 1      # visited[w] <- true
                print(v, end=' ')   # 방문해서 할 일: 방문한 곳 출력
                break
        else:                       # w가 없으면 (for문을 나온 상황)
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top = -1
            else:                   # 스택이 비어있으면
                break               # while 빠져나옴



V, E = map(int, input().split())    # 정점, 간선
N = V + 1                           # 정점의 개수 만큼 행이 필요
adj_list = [[] for _ in range(N)]
temp = list(map(int, input().split()))

for i in range(E):                  # 인접리스트로 저장하기
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

visited = [0] * N                   # visited 생성 (초기화)
stack = [0] * N                     # stack 생성 (초기화)
dfs(1, N)
print()