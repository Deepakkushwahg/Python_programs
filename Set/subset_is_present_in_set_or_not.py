# program to check entered subset is present in a given set or not.
set = eval(input("Enter the set\n"))
subset = eval(input("Enter the set\n"))
c=0
for i in subset:
    if i in set:
        c+=1
if c==len(subset):
    print("Yes, subset is present in a set")
else:
    print("No, subset is not present in a set")