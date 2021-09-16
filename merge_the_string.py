r=int(input("Enter no. of string: "))
c=int(input("Enter the length of each string: "))
lst=[]
lst2=[]
for i in range(r):
    st=input()
    lst.append(st)
for k in range(c):
    lst1=list(map(lambda i: i[k], lst))
    st1="".join(lst1)
    lst2.append(st1)
st2="".join(lst2)
for i in st2:
    if(ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=95):
        continue
    st2=st2.replace(i,' ')
print(st2)

