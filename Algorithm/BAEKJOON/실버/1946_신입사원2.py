import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    grade = [0]*(n+1)
    for i in range(n):
        a, b = map(int,input().split())
        # 인덱스에 맞게 자동 정렬
        grade[a] = b
    # 높은 순위 저장
    top = grade[1]
    # 작은 수가 높은 순위
    for i in range(2, n+1):
        if grade[i] < top:
            # 순위가 높으면 top을 높은 순위로 바꾸기
            top = grade[i]
        else:
            # 순위가 낮으면 개수 감소
            n -= 1
    print(n)