x = [3,6,9,11,17,29,33,52,69]
y = [0,1,2,3,4,5,6,7,8]
iskomoe = 52
jump = int(len(x)**0.5)
index = 0
is_found = False
for i in range(0,len(x),jump) :
    if iskomoe < x[i]:
        for j in range(i-jump,i):
            if x[j] == iskomoe :
                index = j
                is_found=True
                break 
    if x[index] == iskomoe :
        break
for j in range(i,len(x)): #Линейный поиск последнего куска, он будет меньше чем прыжок
    if x[j] == iskomoe :
        index = j
        is_found=True
        break
if is_found:
    print(index)
else:
    print('Not found')