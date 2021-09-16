# Program to get all the strings which contains all vowels
st=eval(input("Enter the set of strings\n"))
lst=[]
for i in st:
    f=0
    for j in i:
        if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
            f=1
    if(f==1):
        lst.append(i)
print("Set of string which contains vowels is\n",set(lst))