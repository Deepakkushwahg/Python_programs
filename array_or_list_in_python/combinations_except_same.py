# all combinations of 1 2 3 except 111 222 333
lst=[]
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i==j==k:
                pass
            else:
                lst.append([i,j,k])

print(lst)
