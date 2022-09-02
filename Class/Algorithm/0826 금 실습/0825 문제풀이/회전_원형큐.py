import sys; sys.stdin = open("회전_input.txt","r")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    queue = [0] + list(map(int, input().split()))
    front, rear = 0, N
    qsize = N + 1
    for _ in range(M):
        #deQueue
        front = (front+1) % qsize
        t = queue[front]

        #enQueue
        rear = (rear+1) % qsize
        queue[rear] = t

    print(f'#{tx} {queue[(front + 1) % qsize]}')