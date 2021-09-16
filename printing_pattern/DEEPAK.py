n=int(input("Enter the size: "))
for i in range(1,n+1):
    print("      #",end='')
    for j in range(1,i+1):
        print("  ",end='')
    print("#",end='')
    for j in range(i,n+1):
        print("  ",end='')
    k=0
    while(k < 2):
        if(i == 1 or i == n):
            print("      #",end='')
            for j in range(1,n+1):
                print(" #",end='')
        else:
            print("      #",end='')
            for j in range(1,n+1):
                print("  ",end='')
        k+=1
    if(i == 1 or i == n):
        print("      #",end='')
        for j in range(1,n+1):
            print(" #",end='')
        print("  ",end='')
    else:
        print("      #",end='')
        for j in range(1,n+1):
            print("  ",end='')
        print(" #",end='')
    if(i == 1):
        print("       ",end='')
        for j in range(1,n+1):
            print(" #",end='')
        print("  ",end='')
    elif(i == n):
        print("      #",end='')
        for j in range(1,n+1):
            print(" #",end='')
        print(" #",end='')
    else:
        print("      #",end='')
        for j in range(1,n+1):
            print("  ",end='')
        print(" #",end='')
    print("      #",end='')
    for j in range(i,n+1):
        print("  ",end='')
    print("#")
for i in range(1,n+1):
    print("      #",end='')
    for j in range(i,n+1):
        print("  ",end='')
    print("#",end='')
    for j in range(1,i+1):
        print("  ",end='')
    k = 0
    while(k < 2):
        if(i == n):
            print("      #",end='')
            for j in range(1,n+1):
                print(" #",end='')
        else:
            print("      #",end='')
            for j in range(1,n+1):
                print("  ",end='')
        k+=1
    print("      #",end='')
    for j in range(1,n+1):
        print("  ",end='')
    print("        #",end='')
    for j in range(1,n+1):
        print("  ",end='')
    print(" #",end='')
    print("      #",end='')
    for k in range(1,i+1):
        print("  ",end='')
    print("#")
