x = int(input("Enter the number of list: "))
n = int(input("Enter the size of each list: "))
ls = []
for i in range(1,x+1):
    ls.append([i*j for j in range(1,n+1)])
p = int(input("Enter the number: "))
q = int(input("Enter the number: "))
print(ls)
if(p<n and q<x):
    print("Verification success")
else:
    l = ls[p-1]
    ls[p-1]=ls[q-1]
    ls[q-1]=l
    print(ls)