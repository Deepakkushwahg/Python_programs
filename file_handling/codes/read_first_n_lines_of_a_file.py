x=open("E:\\file handling\\table.txt",'r')
n=int(input("Enter the number of lines\n"))
k=0
while(k<n):
    data=x.readline()
    print(data)
    k+=1
x.close()
