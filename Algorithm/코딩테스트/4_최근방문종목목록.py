from collections import deque

def solution(maxSize, actions):
    ## 고객 동작
    # 1. 직접 방문 - 숫자
    # 2. 뒤로 가기 = B
    # 3. 앞으로 가기 = F

    visited = deque()
    back = deque()
    front = deque()

    for i in actions:

        if i == 'F':
            if front:
                num = front.popleft()
                back.appendleft(visited[0])

                if num in visited:
                    visited.remove(num)
                visited.appendleft(num)

        elif i == 'B':
            if back:
                num = back.popleft()
                front.appendleft(visited[0])

                if num in visited:
                    visited.remove(num)
                visited.appendleft(num)

        else:

            if len(visited) == 0:
                visited.append(i)
            else:
                back.appendleft(visited[0])
                front = deque()

                if i in visited:
                    visited.remove(i)
                visited.appendleft(i)


        if len(visited) > maxSize:
            visited.pop()

    answer = list(visited)

    return answer


maxSize = 3
actions= ["1", "2", "B", "F"]

print(solution(maxSize, actions))