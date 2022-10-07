line = []
line = input().split(' ')
m, n = line
m, n = int(m), int(n)
basa = []
ones_basa = []   # список координат единичек
ones_border = []  # это список единицек по краю, пригодится 
for i in range (m):
    basa.append(list(map(int, input().split())))
    for i in range(n):
        if basa[i][j]==1:
            ones_basa.append([i, j])
        elif (i == 0 pr i = m-1) and (j == 0 or j==n-1):
            ones_border.append((i,j))

