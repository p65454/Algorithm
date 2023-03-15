n = input()
a = list(n)

len_a = len(a)//2
s1 = a[:len_a]
s2 = a[len_a:]

int_s1 = list(map(int, s1))
int_s2 = list(map(int, s2))
if sum(int_s1) == sum(int_s2):
    print('LUCKY')
else:
    print('READY')

