# import sys; sys.stdin = open('베이비진_input.txt')

def baby_test(c):
    # triplet
    for i in range(10):
        if c[i] >= 3:
            return True
    for i in range(8):
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            return True


def game():
    c1 = [0] * 10
    c2 = [0] * 10
    for i in range(12):
        n = arr[i]
        if i % 2 == 0:
            c1[n] += 1
        else:
            c2[n] += 1

        # 3장 이후부터
        if i > 4:
            if i % 2 == 0:
                if baby_test(c1):
                    return 1
            else:
                if baby_test(c2):
                    return 2
    return 0


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {game()}')