def ami_count(inp):
    prev = inp[0]
    cnt = 1
    D = {}
    B = {}
    for i in inp[1:]:
        if prev == i:
            cnt += 1
        elif i != prev:
            if int(prev) != 0 or cnt == 1:
                if cnt in D.keys():
                    D[cnt] += 1
                else:
                    D[cnt] = 1
            elif int(prev) == 0:
                if cnt in B.keys():
                    B[cnt] += 1
                else:
                    B[cnt] = 1
            cnt = 1 
        prev = i
    if inp[-1] == inp[-2]:
        if cnt in D.keys():
            D[cnt] += 1
        else:
            D[cnt] = 1
    else:
        D[cnt] += 1
    return D[1], sum([i*j if i != 1 else 0 for i,j in D.items()]), sum([i*j if i != 1 else 0 for i, j in B.items()])

print(ami_count('0111110001'))