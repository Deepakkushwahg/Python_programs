# program to find the decimal of all the items in given set after flipping the bits (firstly convert decimal to binary).
set1 = eval(input("Enter the set\n"))
new_set=set()
for i in set1:
    s=0
    x=list(str(bin(i)[2:]).zfill(len(set1)))
    for j in range(len(x)):
        if x[j]=='0':
            x[j]='1'
        else:
            x[j]='0'
    x=int("".join(x))
    c=0
    while x>0:
        r=x%10
        if r==1:
            s=s+2**c
            c+=1
        else:
            c+=1
        x=x//10
    new_set.add(s)
print(new_set)