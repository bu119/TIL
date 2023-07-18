# 부자는 강아지와 코인을 좋아하고, 전기차를 타고다닌다.
# 화성엔 무시무시한 외계 곰팡이가 있다.
# 부자는 자신의 인공위성을 가지고 화성의 안전한 곳을 찾으려고 한다.

# 모든 셀의 외계 곰팡이 개체 수는 다르다.

# 어떠한 셀이 안전하다는 것은
# 해당 셀과 같은 행, 혹은 같은 열에 있는 다른 셀 중 외계 곰팡이 개체 수가 더 높은 것이 없다는 것을 뜻한다.

# 각 셀의 외계 곰팡이 개체 수는 계속 증식
# 증식으로 인해 외계 곰팡이 개체 수가 줄어드는 일은 없으며,
# 여전히 모든 셀의 외계 곰팡이 개체 수는 다르게 유지된다.

# 관측 보고서를 받는 즉시 안전한 셀의 개수를 파악한다.
# Q개의 관측 보고서를 받고, 매번 안전한 셀의 개수를 계산하고, 그 계산한 값의 합을 출력하여라.

t = int(input())
for tc in range(t):
    n, m, q = map(int, input().split())
    mold = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for _ in range(q):
        r, c, x = map(int,input().split())
        mold[r-1][c-1] = x

        # 각 행에서 큰 수 구하기
        for row in range(n):
            maxV = max(mold[row])
            column = mold[row].index(maxV)
            flag = True
            for i in range(n):
                if mold[i][column] > maxV:
                    flag = False
                    break
            if flag:
                ans += 1
    print(f'#{tc+1} {ans}')

