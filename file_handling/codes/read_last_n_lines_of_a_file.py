f=open("E:\\Python programming\\file handling\\files\\my_intro.txt",'r')
c=0
for line in f:
    c+=1
f.seek(0,0)
n=int(input("Enter the number of lines\n"))
a=0
while(a<c-n):
    data=f.readline()
    a+=1
a=0
while(a<n):
    da=f.readline()
    print(da)
    a+=1
f.close()
