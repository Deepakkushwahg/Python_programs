f=open('copy_my_intro.txt','r+')
x=open('updated_my_intro.txt','w')
for line in f:
    data=line.replace('\n',' ')
    x.write(data)
f.close()
