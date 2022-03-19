ant = []
for i in range(10):
    arr = [int(x) for x in input().split()]
    ant.append(arr)

x = 1
y = 1
ant[y][x] = 9
while 1:
    if ant[y][x] == 0:
        ant[y][x] = 9
    elif ant[y][x] == 2:
        ant[y][x] = 9
        break
    if ant[y][x+1] !=1:
        x += 1
    elif ant[y + 1][x] !=1:
        y += 1

    elif ((ant[x][y + 1] == 1 and ant[x + 1][y] == 1) or (x == 9 and y == 9)):
        break
    else:
        break

for i in range(10):
    for j in range(10):
        print(ant[i][j], end=' ')
    print()
