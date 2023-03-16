s = list(input())
L = len(s)//2
n = 0


result = []   # ababcdcd
num_press = []
for i in range(1, L + 1):  # i가 1부터 리스트 절반까지만 돈다. i = 몇개단위로 압축할건지
    temp1 = [] # temp1, temp2 에 저장하면서 비교
    temp2 = []
    cnt = 1

    for j in range(len(s)):

        if len(temp1) != i:
            temp1.append(s[j])
            print(f'temp1={temp1}, temp2={temp2}, i={i}, j={j}, cnt={cnt}, result={result}')
        else:
            temp2.append(s[j])
            print(f'temp1={temp1}, temp2={temp2}, i={i}, j={j}, cnt={cnt}, result={result}')
            print('------------------------------------------')

        # temp1과 temp2에 i개만큼(비교할문자의 길이) 들어갔다면 비교한다
        if len(temp1) == i and len(temp2) == i:

            if temp1 == temp2:
                cnt += 1
            else:
                if cnt > 1:
                    result.append(str(cnt))
                result += temp1   # append로 넣으면 리스트안에 리스트생겨서 join을 못씀
                temp1 = temp2
                cnt = 1
            temp2 = []

        if j == len(s) - 1:
            if cnt > 1:
                result.append(str(cnt))
            result += temp1
            result += temp2
    print(f'최종result = {result}')
    string = ''.join(result)

    num_press.append(len(string))
    print(f'num_press = {num_press}')
    result = []
if len(num_press) != 0:
    answer = min(num_press)
else:
    answer = 1


# a a b a b c d c d


# print(s[:-5])
# print(s[-5:-2])
    # n = len(s) - (2*i - 1)
    # n = len(s) // i
    # sum = (n * (n+1)) // 2   # sum = 문자열 i개 단위일때 비교할 횟수
    # for j in range(n-1):
    #     if s[:-(len(s)-i)] == s[-(len(s)-i)+i*j:-(len(s)-i)+i+i*j]:  # 리스트 절반 나눠서 앞뒤가 똑같을 때
    #         sum += 1
    #         print(f'sum = {sum}')
    #         print(s[:-(len(s)-i)],s[-(len(s)-i)+i*j:-(len(s)-i)+i+i*j])
    #
    #
    # m.append((i,sum))
    # sum = 0
    # print(m)

