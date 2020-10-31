deneme = "LULUDRRRLDLDURUURRLLDRRLLURRDURLLLRLDDLRDLRRULLDLDRRLLLULDULLRDDLULUDUULRLRURUUDLLULULDRLRRULULDRULRLLUDRRUURRULDRLRURLLULUDDLRDUDRDRLDRRLULDDLRDRDLRLLULDDLLDDUDLRLDDRDLLDRRULLLLRLULDULRLDDRRRDDRRDUULDDDLLUDDDRURDUDDDLRURRUDLRRLUDDUDUDDDRLLRUDULURRRLLLRLRLLLUUURRDDUDRLDUDLLLLRLLDURLRRUDRULDRDUUURULDLLDULDUDLLUDLUUUULRRURRULULDULRULDLUDDRRDUULLDDDRLDDRRDDDLDUDURUUURULUDUDULDDLLDURRUURRLLLLULRRURLL"
upCounter = 0
downCounter = 0
rightCounter = 0
leftCounter = 0

for i in deneme:
    if i == "U":
        upCounter+=1
    elif i == "D":
        downCounter+=1
    elif i == "R":
        rightCounter+=1
    elif i == "L":
        leftCounter+=1

upCounter = upCounter % 6
downCounter = downCounter % 6
rightCounter = rightCounter % 11
leftCounter = leftCounter % 11

print("UP",upCounter)
print("DOWN",downCounter)
print("RIGHT",rightCounter)
print("LEFT",leftCounter)