# n = int(input())
# array1 = list(map(int, input().split()))
# m = int(input())
# array2 = list(map(int, input().split()))

class Node:
    def __init__(self, value):
        self.value = value ##노드의 값을 지정
        self.right = None ## 왼쪽 공간을 만들어주는 것
        self.left = None ## 오른쪽 공간을 만들어주는 것

head = Node(1)
print( head.value,
       head.right,
       head.left,
       sep = '\n')


class NodeMgmt:  ##Mgmt는 Management를 의미합니다. 즉 노드를 관리하겠다는 의미입니다.
    def __init__(self, head):
        self.head = head  ## Root Node를 지정해주는 칸입니다.

    def insert(self, value):  ## 이제 값을 추가해주는 논리를 구성합니다.
        self.current_node = self.head  ## 시작 값은 Root Node입니다.

        while True:
            if value < self.current_node.value:  ## 만약 현재 노드 값보다 value가 작다면
                if self.current_node.left != None:  ## 그리고 만약 왼쪽 노드 값이 null이 아니라면
                    self.current_node = self.current_node.left  ## 왼쪽으로 이동한다.
                else:  ## 만약 비어있다면
                    self.current_node.left = Node(value)  ## 노드로서 값을 지정해준다.
                    break  ## 삽입이 끝났으니 Loop를 종료한다.

            else:  ## 만약 현재 노드 값보다 Value가 크다면
                if self.current_node.right != None:  ## 그리고 만약 오른쪽 노드 값이 Null이 아니라면
                    self.current_node = self.current_node.right  ## 오른쪽으로 이동한다.

                else:  ## 만약 오른쪽 값이 비어있다면
                    self.current_node.right = Node(value)  ## 노드로서 값을 지정해준다.
                    break



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)