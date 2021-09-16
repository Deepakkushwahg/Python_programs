f=open("E:\\Python programming\\file handling\\files\\prime.txt",'w')
n=int(input("Enter the limit: "))
if(n==2):
    f.write('2')
else:
    f.write('2')
    for i in range(3,n+1):
        c=0
        for k in range(2,i):
            if(i%k==0):
                c=1
        if(c==0):
            f.write(' '+str(i))
f.close()
