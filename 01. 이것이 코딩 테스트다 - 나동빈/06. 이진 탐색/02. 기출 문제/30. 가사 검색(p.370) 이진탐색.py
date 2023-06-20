def front_qm(array): # 물음표가 왼쪽에 있을 때 물음표 끝나는 index + 1 반환(슬라이싱 하기 위해)
    start = 0
    end = len(array) - 1
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == '?' and array[mid + 1] != '?':
            return mid + 1
        elif '?' in array[mid + 1:]:
            start = mid + 1
        else:
            end = mid - 1

def end_qm(array): # 물음표가 오른쪽에 있을 때 물음표 시작점 index 반환
    start = 0
    end = len(array) - 1
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == '?' and array[mid - 1] != '?':
            return mid
        elif '?' in array[:mid]:
            end = mid - 1
        else:
            start = mid + 1

def solution(words, queries):
    dic_words = {}
    result = []
    check = set()
    for word in words:
        dic_words[word] = len(word)

    print(dic_words)
    for i in range(len(queries)):
        list_q = list(queries[i])
        print(list_q)

        if len(list_q) in dic_words.values(): # query랑 같은 길이의 word가 있을 때
            cnt = 0
            if list_q[0] == '?' and list_q[-1] == '?':  # 전체가 ?로 구성된경우
                for key, value in dic_words.items():
                    if value == len(list_q):  # 쿼리랑 같은 길이의 단어일 때
                        cnt += 1

                result.append(cnt)
            elif list_q[0] == '?' and list_q[-1] != '?': # 앞에 ? 있는경우
                for key, value in dic_words.items():
                    if value == len(list_q):
                        index = front_qm(list_q)
                        key = list(key)
                        #print(index, key[index:], list_q[index:])
                        if key[index:] == list_q[index:]:
                            cnt += 1

                result.append(cnt)
            else: # 뒤에 ? 있는경우
                for key, value in dic_words.items():
                    if value == len(list_q):
                        index = end_qm(list_q)
                        key = list(key)
                        if key[:index] == list_q[:index]:
                            cnt += 1
                result.append(cnt)
        else: # query랑 같은 길이의 word가 존재하지 않을 때
            result.append(0)

    return result

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
queries2 = ['?????', '????', '?????', '??????', '???', '????????']
queries3 = ['fro?', 'f?', '?r', '????t', '?????', 'fr???']
print(solution(words, queries))

'''
 words1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries1 = ["fro??", "????o", "fr???", "fro???", "pro?"]\

    #[3, 2, 4, 1, 0]
'''