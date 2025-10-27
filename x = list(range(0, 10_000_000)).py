x = list(range(0, 10_000_000))
iskomoe = 9_247_236
is_found = False
index = 0
jump = 1
for i in range (0,len(x), jump): 
    print(f"{jump}")
    jump = 2**i
    if iskomoe < x[i]:
        start = i - jump
        end = i
        while is_found is False :
            mid = (end - (start) ) // 2
            if x[mid] == iskomoe:
                index = mid
                is_found = True
                break
            elif x[mid] < iskomoe:
                end=mid
            else:
                start=mid
    if is_found :
        break
"""        for j in range(i-jump,i):
            if x[j] == iskomoe :
                index = j
                is_found=True
                break """
start = i - jump
end = i
while is_found is False :
    mid = (end - (start) ) // 2
    if x[mid] == iskomoe:
        index = mid
        is_found = True
        break
    elif x[mid] < iskomoe:
        end=mid
    else:
        start=mid

if is_found 