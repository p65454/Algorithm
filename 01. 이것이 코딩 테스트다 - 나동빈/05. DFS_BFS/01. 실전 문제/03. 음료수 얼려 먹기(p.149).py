n, m = map(int, input().split())
icebox = []
for _ in range(n):
    icebox.append(list(map(int, input())))

print(icebox)
def dfs(x, y):
    if x < 0 or y < 0 or x > n-1 or y > m-1:
        return False
    if icebox[x][y] == 0:
        icebox[x][y] = 1
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)

        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            """어차피 처음으로 붙어있는 아이스크림 덩어리를 만나는 순간 재귀로 들어가서 
            덩어리째로 다 1이 들어가고 True는 한번만 반환하기 때문에, 아이스크림 덩어리당 result에 1씩 더해진다"""

            result += 1
            print(result)
print(result)

