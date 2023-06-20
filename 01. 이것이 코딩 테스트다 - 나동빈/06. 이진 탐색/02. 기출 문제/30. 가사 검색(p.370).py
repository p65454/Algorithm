# https://programmers.co.kr/learn/courses/30/lessons/60060

def solution(words, queries):
    cnt = 0
    answer = []
    for _ in range(len(queries)):
        answer.append(0)

    for i in range(len(queries)):
        list_q = list(queries[i])

        for j in range(len(words)):
            list_w = list(words[j])
            cnt = 0
            if len(list_q) == len(list_w):
                for k in range(len(list_q)):
                    if list_q[k] == list_w[k] or list_q[k] == '?':
                        cnt += 1
            if cnt == len(list_q):
                answer[i] += 1
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))



'''
 words1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries1 = ["fro??", "????o", "fr???", "fro???", "pro?"]\
        
    #[3, 2, 4, 1, 0]
'''