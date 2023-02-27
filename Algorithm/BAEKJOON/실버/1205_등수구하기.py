# 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하라.
# 만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력
# 리스트에 있는 점수 N개
# 랭킹 리스트에 올라 갈 수 있는 점수의 개수 P

#  현재 랭킹에 같은 점수가 있니?
def sameNum(num):
    if num in grade:
        return 1
    return 0

# 랭킹에 빈자리 있니?
def empty():
    if p-n:
        return 1
    return 0

# 랭킹 리스트 점수가 있니?
def check():
    if n:
        return 1
    return 0


n, new, p = map(int, input().split())
ans = -1

if check():
    grade = list(map(int, input().split()))
    if sameNum(new):
        # 마지막 점수를 기준으로 구분
        if grade[-1] < new:
            # 같은 점수 찾기
            for i in range(n):
                if grade[i] == new:
                    ans = i + 1
                    break
        elif grade[-1] == new:
            if empty():
                for j in range(n):
                    if grade[j] == new:
                        ans = j + 1
                        break
        else:
            # 빈자리 확인
            if empty():
                ans = n + 1
    else:
        #  같은 숫자 없음
        #  더 높은 점수인지 확인
        if grade[-1] < new:
            for k in range(n):
                if grade[k] < new:
                    ans = k + 1
                    break
        else:
            # 빈자리 확인
            if empty():
                ans = n + 1
else:
    if empty():
        ans = n+1

print(ans)