'''
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']
'''


#  완전이진트리에서의 순회
def pre_order(v):
    global last
    if v <= last:  # 마지막 정점번호 이내
        print(tree[v])
        pre_order(2 * v)  # 왼쪽 자식정점 방문
        pre_order(2 * v + 1)  # 오른쪽 자식정점 방문


tree = [0, 1, 2, 3, 4, 5, 6, 7] # 완전이진트리
last = 7
pre_order(2)