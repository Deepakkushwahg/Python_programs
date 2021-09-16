f=open('copy_my_intro.txt','r+')
c=0
for line in f:
    lst1=line.split()
    for i in lst1:
        c+=1
print("Frequency of words is ",c)
f.close()