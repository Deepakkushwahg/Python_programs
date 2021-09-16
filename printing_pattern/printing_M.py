n=int(input("Enter the size: "))
for i in range(0,n+1):
    for j in range(i,n+1):
        print(" ",end=' ')
    print("*",end=' ')
    for k in range(0,i):
        print(" ",end=' ')
    for k in range(0,i-1):
        print(" ",end=' ')
    if(i!=0):
        print("*",end=' ')
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i,n-1):
        print(" ",end=' ')
    if(i!=n and i!=0):
        print("*",end=' ')
    elif(i==0):
        print(" *",end=' ')
    for k in range(0,i):
        print(" ",end=' ')
    for k in range(0,i-1):
        print(" ",end=' ')
    if(i!=0):
        print("*")
    else:
        print()
