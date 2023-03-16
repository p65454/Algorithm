m, n = map(int, input().split())
# m = key, n = lock m<=n
key = []
lock = []
for _ in range(m):
    key.append(list(map(int, input().split())))
for _ in range(n):
    lock.append(list(map(int, input().split())))

for i in range(m):
    print(key[i], end='\n')

print('---------------------------')

for i in range(n):
    print(lock[i], end='\n')

