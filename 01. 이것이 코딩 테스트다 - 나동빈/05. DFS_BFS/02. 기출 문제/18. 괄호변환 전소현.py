# 18. 괄호 변환 (p. 346)
# https://programmers.co.kr/learn/courses/30/lessons/60058
from collections import deque


def is_correct(deq):
    num = 0
    for i in range(len(deq)):
        char = deq.popleft()
        if char == '(':
            num += 1
        elif char == ')':
            num -= 1
        if num < 0:
            return False
    return True


def correct_u(deq):
    deq.popleft()
    deq.pop()
    for _ in range(len(deq)):
        char = deq.popleft()
        if char == '(':
            deq.append(')')
        elif char == ')':
            deq.append('(')
    return deq


answer = '"'
num = 0


def solution(p, ans, cnt):
    cnt += 1
    print(f"{cnt} - 입력 문자열: {p}")
    # 1. 입력이 빈 문자열일 경우, 빈 문자열을 반환한다.
    if not p:
        return ans + ''.join('"')

    # 2. 입력받은 문자열을 두 '균형잡힌 괄호 문자열' u와 v로 분리한다.
    u = deque()
    v = deque(p)

    separated = False
    left, right = 0, 0
    for _ in range(len(p)):
        char = v.popleft()
        if not separated:
            u.append(char)
        else:
            v.append(char)

        if char == '(':
            left += 1
        elif char == ')':
            right += 1
        if left == right:
            separated = True
        # print(f"u: {u}, v: {v}")
        # print(f"left: {left}, right: {right}")

    # 3. 수행한 결과 문자열을 u에 이어붙인 후 반환한다.
    # 3-1. 문자열 u가 '올바른 괄호 문자열'이라면 v에 대해 1단계부터 다시 수행한다.
    if is_correct(u):
        print(f"----------> ans: {ans}")
        ans = ans + ''.join(u) + solution(''.join(v), ans, cnt)
    # 4. 문자열 u가 '올바른 괄호 문자열'이 아니면 아래의 과정을 수행한다.
    else:
        print(f"----------> ans: {ans}")
        ans = ans + '(' + solution(''.join(v), ans, cnt) + ')' + ''.join(correct_u(u))
    print(f"----------> ans: {ans}")

    return answer


# Input
p1 = '"(()())()"'
# p2 = '")("'
# p3 = '"()))((()"'

# Output
p = p1.strip('"')
print(solution(p, answer, 0))