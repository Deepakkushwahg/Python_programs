n=int(input("Enter the size : "))
for i in range(1,n):
    for j in range(i,n+1):
         print("$",end=' ')
    for k in range(1,i):
         print("  ",end=' ')
    for k in range(1,i):
         print("  ",end=' ')
    for j in range(i,n+1):
         print("$",end=' ')
    print("\n")
