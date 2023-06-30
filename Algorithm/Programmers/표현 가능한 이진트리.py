import math
def makeBinary(num):
    if num == 1:
        return 1

    # 2진수 변환
    binary = bin(num)[2:]
    # 2^n - 1꼴의 자릿수를 가져야함.
    n = 2 ** (int(math.log(len(binary), 2)) + 1) - 1
    binary = '0' * (n - len(binary)) + binary

    if binary[len(binary) // 2] == '1' and checkTree(binary, True):
        return 1
    else:
        return 0
def checkTree(binary, parent):
    # 중앙값(자손) 기준으로 재귀적으로 확인
    mid = len(binary) // 2
    if binary:
        if binary[mid] == '1':
            son = True
        else:
            son = False
    else:
        return True

    # 내가 존재하면 부모가 존재해야함.
    if son and not parent:
        return False
    else:
        return checkTree(binary[mid + 1:], son) and checkTree(binary[:mid], son)


def solution(numbers):
    answer = []
    # print(numbers)
    for num in numbers:
        binary = makeBinary(num)
        # 누군가의 부모 노드는 항상 존재해야함.
        answer.append(makeBinary(num))

    return answer

print(solution([63, 111, 95]))