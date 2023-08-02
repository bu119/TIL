import sys
input = sys.stdin.readline

n = int(input())
deque = []

for _ in range(n):
    case = input().rstrip()

    if case == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif case == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif case == 'size':
        print(len(deque))
    elif case == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif case == 'front':
        if deque:
            print(int(deque[0]))
        else:
            print(-1)
    elif case == 'back':
        if deque:
            print(int(deque[-1]))
        else:
            print(-1)
    else:
        push, x = case.split()
        x = int(x)
        if push == 'push_front':
            deque.insert(0, x)
        else:
            deque.append(x)