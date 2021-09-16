f=open('table.txt', 'w')
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        f.write(str(i*j)+'\t')
    f.write('\n')
f.close()