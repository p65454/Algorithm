
res = []
def f(i,N):
    if i == N:
        res.append(p)
    else:
        for j in range(i,N):
            p[i],p[j] = p[j],p[i]

            f(i+1,N)
            p[i], p[j] = p[j], p[i] # 복구


N = 3
p = [x for x in range(1,N+1)]
f(0,N)
