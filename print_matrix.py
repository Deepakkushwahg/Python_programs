lst=list(map(int, input("Enter the elements\n").split(' ')))
r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
if(r*c==len(lst)):
    ls=[]
    m=[]
    count=0
    for i in lst:
        count += 1
        ls.append(i)
        if(count==c):
            m.append(ls)
            ls=[]
            count=0
    print(m)
    for i in m:
        print(*i)
else:
    print("Invalid matrix configuration")
