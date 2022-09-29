def bus(idx, cnt, energy):
    global ans

    if ans < cnt:
        return

    if idx == n-1:
        if cnt < ans:
            ans = cnt
        return
    else:
        bus(idx + 1, cnt+1, busstop[idx]-1)
        if energy > 0:
            bus(idx + 1, cnt, energy-1)



t = int(input())
for tc in range(t):
    n, *busstop = map(int, input().split())

    ans = n

    bus(1, 0, busstop[0]-1)
    print(f'#{tc+1} {ans}')