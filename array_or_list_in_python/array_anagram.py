# program to find no. of strings is anagram in given array

st1=eval(input())
st2=eval(input())
for i in range(len(st1)):
    st1[i]=sorted(st1[i])
for i in range(len(st2)):
    st2[i]=sorted(st2[i])
c=0
for i in st1:
    if i in st2:
        c+=1
print(c)



