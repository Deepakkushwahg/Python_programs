f=open("my_intro.txt",'r')
lst=[]
for line in f:
    lst.append(line)
print(lst)
f.close()