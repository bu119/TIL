# 한번에 두글자 단위로 암호화
# 5×5크기의 표
# 편의상 J가 아예 주어지지 않는다.
# (알파벳 26개를 모두 담기에는 칸이 한 개 부족해 I와 J를 동일한 것으로 생각)

# 먼저, 주어진 키를 5×5크기의 표로 변환
# 키를 한 글자씩 보면서 왼쪽 위 칸부터 한줄씩 표를 채운다.
# 이전에 봤던 알파벳이 한번 더 등장하면 무시하고 다음 글자
# 칸이 남는다면, 아직 등장하지 않은 알파벳을 순서대로 채워넣으면 된다.

message = list(input())
secretkey = list(input())
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
secretkey += alphabet
# 중복키 체크
check = set()

# 암호 배열
cipher = []
tmp = []
# 암호 배열 만들기
for word in secretkey:
    if word not in check:
        tmp.append(word)
        check.add(word)

    if len(tmp) == 5:
        cipher.append(tmp)
        tmp = []

# print(cipher)

# 다음, 암호화하려는 메세지를 두 글자씩 나눈다.
# LL같이 두 글자로 이루어진 쌍이 생기면 중간에 다른 글자를 넣어 쌍을 파괴
# 가장 앞에 있는 쌍 사이에 X를 넣고 뒤쪽은 새롭게 쌍을 구성
# 쌍이 XX였다면 X를 넣어서는 해결이 안되기 때문에 Q를 넣는 것으로 해결
# 마지막에 한 글자가 남는다면 이것도 암호화가 불가능하기 때문에 여기도 X를 덧붙여 강제로 쌍을 맞춰준다.

changemes = []
n = len(message)
idx = 0
if n > 1:
    while True:
        if message[idx] == message[idx+1]:
            if message[idx] == 'X':
                changemes.append([message[idx], 'Q'])
            else:
                changemes.append([message[idx], 'X'])
            idx += 1
        else:
            changemes.append([message[idx], message[idx+1]])
            idx += 2

        # break
        if idx == n-1:
            changemes.append([message[idx], 'X'])
            break
        elif idx == n:
            break
else:
    changemes.append([message[idx], 'X'])

# print(changemes)

# 마지막으로, 쌍을 만든 두 글자를 암호화


ans = []
for a, b in changemes:
    find = 0
    for i in range(5):
        for j in range(5):
            if cipher[i][j] == a:
                ax, ay = i, j
                find += 1
            if cipher[i][j] == b:
                bx, by = i, j
                find += 1

            if find == 2:
                break

        if find == 2:
            # 세 가지 경우
            # 1. 만약, 두 글자가 표에서 같은 행에 존재하면, 오른쪽으로 한 칸 이동한 칸에 적힌 글자로 암호화
            if ax == bx:
                ans.append(cipher[ax][(ay+1) % 5])
                ans.append(cipher[bx][(by + 1) % 5])
            # 2. 두 글자가 표에서 같은 열에 존재하면, 아래쪽으로 한 칸 이동한 칸에 적힌 글자로 암호화
            elif ay == by:
                ans.append(cipher[(ax + 1) % 5][ay])
                ans.append(cipher[(bx + 1) % 5][by])
            # 두 글자가 표에서 서로 다른 행, 열에 존재하면, 두 글자가 위치하는 칸의 열이 서로 교환된 위치에 적힌 글자로 암호화
            elif ax != bx and ay != by:
                ans.append(cipher[ax][by])
                ans.append(cipher[bx][ay])
            break

print(''.join(ans))