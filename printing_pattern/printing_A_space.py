n=int(input("Enter the size : "))
if(n>=3):
    for l in range(1,2*(n+1)+5):
        print("#",end=' ')
    print(" ")
    for i in range(0,n+1):
        for j in range(i,n+1):
             print("#",end=' ')
        print("     ",end=' ')
        for k in range(0,i):
            if(i==n//2):
                print("  ",end=' ')
            else:
                print("#",end=' ')
        for k in range(0,i):
            if(i==n//2):
                print("  ",end=' ')
            else:
                print("#",end=' ')
        print("     ",end=' ')
        for j in range(i,n+1):
            print("#",end=' ')
        print(" ")
    for l in range(1,2*(n+1)+5):
        print("#",end=' ')
    print(" ")
else:
    print("Please enter the size above 2")
