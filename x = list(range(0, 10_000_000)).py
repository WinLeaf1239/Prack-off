x = list(range(0, 10_000_000))
iskomoe = 9_247_236
is_found = False
for i in range (0,len(x), 2**i): 
    jump = 2**i
    if iskomoe < x[i]:
        while is_found is False :
            mid = (i - (i-jump) ) // 2
            if
"""        for j in range(i-jump,i):
            if x[j] == iskomoe :
                index = j
                is_found=True
                break """
    if x[index] == iskomoe :
        break
for j in range(i,len(x),2**i): #Линейный поиск последнего куска, он будет меньше чем прыжок
    if x[j] == iskomoe :
        index = j
        is_found=True
        break
