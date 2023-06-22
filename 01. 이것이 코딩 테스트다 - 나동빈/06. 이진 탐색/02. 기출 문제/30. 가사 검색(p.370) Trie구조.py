# https://school.programmers.co.kr/learn/courses/30/lessons/60060

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
    answer = []
    array = [[] for _ in range(100001)]
    for word in words:
        array[len(word)].append(word)

    for q in queries:
        trie = Trie()
        result = 0
        for w in array[len(q)]:
            if q[0] != '?':
                index = end_qm(q)
                query = q[:index]
                trie.insert(w, len(q))
                if trie.search(query):
                    result += 1

                print(result)
            elif q[0] == '?' and q[-1] == '?':
                result += 1
            else:
                index = front_qm(q)
                query = q[index:]
                trie.insert(w, len(q))
                if trie.search(query):
                    result += 1

                print(result)
        print('------------')
        answer.append(result)
        print(answer)
    return answer


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word, n):
        cur_node = self.root  # 처음 루트로 잡아준다
        for c in word:  # 받은 문자열 하나하나에 대해서
            x = n
            if c not in cur_node:  # 현재 노드에 그 문자가 있으면 들어가고, 그렇지 않으면 새로 만든다
                cur_node[c] = {}
                #print(cur_node)
            cur_node = cur_node[c]
            #print(cur_node)
            #print(cur_node)
            x -= 1
            if x == 0:
                cur_node['*'] = word
            print(cur_node, x)
        cur_node["*"] = word  # "*" 노드를 만들어 '단어의 끝' 표시를 해 준다.
        #print('--------------')
        # {'f':{'r': {'o': {'d': {'o': {'*': 'frodo'}}}}}}
    def search(self, query):
        cur_node = self.root
        for c in query:
            if c in cur_node:
                cur_node = cur_node[c]
            else:
                return False
        return "*" in cur_node  # "*" 가 해당 노드에 있으면 그 글자로 끝나는 단어가 있다는 것이다.\
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
words3 = ["a", "aaaa", "abaa", "abba", "abbb", "aaba", "aabb"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
queries2 = ['?????', '????', '?????', '??????', '???', '????????']
queries3 = ['fro?', 'f?', '?r', '????t', '?????', 'fr???']
queries4 = ["?", "a", "b", "???a", "??aa", "??ab", "aa??", "aaa?"]
#print(solution(words, queries))

#print(trie.search('fro??'))
print(solution(words, queries))
