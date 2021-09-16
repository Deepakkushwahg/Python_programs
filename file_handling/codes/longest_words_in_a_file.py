f=open('copy_my_intro.txt','r+')
for line in f:
    lst1=line.split()
    lst1.sort(key=len)
    for i in lst1:
        if len(i)==len(lst1[-1]):
            print(i)
f.close()