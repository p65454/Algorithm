#https://programmers.co.kr/learn/courses/30/lessons/60058

#print(p)

# '올바른 괄호 문자열' 인지 아닌지 테스트하는 함수
def good_string_test(p):
    cnt = 0

    if p[0] == '(' and p[-1] == ')':
        for i in p:
            if i == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    return False
        return True
    else:
        return False


# p346을 수행하는 함수
def transform1(p):
    temp = []
    answer = ''
    if p == '':
        return answer

    for i in range(len(p)):
        if p[i] == '(':
            temp.append(1)
        if p[i] == ')':
            temp.append(-1)
        if sum(temp) == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    print(f'u = {u}')
    print(f'v = {v}')

    # 올바른괄호문자열 이면
    print(good_string_test(u))
    print('-------------------')
    if good_string_test(u):
        answer = u + transform1(v)
        print(answer)

    #올바른괄호문자열 아니면
    else:
        answer = '('
        answer += transform1(v)
        answer += ')'

        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += ''.join(u)
        print(f'answer = {answer}')
    return answer
# p347을 수행하는 함수






def solution(p):
    #print(good_string_test(p))
    if good_string_test(p):
        answer = ''.join(p)
    else:
        answer = transform1(p)
        #answer = transform1(p)

    return answer


p = "()))((()"
print(solution(p))
