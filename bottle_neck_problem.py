# program to solve bottle neck problem
n=int(input("Enter number of bottles: "))
lst=list(map(int, input("Enter the sizes of bottle\n").split()))
x=max(lst)
lst1=[x for i in lst if i==x]
print("Minimum number of visible bottles are",len(lst1))