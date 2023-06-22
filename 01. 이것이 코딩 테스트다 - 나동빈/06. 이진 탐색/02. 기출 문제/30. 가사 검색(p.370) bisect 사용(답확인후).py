from bisect import bisect_left, bisect_right

def count_match(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

def solution(words, queries):
    answer = []
    array = [[] for _ in range(100001)]
    reverse_array = [[] for _ in range(100001)]
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])
    print(queries)
    for i in range(100001):
        array[i].sort()
        reverse_array[i].sort()
    for q in queries:

        if q[0] != '?':
            result = count_match(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            print(result)
        else:
            result = count_match(reverse_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(result)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
queries2 = ['?????', '????', '?????', '??????', '???', '????????']
queries3 = ['fro?', 'f?', '?r', '????t', '?????', 'fr???']
print(solution(words, queries))
