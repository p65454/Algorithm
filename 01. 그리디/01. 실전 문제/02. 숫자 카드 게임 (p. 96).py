n, m = map(int, input().split())
card = []
card_min = []
for _ in range(n):
    card.append(list(map(int, input().split())))

for i in range(n):
    card_min.append(min(card[i]))

result = max(card_min)
print(card_min)
print(result)

