# Program to get all subsets of given size of a set
lst=list(eval(input("Enter the set\n")))
k=int(input("Enter size of subsets: "))
st=[]
for i in range(1,pow(2,len(lst))):
    ls=list(str(bin(i))[2:].zfill(len(lst)))
    l=[]
    if(ls.count('1')==k):
        for j in range(len(ls)):
            if(ls[j]=='1'):
                l.append(lst[j])
        st.append(set(l))
print(st)