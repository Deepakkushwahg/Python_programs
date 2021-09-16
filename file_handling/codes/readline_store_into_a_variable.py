f=open('copy_my_intro.txt','r+')
lst=[]
for line in f:
    lst.append(line)
var="".join(lst)
print(var)
f.close()