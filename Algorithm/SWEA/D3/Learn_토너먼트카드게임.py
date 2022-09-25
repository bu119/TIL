def win(r1, r2):
    if arr[r1] == arr[r2]:
        return r1
    else:
        if arr[r1] == 1 and arr[r2] == 2:  # 가위 vs 바위
            return r2
        elif arr[r1] == 1 and arr[r2] == 3:  # 가위 vs 보
            return r1
        elif arr[r1] == 2 and arr[r2] == 1:  # 바위 vs 가위
            return r1
        elif arr[r1] == 2 and arr[r2] == 3:  # 바위 vs 보
            return r2
        elif arr[r1] == 3 and arr[r2] == 1:  # 보 vs 가위
            return r2
        elif arr[r1] == 3 and arr[r2] == 2:  # 보 vs 바위
            return r1

def game(s, e):
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        r1 = game(s, mid)
        r2 = game(mid+1, e)
        return win(r1, r2)

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    print(f'#{tc+1} {game(1, n)}')