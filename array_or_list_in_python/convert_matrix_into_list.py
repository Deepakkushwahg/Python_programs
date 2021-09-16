# program to convert matrix into list
mat=eval(input("Enter the matrix\n"))
lst=[]
for i in mat:
    for j in i:
        lst.append(j)
print("Your list is\n",lst)
