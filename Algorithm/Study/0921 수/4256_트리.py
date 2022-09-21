def find_post(preor, inor):
    if len(inor):
        node = inor.index(preor.pop(0))     # 전위 순회 결과로 부모 노드를 찾기
        find_post(preor, inor[:node])       # 중위 순회 결과로 오른쪽, 왼쪽 나누기
        find_post(preor, inor[node + 1:])
        print(inor[node], end=' ')          # 후위 순회
    else:
        return

t = int(input())
for tc in range(t):
    n = int(input())
    preor = list(map(int, input().split()))
    inor = list(map(int, input().split()))
    find_post(preor, inor)
    print()