dic_words = {'frodo': 5, 'front': 5, 'frost': 5, 'frozen': 6, 'frame': 5, 'kakao': 5}
search_key = 'fro'

matching_keys = []
for key in dic_words:
    if search_key in key:
        matching_keys.append(key + ' (있음)')
    else:
        matching_keys.append(key + ' (없음)')

print(matching_keys)