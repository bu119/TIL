from collections import deque

def solution(maxSize, actions):

    visited = deque()
    back = deque()
    front = deque()
    visited_set = set()

    for i in actions:

        if i == 'F':
            if front:
                num = front.popleft()
                back.appendleft(visited[0])

                if num in visited_set:
                    visited.remove(num)
                visited.appendleft(num)
                visited_set.add(num)

        elif i == 'B':
            if back:
                num = back.popleft()
                front.appendleft(visited[0])

                if num in visited_set:
                    visited.remove(num)
                visited.appendleft(num)
                visited_set.add(num)

        else:

            if len(visited) != 0:
                back.appendleft(visited[0])

            front = deque()

            if i in visited_set:
                visited.remove(i)
            visited.appendleft(i)
            visited_set.add(i)


        if len(visited) > maxSize:
            num = visited.pop()
            visited_set.remove(num)

    answer = list(visited)
    return answer

maxSize = 3
actions= ["1", "2", "B", "F"]

print(solution(maxSize, actions))