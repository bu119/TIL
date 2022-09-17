def heappush(value):
    tree.append(value)

    node = len(tree) - 1        # 현재 부모
    idx = node                  # 현재 자식 위치

    while node > 1:
        node = node // 2        # 현재 노드를 부모 노드로 바꿔줌



        if tree[node] > value:          # 부모가 크면
            tree[idx] = tree[node]      # 자식 노드에 저장
            idx = node                  # 현재 자식 위치를 부모로
        else:                           # 부모가 작으면 종료
            break

    tree[idx] = value                   # 현재 자식위치에 값 업데이트


t = int(input())
for tc in range():
    n = int(input())
    arr = list(map(int, input()))
    tree = []

