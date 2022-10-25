from collections import deque
import sys
input = sys.stdin.readline

def bfs(A, dslr):
    deq = deque()
    deq.append((A, dslr))

    visited[int(A)] = 1

    while deq:
        num, dslr = deq.popleft()

        nlist = ['0']*(4 - len(num)) + list(num) # list
        number = int(num)

        for i in ['D', 'S', 'L', 'R']:
            if i == 'D':
                n = number * 2
                if n > 9999:
                    n %= 10000

            elif i == 'S':
                n = number - 1
                if n == -1:
                    n = 9999

            elif i == 'L':
                n = nlist[1] + nlist[2] + nlist[3] + nlist[0]  # str

            else:
                n = nlist[3] + nlist[0] + nlist[1] + nlist[2]  # str

            n = int(n)
            if n == Bnum:
                return dslr + i
            elif not visited[n]:
                visited[n] = 1
                deq.append((str(n), dslr + i))


T = int(input())
for tc in range(T):
    A, B = input().split() # str
    visited = [0] * 10000
    Bnum = int(B)
    print(bfs(A, ''))