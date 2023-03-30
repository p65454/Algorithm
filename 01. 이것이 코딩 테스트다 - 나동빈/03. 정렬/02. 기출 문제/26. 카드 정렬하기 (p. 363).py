# 26. 카드 정렬하기(p.363)
# https://www.acmicpc.net/problem/1715
import time, heapq
# start = time.time()
n = int(input())
card = []
for i in range(n):
    card.append(int(input()))

heapq.heapify(card)
sum_card = 0
front = 0
while len(card) != 1:
    front += heapq.heappop(card)
    front += heapq.heappop(card)
    sum_card += front
    heapq.heappush(card, front)
    front = 0
    print(f'card = {card}, sum_card = {sum_card}, front={front}')

print(sum_card)
# end = time.time()
# print(f'시간 = {end-start}')
