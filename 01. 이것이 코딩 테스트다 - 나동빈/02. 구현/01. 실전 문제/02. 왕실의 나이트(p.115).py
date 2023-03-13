input_data = input()
x = int(input_data[1])
y = int(ord(input_data[0])) - int(ord('a')) + 1

move = [(2,1), (2,-1),     #아래
        (-2,1), (-2,-1),   #위
        (1,2), (-1,2),     #오른쪽
        (1,-2), (-1,-2)]   #왼쪽

print(x,y)
result = 0
for i in range(8):
    knight_x = move[i][0] + x
    knight_y = move[i][1] + y
    print(knight_x,knight_y)
    if (knight_x > 0 and knight_x < 9) and (knight_y > 0 and knight_y < 9):
        result += 1

print(result)




