from collections import deque
import sys
input = sys.stdin.readline

def bfs(A, dslr):
    deq = deque()
    deq.append((A, dslr))

    visited[A] = 1

    while deq:
        num, dslr = deq.popleft()

        for i in ['D', 'S', 'L', 'R']:
            if i == 'D':
                n = (num * 2) % 10000

            elif i == 'S':
                n = num - 1
                if n == -1:
                    n = 9999

            elif i == 'L':
                n = (10 * num) % 10000 + num // 1000

            else:
                n = num // 10 + (num % 10) * 1000

            if n == B:
                return dslr + i
            elif not visited[n]:
                visited[n] = 1
                deq.append((n, dslr + i))


T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    print(bfs(A, ''))