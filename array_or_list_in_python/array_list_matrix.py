# program to display the matix of given list
lst=eval(input())
r, c=map(int, input().split('x'))
if(r*c==len(lst)):
    ls=[]
    m=[]
    count=0
    for i in lst:
        count+=1
        ls.append(i)
        if(count==c):
            m.append(ls)
            ls=[]
            count=0
    for i in m:
        print(*i)
else:
    print("None")
