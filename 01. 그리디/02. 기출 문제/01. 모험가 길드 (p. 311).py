n = int(input())
fear = list(map(int, input().split()))


sum = 0
cnt = 0
for i in range(1,n+1):

    if fear.count(i) != 0:
        mok = fear.count(i) // i
        rem = fear.count(i) % i

        sum += mok
        cnt += rem

        if cnt >= i:
            sum += 1
            cnt -= i


print(sum)








