n=int(input("Enter the size: "))
if(n%2==0):
    for i in range(1,n+1):
        for l in range(1,n+1):
            print("  ",end='')
        for j in range(i,n+1):
            print("  ",end='')
        for k in range(1,i+1):
            print("#",end='')
        for k in range(1,i):
            print("#",end='')
        print(" ")
else:
    for i in range(1,n+1):
        for l in range(1,n):
            print("  ",end='')
        for j in range(i,n+1):
            print("  ",end='')
        for k in range(1,i+1):
            print("#",end='')
        for k in range(1,i):
            print("#",end='')
        print(" ")
for i in range(1,n+1):
    for j in range(1,n//2+1):
        print("  ",end='')
    for k in range(1,n+1):
        print("#",end='')
    for l in range(1,n+1):
        print("  ",end='')
    for m in range(1,n+1):
        print("#",end='')
    print(" ")
