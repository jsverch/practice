
arr = [(1, 1, 1, 0, 0, 0),
(0, 1, 0, 0, 0, 0),
(1, 1, 1, 0, 0, 0),
(0, 0, 2, 4, 4, 0),
(0, 0, 0, 2, 0, 0),
(0, 0, 1, 2, 4, 0)]

hgs = list()
for x in range(0, 4):
    for y in range(0, 4):
        ch = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y]\
             + arr[x+2][y+1] + arr[x+2][y+2]
        hgs.append(ch)

print max(hgs)


