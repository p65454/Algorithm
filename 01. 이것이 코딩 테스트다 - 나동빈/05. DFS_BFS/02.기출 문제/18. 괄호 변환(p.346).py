#https://programmers.co.kr/learn/courses/30/lessons/60058
p = list(input())
del p[0]
del p[-1]
#print(p)
memory_u = []
# '올바른 괄호 문자열' 인지 아닌지 테스트하는 함수
def good_string_test(p):
    cnt = 0
    if p:
        if p[0] == '(' and p[-1] == ')':
            for i in p:
                if i == '(':
                    cnt += 1
                if i == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return True
        else:
            return False
    else:
        return False

# p346을 수행하는 함수
def transform1(p):
    global u, v
    temp = []

    if not p:
        return p

    for i in range(len(p)):
        if p[i] == '(':
            temp.append(1)
        if p[i] == ')':
            temp.append(-1)
        if sum(temp) == 0:
            u = p[:i+1]
            v = p[i+1:]
            print(f'u = {u}')
            print(f'v = {v}')
            break


    if good_string_test(u):
        memory_u.append(u)
        transform1(v)
    else:
        newstring = []
        newstring.append('(')
        newstring.append(transform1(v))
        newstring.append(')')
        print(u)
        del u[0]
        del u[-1]
        for i in u:
            if i == '(':
                i = ')'
            else:
                i = '('
        for i in u:
            newstring.append(i)

    return memory_u + newstring
# p347을 수행하는 함수
def transform2(u, v):
    newstring = []
    newstring.append('(')
    newstring.append(transform1(v))
    newstring.append(')')
    del u[0]
    del u[-1]
    for i in u:
        if i == '(':
            i = ')'
        else:
            i = '('
    for i in u:
        newstring.append(i)
    return newstring





def solution(p):
    #print(good_string_test(p))
    if good_string_test(p):
        a = '\"' + ''.join(p) + '\"'
        answer = print(a)
    else:
        a = '\"' + ''.join(transform1(p)) + '\"'
        answer = print(a)

    return answer

solution(p)
